
class Training:
    def __init__(self, name, duration, seats=12):
        self.subject = name
        self.seats = seats
        self.duration = duration
        self.students = []

    def add_students(self, student_name):
        self.students.append(student_name)

    def display_students(self):
        print(self.students)

t = Training("python", 5)
t.add_students("toto")
t.display_students()
print(t.subject)