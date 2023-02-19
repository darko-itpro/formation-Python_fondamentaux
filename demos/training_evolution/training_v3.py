"""
Ces modules vont présenter l'évolution du modèle de la formation.

Cette version est la version qui a la structure la plus complète où la
_formation_ proposée précédemment représente réellement une _session_.
La notion de formation en elle-même ne contient que les données d'un
_catalogue_.

À ceci s'ajoute la notion de lieu. Les informations de la session doivent donc
aller y chercher le nombre de places disponibles.
"""


from datetime import datetime


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


class Address:
    pass


class Venue:
    def __init__(self, name: str, address: Address, room_number: int, capacity: int):
        self.name = name
        self.address = address
        self.room_number = room_number
        self.capacity = capacity


class Training:
    def __init__(self, subject: str, duration: int, price: float,
                 content: str = "", max_seats: int = 12):
        self.subject = subject
        self.content = content
        self.duration = int(duration)
        self.max_seats = int(max_seats)
        self.price = price


class TrainingSession:
    def __init__(self, training: Training, start_date: datetime, venue: Venue = None):
        self.training = training
        self.start_date = start_date
        self.venue = venue
        self._students = []

        if start_date.weekday() + training.duration > 4:  # La fin est-elle après le vendredi
            raise ValueError(f"Incompatible start date {start_date}")

    @property
    def subject(self):
        return self.training.subject

    @property
    def duration(self):
        return self.training.duration

    @property
    def available_seats(self):
        seats_left = self.capacity - len(self._students)
        return seats_left if seats_left >= 0 else 0

    @property
    def capacity(self):
        return min(self.training.max_seats, self.venue.capacity)

    @property
    def students(self):
        return self._students.copy()

    def add_student(self, student: Student):
        if not self.available_seats:
            raise TrainingFullException('Training full')

        if student in self._students:
            raise ValueError("Student already in training")

        self.students.append(student)
