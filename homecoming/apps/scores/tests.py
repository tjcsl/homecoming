import datetime

from django.urls import reverse
from django.utils import timezone

from ...test.homecoming_test import HomecomingTestCase
from ..events.models import Event
from .models import ScoreBoard


class ScoresTestCase(HomecomingTestCase):
    def test_edit_scores_view(self):
        self.login(make_teacher=True, make_superuser=True)

        event = Event.objects.create(
            name="test",
            description="test",
            location="200D",
            start_time=timezone.now(),
            end_time=timezone.now() + datetime.timedelta(1),
        )

        scoreboard = ScoreBoard.create(event=event)

        response = self.client.get(
            reverse("scores:edit_scores", kwargs={"event_id": event.id}), follow=True
        )
        self.assertEqual(200, response.status_code)

        # Test editing an event
        response = self.client.post(
            reverse("scores:edit_scores", kwargs={"event_id": event.id}),
            follow=True,
            data={
                "name": "test-modify",
                "description": "haha",
                "location": event.location,
                "start_time": event.start_time,
                "end_time": event.end_time,
                "event_info": True,
            },
        )

        self.assertEqual(200, response.status_code)
        self.assertEqual(
            1,
            len(
                Event.objects.filter(
                    name="test-modify", description="haha", location=event.location
                )
            ),
        )

        # Test invalid values
        # End date before start date
        response = self.client.post(
            reverse("scores:edit_scores", kwargs={"event_id": event.id}),
            follow=True,
            data={
                "name": "test-modify",
                "description": "haha",
                "location": event.location,
                "start_time": event.start_time,
                "end_time": event.start_time - timezone.timedelta(days=1),
                "event_info": True,
            },
        )

        self.assertEqual(200, response.status_code)
        self.assertEqual(
            1, len(Event.objects.filter(end_time=event.end_time, name="test-modify"))
        )

        # Test editing scores
        response = self.client.post(
            reverse("scores:edit_scores", kwargs={"event_id": event.id}),
            follow=True,
            data={
                "freshman_score": 1,
                "sophomore_score": 2,
                "junior_score": 3,
                "senior_score": 4,
                "event_score": True,
            },
        )

        self.assertEqual(200, response.status_code)
        self.assertEqual(1, ScoreBoard.objects.get(id=scoreboard.id).freshman_score)
        self.assertEqual(2, ScoreBoard.objects.get(id=scoreboard.id).sophomore_score)
        self.assertEqual(3, ScoreBoard.objects.get(id=scoreboard.id).junior_score)
        self.assertEqual(4, ScoreBoard.objects.get(id=scoreboard.id).senior_score)

        # Test an invalid value
        response = self.client.post(
            reverse("scores:edit_scores", kwargs={"event_id": event.id}),
            follow=True,
            data={
                "freshman_score": "sdlkj2",
                "sophomore_score": "sdlf",
                "junior_score": "haha",
                "senior_score": "sdfd",
                "event_score": True,
            },
        )

        self.assertEqual(200, response.status_code)
        # i.e. assert nothing changed
        self.assertEqual(1, ScoreBoard.objects.get(id=scoreboard.id).freshman_score)
        self.assertEqual(2, ScoreBoard.objects.get(id=scoreboard.id).sophomore_score)
        self.assertEqual(3, ScoreBoard.objects.get(id=scoreboard.id).junior_score)
        self.assertEqual(4, ScoreBoard.objects.get(id=scoreboard.id).senior_score)

    def test_scoreboard_model(self):
        # Only because I like 100% coverage. :)
        event = Event.objects.create(
            name="test1234!",
            description="test",
            location="200D",
            start_time=timezone.now(),
            end_time=timezone.now() + datetime.timedelta(1),
        )

        scoreboard = ScoreBoard.create(event=event)
        self.assertEqual("test1234!", str(scoreboard))
