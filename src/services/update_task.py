from repository.task_repository import task_repository

def update_task_service(id, data):
    return task_repository.update_task(id, data)