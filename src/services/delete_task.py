from repository.task_repository import task_repository

def delete_task_service(id):
    return task_repository.delete_task_by_id(id)