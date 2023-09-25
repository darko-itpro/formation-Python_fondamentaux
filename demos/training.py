
class TraininfFullException(Exception):
    ...

class Training:
    def __init__(self, subject: str, duration: int, capacity: int = 12):
        self.subject = subject
        self.duration = int(duration)
        self.available_seats = int(capacity)
        self._students = []

        if self.available_seats < 1:
            raise TraininfFullException(f"Capacity must be positive, "
                                        f"got {self.available_seats}")

    @property
    def remaining_seats(self):
        return self.available_seats - len(self._students)

    @property
    def students(self):
        return self._students.copy()

    def add_student(self, name:str):
        if len(self.students) >= self.available_seats:
            raise ValueError('Training full')

        self.students.append(name)

class Person:
    def __init__(self, name:str, title:str):
        if len(name) < 2:
            raise ValueError("Name too short")

        self.name = name
        self.title = title


class Student(Person):
    def __init__(self, name:str, title:str, company:str=None):
        super().__init__(name, title)
        self.company = company
