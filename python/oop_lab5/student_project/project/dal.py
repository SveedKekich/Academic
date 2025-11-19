from typing import List
import csv
from .models import Student


class FileDAL:

    def __init__(self, csv_path: str):
        self.csv_path = csv_path

    def load_students(self) -> List[Student]:
        students = []
        with open(self.csv_path, newline='', encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                students.append(
                    Student(
                        last_name=row["last_name"],
                        first_name=row["first_name"],
                        course=int(row["course"]),
                        student_id=row["student_id"],
                        gender=row["gender"],
                        residence=row.get("residence")
                    )
                )
        return students

    def save_students(self, students: List[Student]):
        with open(self.csv_path, "w", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["last_name", "first_name", "course", "student_id", "gender", "residence"])
            for st in students:
                writer.writerow([
                    st.last_name,
                    st.first_name,
                    st.course,
                    st.student_id,
                    st.gender,
                    st.residence
                ])
