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
    
@task_bp.put('/<int:id>')
def update_task(id):
    global task
    task = None

    data = request.get_json()

    for taskItem in tasks:
        if taskItem['id'] == id:
            task = taskItem
        else:
            continue

    if task:
        task['title'] = data.get('title') or task['title']
        task['description'] = data.get('description') or task['description']
        task['completed'] = data.get('completed') if data.get('completed') is not None else task['completed']

        return jsonify({
            "message": "Tarefa atualiza com sucesso!",
            "task": task
        })
    else:
        return jsonify({
            "message": 'Não foi possivel encontrar a tarefa'
        }), 404