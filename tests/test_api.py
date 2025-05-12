import json
from app import create_app
from app.backend.models import db

app = create_app()
app.testing = True

def test_create_task():
    client = app.test_client()
    response = client.post('/api/tasks', json={
        "title": "Test Task",
        "description": "This is a test"
    })
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['title'] == "Test Task"

def test_get_tasks():
    client = app.test_client()
    response = client.get('/api/tasks')
    assert response.status_code == 200
    assert isinstance(json.loads(response.data), list)

