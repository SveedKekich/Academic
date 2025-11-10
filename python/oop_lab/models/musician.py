from .person import Person

class Musician(Person):
    def __init__(self, first_name, last_name, gender, instrument, address=""):
        super().__init__(first_name, last_name, gender, address)
        self.instrument = instrument

    def play(self):
        print(f"{self.first_name} {self.last_name} plays {self.instrument}.")

    def info(self):
        return (f"Musician: {self.first_name} {self.last_name}, "
                f"Instrument: {self.instrument}, Gender: {self.gender}")
