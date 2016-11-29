from django.core.urlresolvers import reverse
from django.db.utils import IntegrityError
from django.test import Client, TestCase

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


class BookInventoryListViewTest(TestCase):
    """Test for BookInventoryListView."""

    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name='Biology')
        self.book = Book.objects.create(
            title='Human Brain',
            authors='Liskov and Rajkput',
            category=self.category
        )

    def test_bookpage_is_up(self):
        response = self.client.get('/')

        self.assertEquals(200, response.status_code)

    def test_bookpage_for_a_specific_category_is_up(self):
        response = self.client.get(reverse('inventory:bookpage', args='1'))

        self.assertEquals('Human Brain', [book for book in response.context_data['books']][0].title)

    def test_search_with_book_title_insensitive(self):
        response = self.client.get('/', data={'q': 'Human Brain'})

        self.assertEquals('Human Brain', [book for book in response.context_data['books']][0].title)

    def test_search_with_book_title_sensitive(self):
        response = self.client.get('/', data={'q': 'huMan braIn'})

        self.assertEquals('Human Brain', [book for book in response.context_data['books']][0].title)

    def test_search_with_book_title_incomplete(self):
        response = self.client.get('/', data={'q': 'Huma'})

        self.assertEquals('Human Brain', [book for book in response.context_data['books']][0].title)

    def test_search_with_category_name_complete(self):
        response = self.client.get('/', data={'q': 'Biology'})

        self.assertEquals('Human Brain', [book for book in response.context_data['books']][0].title)

    def test_search_with_category_name_incomplete(self):
        response = self.client.get('/', data={'q': 'Bio'})

        self.assertEquals([], [book for book in response.context_data['books']])
