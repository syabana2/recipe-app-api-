from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a user with email is successfull"""
        email = "rizkisyaban2@gmail.com"
        password = 'rahasia2020'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """Test for normalize new user email"""
        email = "rizkisyaban2@GMAIL.COM"
        user = get_user_model().objects.create_user(email, 'testing123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_without_email(self):
        """Test creating user without email and raise the error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'testing123')

    def test_create_super_user(self):
        """Test creating a super user"""
        user = get_user_model().objects.create_superuser(
            'rizkisyaban2@gmail.com',
            'testing1234'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)