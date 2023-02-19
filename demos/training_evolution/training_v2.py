"""
Ces modules vont présenter l'évolution du modèle de la formation.

Cette troisième version propose la notion de stagiaire sous forme d'objet.
"""


class TrainingFullException(Exception):
    ...


class Student:
    def __init__(self, name: str, title: str, company: str = None):
        self.name = name
        self.title = title
        self.company = company

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False

        return (self.name, self.company) == (other.name, other.company)


class Training:
    def __init__(self, subject: str, duration: int, capacity: int = 12):
        self.subject = subject
        self.duration = int(duration)
        self._capacity = int(capacity)
        self._students = []

        if self._capacity < 1:
            raise ValueError(f"Capacity must be positive, "
                             f"got {self.available_seats}")

    @property
    def capacity(self):
        return self._capacity

    @property
    def available_seats(self):
        return self.available_seats - len(self._students)

    @property
    def students(self):
        return self._students.copy()

    def add_student(self, student: Student):
        if len(self.students) >= self.available_seats:
            raise TrainingFullException('Training full')

        if student in self._students:
            raise ValueError("Student already in training")

        self.students.append(student)
