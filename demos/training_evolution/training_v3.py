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
from dataclasses import dataclass, field


class TrainingFullException(Exception):
    ...


@dataclass(frozen=True)
class Student:
    name:str
    title:str = field(default=None, compare=False)
    company: str|None = None


class Address:
    pass


@dataclass(frozen=True)
class Venue:
    name:str
    address:Address
    room_number:int
    capacity:int


@dataclass(frozen=True)
class Training:
    subject:str
    content:str
    duration:int
    price:int
    max_seats:int=12


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
