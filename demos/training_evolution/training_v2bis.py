"""
Ces modules vont présenter l'évolution du modèle de la formation.

Cette variation de la troisième version propose la notion de stagiaire sous forme d'objet et
ajoute le coach. En conséquence, elle illustre aussi le mécanisme d'héritage puisque le stagiare
et le coach peuvent être généralisés en une personne.

Avec l'ajout du coach, cette version ajoute aussi la notion de classmethod pour la formation afin
de proposer un constructeur alternatif.
"""


class TraininfFullException(Exception):
    ...


class Person:
    def __init__(self, name: str, title: str):
        if len(name) < 2:
            raise ValueError("Name too short")

        self.name = name
        self.title = title

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False

        return self.name == other.name


class Student(Person):
    def __init__(self, name: str, title: str, company: str = None):
        super().__init__(name, title)
        self.company = company

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False

        return (self.name, self.company) == (other.name, other.company)


class Coach(Person):
    def __init__(self, name: str, title: str, cost: float):
        super().__init__(name, title)
        self.cost = cost


class Training:
    def __init__(self, subject: str, duration: int, capacity: int = 12):
        self.subject = subject
        self.duration = int(duration)
        self.available_seats = int(capacity)
        self._students = []
        self.coach = None

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

    def set_coach(self, coach: Coach):
        self.coach = coach

    @classmethod
    def with_coach(cls, coach, subject: str, duration: int, capacity: int = 12):
        training = cls(subject, duration, capacity)
        training.set_coach(coach)

        return training
