from .bll import StudentService
from .dal import FileDAL
from .models import Student

def main():
    dal = FileDAL("students.csv")
    service = StudentService(dal)

    print("1 - Count 1st-year girls in dorms")
    print("2 - Settle student into a room")

    choice = input("Choose: ")

    if choice == "1":
        print("Count:", service.count_first_course_girls_in_dorm())

    elif choice == "2":
        sid = input("Student ID: ")
        dorm = int(input("Dorm number: "))
        room = int(input("Room: "))

        students = dal.load_students()

        student = next((s for s in students if s.student_id == sid), None)
        if not student:
            print("Student not found")
            return

        service.settle_by_gender(student, dorm, room)
        print("Done.")

if __name__ == "__main__":
    main()
