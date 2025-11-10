import re

def validate_student_id(student_id: str) -> bool:
    return bool(re.match(r"^[A-Z]{2}\d{6}$", student_id))

def validate_name(name: str) -> bool:
    return bool(re.match(r"^[A-Za-zА-Яа-яІіЇїЄє]+$", name))
