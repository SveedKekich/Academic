import os
from project.dal import FileDAL
from project.models import Student


def test_dal_save_and_load(tmp_path):
    csv_file = tmp_path / "students.csv"
    dal = FileDAL(str(csv_file))

    students = [
        Student("Test", "User", 1, "ID1", "F", "1.101")
    ]

    dal.save_students(students)
    loaded = dal.load_students()

    assert len(loaded) == 1
    assert loaded[0].student_id == "ID1"
