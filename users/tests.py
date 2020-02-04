from django.test import TestCase
from django.contrib.auth import get_user_model


User = get_user_model()


class TestCustomUser(TestCase):
    def setUp(self):
        self.sup_user = User.objects.create_superuser(
            'admin01', 'admin1@gmail.com', 'testing321')
        self.user = User.objects.create_user(
            'johndoe', 'johndoe@gmail.com', 'testing123')

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'johndoe')
        self.assertEqual(self.user.email, 'johndoe@gmail.com')
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

    def test_superuser_creation(self):
        self.assertEqual(self.sup_user.username, 'admin01')
        self.assertEqual(self.sup_user.email, 'admin1@gmail.com')
        self.assertTrue(self.sup_user.is_active)
        self.assertTrue(self.sup_user.is_staff)
        self.assertTrue(self.sup_user.is_superuser)


# users/tests.py



