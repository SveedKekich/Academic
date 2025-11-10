from models.student import Student
from models.musician import Musician
from models.pilot import Pilot
from app_io.file_manager import FileManager

class ConsoleMenu:
    def __init__(self):
        self.file_manager = FileManager("database.txt")
        self.people = []

    def add_student(self):
        f = input("First name: ")
        l = input("Last name: ")
        g = input("Gender: ")
        sid = input("Student ID: ")
        c = input("Course: ")
        a = input("Address: ")
        self.people.append(Student(f, l, g, sid, c, a))

    def add_musician(self):
        f = input("First name: ")
        l = input("Last name: ")
        g = input("Gender: ")
        i = input("Instrument: ")
        self.people.append(Musician(f, l, g, i))

    def add_pilot(self):
        f = input("First name: ")
        l = input("Last name: ")
        g = input("Gender: ")
        lid = input("License ID: ")
        exp = int(input("Experience years: "))
        self.people.append(Pilot(f, l, g, lid, exp))

    def save_to_file(self):
        self.file_manager.write(self.people)
        print("Data saved successfully!")

    def show_all(self):
        for p in self.people:
            print(p.info())

    def start(self):
        while True:
            print("\n1. Add Student\n2. Add Musician\n3. Add Pilot\n4. Show All\n5. Save to file\n0. Exit")
            choice = input("Select: ")
            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.add_musician()
            elif choice == "3":
                self.add_pilot()
            elif choice == "4":
                self.show_all()
            elif choice == "5":
                self.save_to_file()
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
