from typing import List, Type
from .models import (
    Student, Musician, Pilot, CanSkate
)


class StudentService:
    def __init__(self, dal):
        self.dal = dal

    def get_all_students(self) -> List[Student]:
        return self.dal.load_students()

    def count_first_course_girls_in_dorm(self) -> int:
        students = self.dal.load_students()
        return sum(
            1 for s in students
            if s.gender == "F" and s.course == 1 and s.is_in_dorm()
        )

    def settle_by_gender(self, student: Student, dorm: int, room: int):
        if student.gender not in ("M", "F"):
            raise ValueError("Invalid gender")

        student.residence = f"{dorm}.{room}"

        students = self.dal.load_students()
        for i, s in enumerate(students):
            if s.student_id == student.student_id:
                students[i] = student
                break
        else:
            students.append(student)

        self.dal.save_students(students)

    def get_musicians(self) -> List[Musician]:
        return [
            s for s in self.dal.load_students()
            if isinstance(s, Musician)
        ]

    def get_pilots(self) -> List[Pilot]:
        return [
            s for s in self.dal.load_students()
            if isinstance(s, Pilot)
        ]

    def train_pilot(self, pilot_id: str, hours: int):
        students = self.dal.load_students()
        for s in students:
            if isinstance(s, Pilot) and s.student_id == pilot_id:
                s.train(hours)
                self.dal.save_students(students)
                return
        raise ValueError("Pilot not found")

    def get_skaters(self) -> List[CanSkate]:
        return [
            s for s in self.dal.load_students()
            if isinstance(s, CanSkate)
        ]
