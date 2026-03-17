from flask import Blueprint, request, jsonify, g
from models.task import Task

# Services
from services.create_new_task import create_new_task
from services.get_all_tasks import get_all_tasks
from services.find_task_by_id import find_task_by_id
from services.update_task import update_task_service
from services.delete_task import delete_task_service

# Middlewares
from middleware.auth_middle import auth_require

task_bp = Blueprint('tasks', __name__, url_prefix='/tasks')

tasks = []

task_id_control = 1

# Create
@task_bp.post('/')
@auth_require
def create_task():
    global task_id_control

    data = request.get_json()

    # result if case return something
    result = create_new_task(data)

    return jsonify({
        'message': 'Nova tarefa criada com sucesso'
    }), 201

# Read 
@task_bp.get('/')
@auth_require
def view_tasks():
    return jsonify({
        "tasks": get_all_tasks()
    })

# Read-One
@task_bp.get('/<int:id>')
@auth_require
def get_one_task(id):
    print(g.user_id)
    task = find_task_by_id(id)

    if task:
        return jsonify({ "task": task }), 302
    else:
        return jsonify({ "message": 'Não foi encontrada nenhuma tarefa!'}), 404
    
@task_bp.put('/<int:id>')
@auth_require
def update_task(id):
    data = request.get_json()

    task = update_task_service(id, data)

    if task:
        return jsonify({
            "message": "Tarefa atualiza com sucesso!",
            "task": task
        })
    else:
        return jsonify({
            "message": 'Não foi possivel encontrar a tarefa'
        }), 404
    
@task_bp.delete('/<int:id>')
@auth_require
def delete_task(id):
    task_deleted = delete_task_service(id)

    return jsonify({
        "message": "Sua tarefa foi deletada com sucesso!" if task_deleted else "Não foi possivel deletar sua tarefa"
    })