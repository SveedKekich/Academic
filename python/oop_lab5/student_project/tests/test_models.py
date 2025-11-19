import pytest
from project.models import Student, SkatingStudent


# =============================
# Testing Student methods
# =============================

def test_is_in_dorm_none():
    s = Student("A", "B", 1, "1", "F", residence=None)
    assert s.is_in_dorm() is False

def test_is_in_dorm_wrong_format():
    s = Student("A", "B", 1, "1", "F", residence="invalid")
    assert s.is_in_dorm() is False

def test_is_in_dorm_true():
    s = Student("A", "B", 1, "1", "F", residence="2.205")
    assert s.is_in_dorm() is True

def test_full_name_order():
    s = Student("Bondar", "Ira", 1, "1", "F")
    assert s.full_name() == "Ira Bondar"

def test_pilot_status():
    from project.models import Pilot

    p = Pilot("Bondar", "Ira", 2, "P1", "F", flight_hours=10)
    assert p.status() == "Ira Bondar has 10 flight hours"


# =============================
# SkatingStudent
# =============================

def test_skating_student():
    s = SkatingStudent("Ivanenko", "Olena", 1, "S1", "F", level="Advanced")
    assert s.skate() == "Olena Ivanenko skates at Advanced level"

def test_skating_student_default_level():
    s = SkatingStudent("Petrenko", "Oleg", 2, "S2", "M")
    assert s.skate() == "Oleg Petrenko skates at Beginner level"
