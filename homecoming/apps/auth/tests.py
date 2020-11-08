from ...test.homecoming_test import HomecomingTestCase


class AuthTest(HomecomingTestCase):
    def test_login_view(self):
        # I am currently unauthenticated.
        response = self.client.get("/", follow=True)
        self.assertTemplateUsed(response, "auth/login.html")

        # Now, authenticate myself
        user = self.login("awilliam", make_teacher=True, make_student=False)
        response = self.client.get("/", follow=True)
        self.assertTemplateNotUsed(response, "auth/login.html")
        self.assertTemplateUsed(response, "base/home.html")

        self.assertEqual("awilliam", user.short_name)
        self.assertEqual("awilliam", str(user))
