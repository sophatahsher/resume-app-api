"""
Test for models.
"""
from decimal import Decimal

from unittest.mock import patch
from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


class ModelTests(TestCase):
    """Test models."""

    def test_create_user_with_successful(self):
        """Test creating a user with an email is successful."""
        email = 'test@example.com'
        password = '123456'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users."""
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test that creating a user without an email raises a ValueError."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')

    def test_create_superuser(self):
        """Test creating a superuser."""
        user = get_user_model().objects.create_superuser(
            'superdev@example.com',
            'super123456'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_resume(self):
        """Test creating a resume is successful."""
        user = get_user_model().objects.create_user(
            'test@example.com',
            '123456'
        )
        recipe = models.Recipe.objects.create(
            user=user,
            title='Avocado Durian Smoothie Recipe',
            description='How to create avocado durian smoothie',
            time_minutes=15,
            price=Decimal('4.50')
        )

        self.assertEqual(str(recipe), recipe.title)

    @patch('core.models.uuid.uuid4')
    def test_recipe_file_name_uuid(self, mock_uuid):
        """Test generating image path."""
        uuid = 'test-uuid'
        mock_uuid.return_value = uuid
        file_path = models.recipe_image_file_path(None, 'example.jpg')

        self.assertEqual(file_path, f'uploads/recipe/{uuid}.jpg')
