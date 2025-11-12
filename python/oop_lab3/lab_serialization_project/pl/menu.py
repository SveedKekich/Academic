from bll.entity_service import EntityService
from dal.entity_context import EntityContext
from dal.providers import PickleProvider, JSONProvider, XMLProvider, CustomProvider
from models.product import Product
from models.student import Student


class Menu:
    @staticmethod
    def select_provider():
        print("\nОберіть тип серіалізації:")
        print("1 — Бінарна (Pickle)")
        print("2 — JSON")
        print("3 — XML")
        print("4 — Користувацька (Custom TXT)")
        choice = input("Ваш вибір: ")

        if choice == "1":
            return PickleProvider(), ".dat"
        elif choice == "2":
            return JSONProvider(), ".json"
        elif choice == "3":
            return XMLProvider(), ".xml"
        elif choice == "4":
            return CustomProvider(), ".txt"
        else:
            print("Невірний вибір, використано Pickle за замовчуванням.")
            return PickleProvider(), ".dat"

    @staticmethod
    def main_menu():
        print("=== Демонстрація серіалізації (Python) ===")
        print("\nОберіть сутність:")
        print("1 — Товари (Product)")
        print("2 — Студенти (Student)")
        choice = input("Ваш вибір: ")

        if choice == "1":
            Menu.run_products()
        elif choice == "2":
            Menu.run_students()
        else:
            print("Невірний вибір. Завершення роботи.")

    @staticmethod
    def run_products():
        provider, ext = Menu.select_provider()
        filename = "products" + ext
        context = EntityContext(provider, filename)
        service = EntityService(context)

        products = [
            Product(1, "Молоко", "Ферма", 25.5, 10),
            Product(2, "Хліб", "Пекарня", 15.0, 20),
            Product(3, "Сир", "Молокозавод", 120.0, 5),
            Product(4, "Масло", "Ферма", 75.0, 8),
            Product(5, "Йогурт", "Молокозавод", 28.0, 12),
        ]

        print(f"\nСеріалізація товарів у файл: {filename}")
        service.save_all(products)
        print("Об’єкти збережено успішно!")

        print("\nДесеріалізація даних...")
        loaded = service.load_all(Product)
        print("Об’єкти відновлено з файлу:")
        for p in loaded:
            print(" ", p)
        print("\nРоботу з товарами завершено.\n")

    @staticmethod
    def run_students():
        provider, ext = Menu.select_provider()
        filename = "students" + ext
        context = EntityContext(provider, filename)
        service = EntityService(context)

        students = [
            Student("Іваненко", "Марія", 1, "ST001", "Ж", "м. Київ", "1.204"),
            Student("Петренко", "Олег", 2, "ST002", "Ч", "м. Львів"),
            Student("Сидорова", "Анастасія", 1, "ST003", "Ж", "гуртожиток 2.105", "2.105"),
            Student("Гончар", "Ірина", 1, "ST004", "Ж", "гуртожиток 1.305", "1.305"),
            Student("Бондар", "Дмитро", 3, "ST005", "Ч", "м. Харків"),
        ]

        print(f"\n▶ Серіалізація студентів у файл: {filename}")
        service.save_all(students)
        print("Дані студентів збережено!")

        print("\n▶ Десеріалізація студентів...")
        loaded = service.load_all(Student)
        print("Відновлені студенти:")
        for s in loaded:
            print(" ", s)

        girls_in_dorm = [
            s for s in loaded if s.sex == "Ж" and s.year == 1 and s.dorm
        ]
        print("\nРезультат обчислення:")
        print(f"Кількість студенток 1-го курсу, які живуть у гуртожитку: {len(girls_in_dorm)}")

        if girls_in_dorm:
            print("Їхні дані:")
            for s in girls_in_dorm:
                print(" ", s)

        print("\nРоботу зі студентами завершено.\n")
