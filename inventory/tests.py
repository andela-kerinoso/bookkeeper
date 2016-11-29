from django.db.utils import IntegrityError
from django.test import TestCase

from .models import Book, Category


class CategoryTest(TestCase):
    """Test for Category model."""

    def setUp(self):
        self.category = Category.objects.create(name='Biology')

    def test_uniqueness_of_category_name(self):
        category = Category(name='Biology')

        self.assertRaises(IntegrityError, category.save)


class BookTest(TestCase):
    """Test for Book model."""

    def setUp(self):
        self.category = Category.objects.create(name='Biology')
        self.book = Book.objects.create(
            title='Human Brain',
            authors='Liskov and Rajkput',
            category=self.category
        )

    def test_unique_together_of_title_and_authors(self):
        category = Category.objects.create(name='Siocology')
        book = Book(
            title=self.book.title,
            authors=self.book.authors,
            category=category
        )

        self.assertRaises(IntegrityError, book.save)
