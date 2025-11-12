from dataclasses import dataclass

@dataclass
class Student:
    last_name: str
    first_name: str
    year: int          
    id_card: str       
    sex: str           
    address: str       
    dorm: str = ""     

    def __str__(self):
        dorm_str = self.dorm if self.dorm else "не проживає в гуртожитку"
        return f"{self.last_name} {self.first_name}, курс {self.year}, {self.sex}, проживання: {dorm_str}"
