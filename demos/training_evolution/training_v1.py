"""
Ces modules vont présenter l'évolution du modèle de la formation.

Cette seconde version ferme la notion de _places disponibles_ pour exposer sous
forme de properties la capacité et les places disponibles (calculé).
"""


class TrainingFullException(Exception):
    ...


class Training:
    def __init__(self, subject: str, duration: int, capacity: int = 12):
        self._subject = subject
        self._duration = int(duration)
        self._capacity = int(capacity)
        self._students = []

        if self._capacity < 1:
            raise ValueError(f"Capacity must be positive, "
                             f"got {self.available_seats}")

    @property
    def subject(self):
        return self._subject

    @property
    def duration(self):
        return self._duration

    @property
    def capacity(self):
        return self._capacity

    @property
    def available_seats(self):
        return self.available_seats - len(self._students)

    @property
    def students(self):
        return self._students.copy()

    def add_student(self, name: str):
        if len(self.students) >= self.available_seats:
            raise TrainingFullException('Training full')

        self.students.append(name)
