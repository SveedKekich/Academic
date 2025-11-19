import pytest
from project.models import Musician, Pilot, SkatingStudent


def test_musician_practice():
    m = Musician("Bondar", "Ira", 2, "M1", "F", None, instrument="violin")
    assert m.practice() == "Ira Bondar practices playing the violin"


def test_pilot_training():
    p = Pilot("Smith", "John", 3, "P1", "M", None, flight_hours=10)
    p.train(5)
    assert p.flight_hours == 15


def test_pilot_training_negative():
    p = Pilot("Smith", "John", 3, "P2", "M")
    with pytest.raises(ValueError):
        p.train(-1)


def test_skating_student():
    s = SkatingStudent("Ivanenko", "Olena", 1, "S1", "F", None, level="Advanced")
    assert s.skate() == "Olena Ivanenko skates at Advanced level"
