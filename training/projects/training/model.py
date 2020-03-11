"""
Module pour une représentation de formation sous forme d'objet.
"""


class Student:
    def __init__(self, name: str, company: str = None):
        """
        Describes a student

        :param name: The student name
        :param company: The student's company name
        """
        self._name = name.capitalize()
        self._company = company.capitalize() if company else None

    @property
    def name(self):
        return self._name

    @property
    def company(self):
        return self._company

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False

        return (self._name, self._company) == (other.name, other.company)


class Training:
    def __init__(self, subject: str, duration: int, available_seats: int = 12):
        """
        Describes a training

        :param subject: Subject of the training
        :param duration: Duration in days
        :param available_seats: maximum seats available for the training
        """

        duration = int(duration)
        if duration < 1:
            raise ValueError("Duration should be at least one (1) day")

        self._subject = subject
        self._duration = int(duration)
        self._students = []
        self._seats = int(available_seats)

    @property
    def subject(self):
        return self._subject

    @property
    def duration(self):
        return self._duration

    @property
    def students(self):
        return self._students.copy()

    def add_student(self, student: Student):
        if len(self.students) == self._seats:
            raise ValueError("Training full, can't add student")

        self._students.append(student)

    def remove_student(self, student: Student):
        if student not in self._students:
            raise ValueError(f"Student {student.name} not in this training")

        self._students.remove(student)

    def remove_student_by_name(self, name: str) -> Student:
        """
        Remove a student by his name. Raises ValueError if no student with this name is present or if more than one is
        present.

        :param name: The name of the student
        :return: The student with the name
        :raises ValueError: if there is no student or more than one student with this name.
        """
        students_names = [student.name for student in self._students]
        name_occurences = students_names.count(name.capitalize())

        if name_occurences > 1:
            raise ValueError(f"More than one student with name {name}")
        elif name_occurences < 0:
            raise ValueError(f"No student with name {name}")
        else:
            return self._students.pop(students_names.index(name.capitalize()))

    def remove_students_for_company(self, comany: str):
        """
        Remove all students for a given company.

        :param comany: The company name.
        :return: A list of students removed which are from the company or an empty list if there is no student from that
        company.
        """
        students = [student for student in self._students if student.company == comany.capitalize()]
        self._students = [student for student in self._students if student not in students]

        return students
