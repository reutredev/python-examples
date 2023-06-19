import unittest
from fastapi.testclient import TestClient
from fast_api_server.fastapi_server import app, Task

client = TestClient(app)

class TestApp(unittest.TestCase):
    def setUp(self):
        self.tasks = [
            Task(id=1, title='Task 1', description='Description 1'),
            Task(id=2, title='Task 2', description='Description 2'),
        ]

    def test_get_tasks(self):
        response = client.get('/tasks')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), self.tasks)

    def test_get_task(self):
        response = client.get('/tasks/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), self.tasks[0])

    def test_get_task_not_found(self):
        response = client.get('/tasks/3')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()['detail'], 'Task not found')

    def test_create_task(self):
        new_task = Task(id=3, title='Task 3', description='Description 3')
        response = client.post('/tasks', json=new_task.dict())
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), new_task)
        # Check if the task is added to the tasks list
        response = client.get('/tasks')
        self.assertIn(new_task, response.json())

    def test_update_task(self):
        updated_task = Task(id=1, title='Updated Task', description='Updated Description')
        response = client.put('/tasks/1', json=updated_task.dict())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), updated_task)
        # Check if the task is updated in the tasks list
        response = client.get('/tasks/1')
        self.assertEqual(response.json(), updated_task)

    def test_update_task_not_found(self):
        updated_task = Task(id=3, title='Updated Task', description='Updated Description')
        response = client.put('/tasks/3', json=updated_task.dict())
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()['detail'], 'Task not found')

    def test_delete_task(self):
        response = client.delete('/tasks/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message': 'Task deleted'})
        # Check if the task is removed from the tasks list
        response = client.get('/tasks')
        self.assertNotIn(self.tasks[0], response.json())

    def test_delete_task_not_found(self):
        response = client.delete('/tasks/3')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()['detail'], 'Task not found')

if __name__ == '__main__':
    unittest.main()
