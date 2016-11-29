from django.db.utils import IntegrityError
from django.test import TestCase

from .models import Category


class CategoryTest(TestCase):
    """Test for Category model."""

    def setUp(self):
        self.category = Category.objects.create(name='Biology')

    def test_uniqueness_of_category_name(self):
        category = Category(name='Biology')

        self.assertRaises(IntegrityError, category.save)
