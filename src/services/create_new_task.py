from repository.task_repository import task_repository

def create_new_task(data):
    task_repository.add_task(data)