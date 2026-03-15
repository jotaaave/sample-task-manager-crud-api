from flask import Blueprint, request, jsonify
from models.task import Task

task_bp = Blueprint('tasks', __name__, url_prefix='/tasks')

tasks = []

task_id_control = 1

# Create
@task_bp.post('/')
def create_task():
    global task_id_control

    data = request.get_json()

    new_task = Task(id=task_id_control, title=data['title'], description=data.get("description", "")).to_dict()
    tasks.append(new_task)

    task_id_control += 1

    print(new_task)
    print(tasks)

    return jsonify({
        'message': 'Nova tarefa criada com sucesso'
    }), 201

# Read 
@task_bp.get('/')
def view_tasks():
    return jsonify({
        "tasks": tasks
    })

# Read-One
@task_bp.get('/<int:id>')
def get_one_task(id):
    global selected_task
    selected_task = {}

    for task in tasks:
        if task['id'] == id:
            selected_task = task
            break
        else:
            continue

    if selected_task:
        return jsonify({ "task": selected_task }), 302
    else:
        return jsonify({ "message": 'Não foi encontrada nenhuma tarefa!'}), 404