from flask import Blueprint, request, jsonify
from app.backend.models import db, Task

api_routes = Blueprint('api', __name__)

@api_routes.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks])

@api_routes.route('/api/tasks', methods=['POST'])
def create_task():
    data = request.json
    new_task = Task(title=data['title'], description=data.get('description', ''))
    db.session.add(new_task)
    db.session.commit()
    return jsonify(new_task.to_dict()), 201

@api_routes.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.json
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
    db.session.commit()
    return jsonify(task.to_dict())

@api_routes.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return '', 204

