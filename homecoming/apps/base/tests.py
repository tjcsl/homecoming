import datetime
import json

from django.urls import reverse
from django.utils import timezone

from ...test.homecoming_test import HomecomingTestCase
from ..events.models import Event
from ..scores.models import ScoreBoard


class BaseTestCase(HomecomingTestCase):
    def test_index_view(self):
        self.login(username="2020awilliam", make_student=True, make_superuser=False)

        # As of now, there should be no events and zero scores.
        response = self.client.get(reverse("base:index"))
        self.assertEqual(0, len(response.context["events"]))
        self.assertEqual(0, len(response.context["scoreboards"]))
        self.assertEqual(0, response.context["freshman_total"])
        self.assertEqual(0, response.context["sophomore_total"])
        self.assertEqual(0, response.context["junior_total"])
        self.assertEqual(0, response.context["senior_total"])

        # Create an event
        event = Event.objects.create(
            name="test",
            description="test",
            location="200D",
            start_time=timezone.now(),
            end_time=timezone.now() + datetime.timedelta(1),
        )
        response = self.client.get(reverse("base:index"))
        self.assertEqual(1, len(response.context["events"]))
        self.assertIn(event, response.context["events"])

        # Create a scoreboard for said event
        ScoreBoard.objects.create(
            event=event,
            freshman_score=1,
            sophomore_score=2,
            junior_score=3,
            senior_score=4,
        )
        response = self.client.get(reverse("base:index"))
        self.assertEqual(1, response.context["freshman_total"])
        self.assertEqual(2, response.context["sophomore_total"])
        self.assertEqual(3, response.context["junior_total"])
        self.assertEqual(4, response.context["senior_total"])

        # Now create another event and a corresponding scoreboard
        event2 = Event.objects.create(
            name="test2",
            description="test2",
            location="200C",
            start_time=timezone.now(),
            end_time=timezone.now() + datetime.timedelta(2),
        )
        response = self.client.get(reverse("base:index"))
        self.assertEqual(2, len(response.context["events"]))
        self.assertIn(event2, response.context["events"])

        ScoreBoard.objects.create(
            event=event2,
            freshman_score=4,
            sophomore_score=5,
            junior_score=6,
            senior_score=7,
        )
        response = self.client.get(reverse("base:index"))
        self.assertEqual(5, response.context["freshman_total"])
        self.assertEqual(7, response.context["sophomore_total"])
        self.assertEqual(9, response.context["junior_total"])
        self.assertEqual(11, response.context["senior_total"])

    def test_api_view(self):
        self.login(username="2020awilliam", make_student=True, make_superuser=False)
        response = json.loads(self.client.get(reverse("base:api")).content)

        # These should be None because there are no ScoreBoards created yet
        self.assertEqual(None, response["freshman_total"])
        self.assertEqual(None, response["sophomore_total"])
        self.assertEqual(None, response["junior_total"])
        self.assertEqual(None, response["senior_total"])

        # Create an event
        event = Event.objects.create(
            name="test",
            description="test",
            location="200D",
            start_time=timezone.now(),
            end_time=timezone.now() + datetime.timedelta(1),
        )
        response = self.client.get(reverse("base:index"))
        self.assertEqual(1, len(response.context["events"]))
        self.assertIn(event, response.context["events"])

        # Create a scoreboard for said event
        ScoreBoard.objects.create(
            event=event,
            freshman_score=1,
            sophomore_score=2,
            junior_score=3,
            senior_score=4,
        )

        response = json.loads(self.client.get(reverse("base:api")).content)
        self.assertEqual(1, response["freshman_total"])
        self.assertEqual(2, response["sophomore_total"])
        self.assertEqual(3, response["junior_total"])
        self.assertEqual(4, response["senior_total"])

        # Now create another event and a corresponding scoreboard
        event2 = Event.objects.create(
            name="test2",
            description="test2",
            location="200C",
            start_time=timezone.now(),
            end_time=timezone.now() + datetime.timedelta(2),
        )
        response = self.client.get(reverse("base:index"))
        self.assertEqual(2, len(response.context["events"]))
        self.assertIn(event2, response.context["events"])

        ScoreBoard.objects.create(
            event=event2,
            freshman_score=4,
            sophomore_score=5,
            junior_score=6,
            senior_score=7,
        )

        response = json.loads(self.client.get(reverse("base:api")).content)
        self.assertEqual(5, response["freshman_total"])
        self.assertEqual(7, response["sophomore_total"])
        self.assertEqual(9, response["junior_total"])
        self.assertEqual(11, response["senior_total"])

    def test_reset_view(self):
        # Test as an unprivileged user
        self.login(username="2020awilliam", make_student=True, make_superuser=False)
        response = self.client.get(reverse("base:reset"), follow=True)
        self.assertTemplateNotUsed(response, "base/reset.html")

        # Test as a privileged user
        self.login(username="2020awilliam", make_student=True, make_superuser=True)
        response = self.client.get(reverse("base:reset"), follow=True)
        self.assertTemplateUsed(response, "base/reset.html")

        # Make an event
        event = Event.objects.create(
            name="test",
            description="test",
            location="200D",
            start_time=timezone.now(),
            end_time=timezone.now() + datetime.timedelta(1),
        )

        # Create a scoreboard for said event
        ScoreBoard.objects.create(
            event=event,
            freshman_score=1,
            sophomore_score=2,
            junior_score=3,
            senior_score=4,
        )

        response = self.client.post(reverse("base:reset"), follow=True)
        self.assertTemplateUsed(response, "base/home.html")
        self.assertEqual(0, len(Event.objects.all()))
        self.assertEqual(0, len(ScoreBoard.objects.all()))
