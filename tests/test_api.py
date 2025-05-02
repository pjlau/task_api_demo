# tests/test_api.py
import unittest
from app import create_app
import json
from app.models import tasks

class TestTaskAPI(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True
        # Reset tasks list before each test
        tasks.clear()  # Clear the tasks list to ensure a clean state

    def test_create_task(self):
        response = self.client.post('/api/tasks', json={'title': 'Test Task'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data)['title'], 'Test Task')

    def test_get_tasks(self):
        self.client.post('/api/tasks', json={'title': 'Test Task'})
        response = self.client.get('/api/tasks')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(json.loads(response.data)) > 0)

    def test_get_task(self):
        response = self.client.post('/api/tasks', json={'title': 'Test Task'})
        self.assertEqual(response.status_code, 201)  # Ensure POST succeeds
        response = self.client.get('/api/tasks/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['title'], 'Test Task')

    def test_update_task(self):
        response = self.client.post('/api/tasks', json={'title': 'Test Task'})
        self.assertEqual(response.status_code, 201)  # Ensure POST succeeds
        response = self.client.put('/api/tasks/1', json={'title': 'Updated Task'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['title'], 'Updated Task')

    def test_delete_task(self):
        self.client.post('/api/tasks', json={'title': 'Test Task'})
        response = self.client.delete('/api/tasks/1')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/api/tasks/1')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
