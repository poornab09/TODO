class Task:
    def __init__(self, title, priority="Medium", deadline=None, completed=False):
        self.title = title
        self.priority = priority
        self.deadline = deadline
        self.completed = completed

    def to_dict(self):
        return {
            "title": self.title,
            "priority": self.priority,
            "deadline": self.deadline,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data):
        return Task(
            data["title"],
            data["priority"],
            data["deadline"],
            data["completed"]
        )