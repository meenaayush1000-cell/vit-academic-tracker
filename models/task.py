class Task:
    def __init__(self, task_id, title, category, deadline, priority, is_completed=False):
        self.task_id = task_id
        self.title = title
        self.category = category
        self.deadline = deadline
        self.priority = priority
        self.is_completed = is_completed

    def mark_done(self):
        self.is_completed = True

    def get_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "category": self.category,
            "deadline": self.deadline,
            "priority": self.priority,
            "is_completed": self.is_completed
        }
