from .person import Person

class Pilot(Person):
    def __init__(self, first_name, last_name, gender, license_id, experience_years, address=""):
        super().__init__(first_name, last_name, gender, address)
        self.license_id = license_id
        self.experience_years = experience_years

    def drive(self):
        print(f"{self.first_name} {self.last_name} is flying a plane with license {self.license_id}.")

    def info(self):
        return (f"Pilot: {self.first_name} {self.last_name}, License: {self.license_id}, "
                f"Experience: {self.experience_years} years, Gender: {self.gender}")
