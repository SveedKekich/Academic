from dataclasses import dataclass
from typing import Optional, Protocol


@dataclass
class Student:
    last_name: str
    first_name: str
    course: int
    student_id: str
    gender: str  
    residence: Optional[str] = None

    def full_name(self) -> str:
     return f"{self.first_name} {self.last_name}"



    def is_in_dorm(self) -> bool:
        if not self.residence:
            return False
        parts = self.residence.split('.')
        if len(parts) != 2:
            return False
        dorm, room = parts
        return dorm.isdigit() and room.isdigit()



from typing import Protocol, runtime_checkable

@runtime_checkable
class CanSkate(Protocol):
    def skate(self) -> str:
        ...



@dataclass
class Musician(Student):
    instrument: str = "Unknown"

    def practice(self) -> str:
     return f"{self.first_name} {self.last_name} practices playing the {self.instrument}"



@dataclass
class Pilot(Student):
    flight_hours: int = 0

    def train(self, hours: int) -> None:
        if hours < 0:
            raise ValueError("Training hours cannot be negative")
        self.flight_hours += hours
    def status(self) -> str:
     return f"{self.full_name()} has {self.flight_hours} flight hours"



@dataclass
class SkatingStudent(Student, CanSkate):
    level: str = "Beginner"

    def skate(self) -> str:
     return f"{self.first_name} {self.last_name} skates at {self.level} level"

