from rest_framework.test import APITestCase
from django.urls import reverse
from uuid import UUID
from api.models import Note


class NotesCrudTests(APITestCase):
    def test_crud_flow(self):
        # Health
        url = reverse('Health')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

        # Create
        create_url = "/api/notes/"
        payload = {"title": "My Note", "content": "Hello"}
        resp = self.client.post(create_url, payload, format='json')
        self.assertEqual(resp.status_code, 201)
        note_id = resp.data["id"]
        # Validate is UUID
        UUID(note_id)

        # Retrieve
        retrieve_url = f"/api/notes/{note_id}/"
        resp = self.client.get(retrieve_url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data["title"], "My Note")

        # Update (PUT)
        resp = self.client.put(retrieve_url, {"title": "Updated", "content": "World"}, format='json')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data["title"], "Updated")

        # Partial update (PATCH)
        resp = self.client.patch(retrieve_url, {"content": "World!!"}, format='json')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data["content"], "World!!")

        # List with pagination
        list_url = "/api/notes/"
        resp = self.client.get(list_url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn("results", resp.data)

        # Delete
        resp = self.client.delete(retrieve_url)
        self.assertEqual(resp.status_code, 204)
        self.assertFalse(Note.objects.filter(id=note_id).exists())
