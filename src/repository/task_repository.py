from models.task import Task

class TaskRepositoryInMemory:
    def __init__(self):
        self.tasks = []
        self.task_id_control = 1
    
    def add_task(self, task):
        new_task = Task(id=self.task_id_control, title=task.get('title'), description=task.get("description", "")).to_dict()
        
        self.tasks.append(new_task)
        self.task_id_control += 1

    def get_tasks(self):
        print(self.tasks)
        return self.tasks
    
    def find_by_id(self, id):
        global selected_task
        selected_task = None

        for t in self.tasks:
            if t['id'] == id:
                selected_task = t
                break
            else:
                continue

        return selected_task
    
    def update_task(self, id, data):
        task = self.find_by_id(id)

        if not task:
            return None
        
        task['title'] = data.get('title') or task['title']
        task['description'] = data.get('description') or task['description']
        task['completed'] = data.get('completed') if data.get('completed') is not None else task['completed']

        return task

task_repository = TaskRepositoryInMemory()