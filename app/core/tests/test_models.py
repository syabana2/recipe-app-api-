from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='test@allein.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


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

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """Test the ingredient representation"""
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Cucumber'
        )

        self.assertEqual(str(ingredient), ingredient.name)