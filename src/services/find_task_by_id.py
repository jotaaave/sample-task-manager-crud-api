from repository.task_repository import task_repository

def find_task_by_id(id):
    return task_repository.find_by_id(id)