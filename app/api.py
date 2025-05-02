# app/api.py
from flask import Blueprint, request, jsonify
from app.models import tasks

api = Blueprint('api', __name__)

@api.route('/')
def index():
    return redirect(url_for('api.index'))  # Redirects to /api/

@api.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@api.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify(task)

@api.route('/tasks', methods=['POST'])
def create_task():
    if not request.json or 'title' not in request.json:
        return jsonify({'error': 'Title is required'}), 400
    task = {
        'id': len(tasks) + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ''),
        'done': False
    }
    tasks.append(task)
    return jsonify(task), 201

@api.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    if not request.json:
        return jsonify({'error': 'Request body is required'}), 400
    task['title'] = request.json.get('title', task['title'])
    task['description'] = request.json.get('description', task['description'])
    task['done'] = request.json.get('done', task['done'])
    return jsonify(task)

@api.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({'message': 'Task deleted'})
