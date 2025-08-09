from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book


class BookAPITests(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpass123")
        self.client.login(username="testuser", password="testpass123")

        # Create some books
        self.book1 = Book.objects.create(title="Omwami", author="barasa", publication_year=2024)
        self.book2 = Book.objects.create(title="Omwami 1", author="Norah mgandi", publication_year=2002)
        self.book3 = Book.objects.create(title="Omwami 2", author="Norah mgandi", publication_year=2023)

        self.list_url = reverse("book-list")  # Adjust to your URL name

    # ---------- CRUD TESTS ----------
    def test_create_book(self):
        data = {"title": "Django for APIs", "author": "William S. Vincent", "publication_year": 2018}
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)
        self.assertEqual(Book.objects.last().title, "Django for APIs")

    def test_retrieve_books_list(self):
        response = self.client.get(self.list_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_update_book(self):
        url = reverse("book-detail", args=[self.book1.id])
        data = {"title": "Omwami 1 updated", "author": "Norah mgandi", "publication_year": 2002}
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Omwami updated")

    def test_delete_book(self):
        url = reverse("book-detail", args=[self.book1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 2)

    # ---------- FILTERING / SEARCH / ORDER ----------
    def test_filter_books_by_author(self):
        response = self.client.get(self.list_url + "?author=Norah mgandi")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(book["author"] == "Norah mgandi" for book in response.data))

    def test_search_books_by_title(self):
        response = self.client.get(self.list_url + "?search=Omwami 1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any("Omwami 1" in book["title"] for book in response.data))

    def test_order_books_by_publication_year_desc(self):
        response = self.client.get(self.list_url + "?ordering=-publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book["publication_year"] for book in response.data]
        self.assertEqual(years, sorted(years, reverse=True))

    # ---------- PERMISSIONS ----------
    def test_cannot_create_book_without_authentication(self):
        self.client.logout()
        data = {"title": "Unauthorized Book", "author": "Unknown", "publication_year": 2025}
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
