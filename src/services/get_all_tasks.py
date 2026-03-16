from repository.task_repository import task_repository

def get_all_tasks():
    return task_repository.get_tasks()