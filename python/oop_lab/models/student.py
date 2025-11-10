from .person import Person

class Student(Person):
    def __init__(self, first_name, last_name, gender, student_id, course, address=""):
        super().__init__(first_name, last_name, gender, address)
        self.student_id = student_id
        self.course = course

    def study(self):
        print(f"{self.first_name} {self.last_name} is studying on course {self.course}.")

    def info(self):
        return (f"Student: {self.first_name} {self.last_name}, ID: {self.student_id}, "
                f"Course: {self.course}, Gender: {self.gender}, Address: {self.address}")
