import pytest
from project.bll import StudentService
from project.models import Student, Musician, Pilot, SkatingStudent


class MockDAL:
    def __init__(self, students):
        self.students = students
        self.saved_students = None

    def load_students(self):
        return self.students

    def save_students(self, students):
        self.saved_students = students



def test_get_all_students():
    dal = MockDAL([Student("A", "B", 1, "1", "F")])
    service = StudentService(dal)
    result = service.get_all_students()
    assert len(result) == 1
    assert result[0].student_id == "1"


def test_count_first_course_girls_in_dorm():
    students = [
        Student("A", "B", 1, "1", "F", residence="1.101"),
        Student("C", "D", 1, "2", "F", residence=None),
        Student("E", "F", 2, "3", "F", residence="1.102")
    ]
    dal = MockDAL(students)
    service = StudentService(dal)
    assert service.count_first_course_girls_in_dorm() == 1


def test_count_first_course_girls_in_dorm_empty():
    dal = MockDAL([])
    service = StudentService(dal)
    assert service.count_first_course_girls_in_dorm() == 0


def test_settle_by_gender_updates_existing():
    st = Student("I", "J", 1, "S1", "M")
    dal = MockDAL([st])
    service = StudentService(dal)
    service.settle_by_gender(st, 3, 200)
    assert dal.saved_students[0].residence == "3.200"


def test_settle_by_gender_invalid_gender():
    st = Student("I", "J", 1, "S1", "X") 
    dal = MockDAL([])
    service = StudentService(dal)
    with pytest.raises(ValueError):
        service.settle_by_gender(st, 1, 1)

def test_settle_by_gender_appends_new_student():
    from project.models import Student
    from project.bll import StudentService

    new_student = Student("Bondar", "Ira", 1, "S1", "F")
    
    dal = MockDAL([])
    service = StudentService(dal)
    
    service.settle_by_gender(new_student, dorm=2, room=101)
    
    assert dal.saved_students is not None
    assert len(dal.saved_students) == 1
    assert dal.saved_students[0] == new_student
    assert dal.saved_students[0].residence == "2.101"



def test_get_musicians():
    dal = MockDAL([
        Musician("A", "B", 1, "1", "F", instrument="piano"),
        Student("C", "D", 2, "2", "M")
    ])
    service = StudentService(dal)
    result = service.get_musicians()
    assert len(result) == 1
    assert isinstance(result[0], Musician)
    assert result[0].instrument == "piano"

def test_get_musicians_empty():
    dal = MockDAL([Student("A", "B", 1, "1", "F")])
    service = StudentService(dal)
    result = service.get_musicians()
    assert result == []



def test_get_pilots():
    dal = MockDAL([
        Pilot("A", "B", 1, "1", "M", flight_hours=10),
        Student("C", "D", 1, "2", "F")
    ])
    service = StudentService(dal)
    result = service.get_pilots()
    assert len(result) == 1
    assert result[0].flight_hours == 10


def test_train_pilot_success():
    pilot = Pilot("A", "B", 1, "P1", "M", flight_hours=5)
    dal = MockDAL([pilot])
    service = StudentService(dal)
    service.train_pilot("P1", 3)
    assert dal.saved_students[0].flight_hours == 8


def test_train_pilot_not_found():
    dal = MockDAL([Pilot("A", "B", 1, "P10", "M", flight_hours=5)])
    service = StudentService(dal)
    with pytest.raises(ValueError):
        service.train_pilot("XXX", 2)



def test_get_skaters():
    dal = MockDAL([
        SkatingStudent("A", "B", 1, "1", "F", level="Advanced"),
        Student("C", "D", 1, "2", "M")
    ])
    service = StudentService(dal)
    result = service.get_skaters()
    assert len(result) == 1
    assert isinstance(result[0], SkatingStudent)
    assert result[0].level == "Advanced"
