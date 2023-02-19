"""
Ces modules vont présenter l'évolution du modèle de la formation.

Cette première version correspond à ce qui a été présenté en formation. La version
est _simple_ avec une méthode d'ajout de stagiaire et une property pour l'accès.
"""


class TrainingFullException(Exception):
    ...


class Training:
    def __init__(self, subject: str, duration: int, capacity: int = 12):
        self.subject = subject
        self.duration = int(duration)
        self.available_seats = int(capacity)
        self._students = []

        if self.available_seats < 1:
            raise ValueError(f"Capacity must be positive, "
                             f"got {self.available_seats}")

    @property
    def students(self):
        return self._students.copy()

    def add_student(self, name: str):
        if len(self.students) >= self.available_seats:
            raise TrainingFullException('Training full')

        self.students.append(name)
