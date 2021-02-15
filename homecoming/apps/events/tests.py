import datetime
import json

from django.urls import reverse
from django.utils import timezone

from ...test.homecoming_test import HomecomingTestCase
from .models import Event
from .views import unix_time_millis


class EventsTestCase(HomecomingTestCase):
    def test_create_event_view(self):
        self.login(make_teacher=True, make_superuser=True)

        response = self.client.get(reverse("events:create_event_page"), follow=True)
        self.assertTemplateUsed(response, "events/create_event_form.html")

        response = self.client.post(
            reverse("events:create_event_page"),
            follow=True,
            data={
                "name": "Test Activity",
                "description": "Hello there!",
                "location": "200C",
                "start_time": "2020/11/07 21:00",
                "end_time": "2020/11/08 21:00",
            },
        )
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, len(Event.objects.filter(name="Test Activity")))

        # Test start time > end time
        response = self.client.post(
            reverse("events:create_event_page"),
            follow=True,
            data={
                "name": "Test Activity",
                "description": "Hello there!",
                "location": "200C",
                "start_time": "2020/11/07 21:00",
                "end_time": "2020/11/06 21:00",
            },
        )
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, len(Event.objects.filter(name="Test Activity")))

    def test_delete_event_view(self):
        self.login(make_teacher=True, make_superuser=True)
        event = Event.create(
            name="test",
            description="test",
            location="200D",
            start_time=timezone.now(),
            end_time=timezone.now() + datetime.timedelta(1),
        )
        response = self.client.post(
            reverse("events:delete", kwargs={"pk": event.id}), follow=True
        )
        self.assertEqual(200, response.status_code)

        self.assertEqual(0, len(Event.objects.filter(name="test")))

    def test_calendar_data_view(self):
        self.login(make_teacher=True, make_superuser=False)

        response = json.loads(
            self.client.get(reverse("events:calendar_source"), follow=True).content
        )
        self.assertDictEqual({"success": 1, "result": []}, response)

        event = Event.create(
            name="test",
            description="test",
            location="200D",
            start_time=timezone.now(),
            end_time=timezone.now() + datetime.timedelta(1),
        )

        response = json.loads(
            self.client.get(reverse("events:calendar_source"), follow=True).content
        )
        self.assertDictEqual(
            {
                "success": 1,
                "result": [
                    {
                        "id": event.id,
                        "title": event.name,
                        "start": unix_time_millis(event.start_time),
                        "end": unix_time_millis(event.end_time),
                    }
                ],
            },
            response,
        )

    def test_event_model(self):
        # Only because I like 100% coverage. :)
        event = Event.create(
            name="test123!",
            description="test",
            location="200D",
            start_time=timezone.now(),
            end_time=timezone.now() + datetime.timedelta(1),
        )
        self.assertEqual("test123!", str(event))
