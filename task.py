class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.task_id_counter = 1

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append((self.task_id_counter, task))
        self.task_id_counter += 1

    def view_tasks(self):
        print("\nTask List:")
        for task_id, task in self.tasks:
            status = "Completed" if task.completed else "Pending"
            print(f"{task_id}. {task.title} - {status}")

    def mark_task_completed(self, task_id):
        for task_id_, task in self.tasks:
            if task_id_ == task_id:
                task.mark_completed()
                return

    def remove_task(self, task_id):
        self.tasks = [(task_id_, task) for task_id_, task in self.tasks if task_id_ != task_id]
