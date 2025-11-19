from datetime import datetime
from ..bll.exceptions import DomainError
from ..dal.hotel_repository import HotelRepository
from ..dal.client_repository import ClientRepository
from ..dal.request_repository import BookingRequestRepository
from ..dal.reservation_repository import ReservationRepository
from ..bll.hotel_service import HotelService
from ..bll.client_service import ClientService
from ..bll.booking_service import BookingService
from ..bll.search_service import SearchService



def read_int(prompt: str) -> int:
    while True:
        s = input(prompt)
        try:
            return int(s)
        except ValueError:
            print("Помилка: введіть ціле число.")


def read_float(prompt: str) -> float:
    while True:
        s = input(prompt)
        try:
            return float(s)
        except ValueError:
            print("Помилка: введіть число.")


def read_date(prompt: str):
    while True:
        s = input(prompt + " (формат РРРР-ММ-ДД): ")
        try:
            return datetime.strptime(s, "%Y-%m-%d").date()
        except ValueError:
            print("Помилка: неправильний формат дати.")


def normalize_id(raw: str) -> str:
    """
    Дозволяє копіювати ID у вигляді 'id=...' з консолі:
    normalize_id("id=1234") -> "1234"
    """
    raw = raw.strip()
    if raw.startswith("id="):
        raw = raw[3:]
    return raw.strip()


def main_menu():
    print("\n=== ГОЛОВНЕ МЕНЮ ===")
    print("1. Управління готелями")
    print("2. Управління клієнтами")
    print("3. Управління замовленнями")
    print("4. Пошук")
    print("0. Вихід")


def run():
    hotel_repo = HotelRepository()
    client_repo = ClientRepository()
    request_repo = BookingRequestRepository()
    reservation_repo = ReservationRepository()

    hotel_service = HotelService(hotel_repo, request_repo)
    client_service = ClientService(client_repo)
    booking_service = BookingService(hotel_repo, client_repo, reservation_repo)
    search_service = SearchService(hotel_repo, client_repo)

    while True:
        main_menu()
        choice = input("Ваш вибір: ").strip()
        try:
            if choice == "1":
                handle_hotels(hotel_service)
            elif choice == "2":
                handle_clients(client_service)
            elif choice == "3":
                handle_bookings(hotel_service, booking_service)
            elif choice == "4":
                handle_search(search_service)
            elif choice == "0":
                print("До побачення!")
                break
            else:
                print("Невірний вибір меню.")
        except DomainError as ex:
            print(f"ПОМИЛКА: {ex}")
        except Exception as ex:
            print(f"НЕОЧІКУВАНА ПОМИЛКА: {ex}")


def handle_hotels(hotel_service: HotelService):
    print("\n--- Управління готелями ---")
    print("1. Додати готель")
    print("2. Переглянути всі готелі")
    print("3. Переглянути один готель")
    print("4. Додати номер до готелю")
    print("5. Додати заявку на номер")
    print("6. Видалити готель")
    print("7. Змінити текст заявки")
    print("0. Назад")

    choice = input("Ваш вибір: ").strip()

    if choice == "1":
        name = input("Назва готелю: ")
        desc = input("Опис: ")
        hotel = hotel_service.add_hotel(name, desc)
        print(f"Додано готель. ID: {hotel.id}")

    elif choice == "2":
        hotels = hotel_service.get_all_hotels()
        if not hotels:
            print("Готелів поки що немає.")
        for h in hotels:
            total_capacity = sum(r.capacity for r in h.rooms)
            print(f"[{h.id}] {h.name} – {h.description}, кімнат: {len(h.rooms)}, місць: {total_capacity}")

    elif choice == "3":
        hotel_id = normalize_id(input("ID готелю: "))
        hotel = hotel_service.get_hotel(hotel_id)
        print(f"\nГотель: {hotel.name}")
        print(f"ID: {hotel.id}")
        print(f"Опис: {hotel.description}")
        if not hotel.rooms:
            print("Номерів поки що немає.")
        else:
            print("\nНомери:")
            for r in hotel.rooms:
                print(
                    f"- ID: {r.id}, номер: {r.number}, "
                    f"місць: {r.capacity}, ціна за день: {r.price_per_day}"
                )

    elif choice == "4":
        hotel_id = normalize_id(input("ID готелю: "))
        number = input("Номер кімнати (наприклад 101): ")
        capacity = read_int("Кількість місць: ")
        price = read_float("Ціна за день: ")
        room = hotel_service.add_room(hotel_id, number, capacity, price)
        print(f"Додано номер. ID: {room.id}")

    elif choice == "5":
        hotel_id = normalize_id(input("ID готелю: "))
        room_id = normalize_id(input("ID номера: "))
        text = input("Текст заявки: ")
        start = read_date("Дата заїзду")
        end = read_date("Дата виїзду")
        req = hotel_service.add_request(hotel_id, room_id, text, start, end)
        print(f"Додано заявку. ID: {req.id}")

    elif choice == "6":
        hotel_id = normalize_id(input("ID готелю для видалення: "))
        hotel_service.delete_hotel(hotel_id)
        print("Готель видалено.")

    elif choice == "7":
        request_id = normalize_id(input("ID заявки: "))
        new_text = input("Новий текст заявки: ")
        updated = hotel_service.update_request_text(request_id, new_text)
        print("Текст заявки оновлено.")
        print(f"Новий текст: {updated.text}")

    elif choice == "0":
        return

    else:
        print("Невірний вибір меню.")


def handle_clients(client_service: ClientService):
    print("\n--- Управління клієнтами ---")
    print("1. Додати клієнта")
    print("2. Переглянути всіх клієнтів")
    print("3. Переглянути конкретного клієнта")
    print("4. Змінити дані про клієнта")
    print("5. Видалити клієнта")
    print("6. Сортувати по імені")
    print("7. Сортувати по прізвищу")
    print("0. Назад")

    choice = input("Ваш вибір: ").strip()

    if choice == "1":
        fn = input("Ім'я: ")
        ln = input("Прізвище: ")
        phone = input("Телефон: ")
        email = input("Email: ")
        c = client_service.create_client(fn, ln, phone, email)
        print(f"Клієнт доданий. ID: {c.id}")

    elif choice == "2":
        clients = client_service.get_all_clients()
        if not clients:
            print("Клієнтів поки що немає.")
        for c in clients:
            print(f"[{c.id}] {c.last_name} {c.first_name}, {c.phone}, {c.email}")

    elif choice == "3":
        client_id = normalize_id(input("ID клієнта: "))
        c = client_service.get_client(client_id)
        print(f"\nКлієнт:")
        print(f"ID: {c.id}")
        print(f"Ім'я: {c.first_name}")
        print(f"Прізвище: {c.last_name}")
        print(f"Телефон: {c.phone}")
        print(f"Email: {c.email}")
    elif choice == "4":
        client_id = normalize_id(input("ID клієнта для зміни: "))
        c = client_service.get_client(client_id)
        print("Залиште порожнім поле, якщо не хочете змінювати значення.")
        new_fn = input(f"Нове ім'я ({c.first_name}): ").strip()
        new_ln = input(f"Нове прізвище ({c.last_name}): ").strip()
        new_phone = input(f"Новий телефон ({c.phone}): ").strip()
        new_email = input(f"Новий email ({c.email}): ").strip()

        if new_fn:
            c.first_name = new_fn
        if new_ln:
            c.last_name = new_ln
        if new_phone:
            c.phone = new_phone
        if new_email:
            c.email = new_email

        client_service.update_client(c)
        print("Дані клієнта оновлено.")

    elif choice == "5":
        client_id = normalize_id(input("ID клієнта для видалення: "))
        client_service.delete_client(client_id)
        print("Клієнта видалено.")

    elif choice == "6":
        clients = client_service.sort_by_first_name()
        for c in clients:
            print(f"{c.first_name} {c.last_name} (ID: {c.id})")

    elif choice == "7":
        clients = client_service.sort_by_last_name()
        for c in clients:
            print(f"{c.last_name} {c.first_name} (ID: {c.id})")

    elif choice == "0":
        return

    else:
        print("Невірний вибір меню.")


def handle_bookings(hotel_service: HotelService, booking_service: BookingService):
    print("\n--- Управління замовленнями ---")
    print("1. Створити замовлення")
    print("2. Відмінити замовлення")
    print("3. Переглянути конкретне замовлення")
    print("4. Подивитись заброньовані місця в готелі на дату")
    print("5. Подивитись вільні місця в готелі на дату")
    print("6. Подивитись вартість замовлення (по днях)")
    print("7. Подивитись клієнтів, які забронювали номери в готелі")
    print("0. Назад")

    choice = input("Ваш вибір: ").strip()

    if choice == "1":
        client_id = normalize_id(input("ID клієнта: "))
        hotel_id = normalize_id(input("ID готелю: "))
        room_id = normalize_id(input("ID номера: "))
        start = read_date("Дата заїзду")
        end = read_date("Дата виїзду")
        res = booking_service.create_reservation(client_id, hotel_id, room_id, start, end)
        print("\nБронювання створено.")
        print(f"ID: {res.id}")
        print(f"Готель ID: {res.hotel_id}")
        print(f"Номер ID: {res.room_id}")
        print(f"Клієнт ID: {res.client_id}")
        print(f"Період: {res.start_date} - {res.end_date}")
        print(f"Загальна ціна: {res.total_price}")

    elif choice == "2":
        res_id = normalize_id(input("ID бронювання: "))
        booking_service.cancel_reservation(res_id)
        print("Бронювання скасовано.")

    elif choice == "3":
        res_id = normalize_id(input("ID бронювання: "))
        res = booking_service.get_reservation(res_id)
        print("\nДані бронювання:")
        print(f"ID: {res.id}")
        print(f"Готель ID: {res.hotel_id}")
        print(f"Номер ID: {res.room_id}")
        print(f"Клієнт ID: {res.client_id}")
        print(f"Період: {res.start_date} - {res.end_date}")
        print(f"Вартість: {res.total_price}")
        print(f"Скасовано: {'так' if res.is_cancelled else 'ні'}")

    elif choice == "4":
        hotel_id = normalize_id(input("ID готелю: "))
        on_date = read_date("Дата")
        rooms = booking_service.get_booked_rooms(hotel_id, on_date)
        if not rooms:
            print("Немає заброньованих місць на цю дату.")
        else:
            total_places = sum(r.capacity for r in rooms)
            print(f"\nЗаброньовані місця на {on_date}: {total_places}")
            print("Номери:")
            for r in rooms:
                print(f"Номер {r.number} (ID: {r.id}), місць: {r.capacity}")

    elif choice == "5":
        hotel_id = normalize_id(input("ID готелю: "))
        on_date = read_date("Дата")
        rooms = booking_service.get_free_rooms(hotel_id, on_date)
        if not rooms:
            print("Немає вільних місць на цю дату.")
        else:
            total_places = sum(r.capacity for r in rooms)
            print(f"\nВільні місця на {on_date}: {total_places}")
            print("Номери:")
            for r in rooms:
                print(f"Номер {r.number} (ID: {r.id}), місць: {r.capacity}")

    elif choice == "6":
        res_id = normalize_id(input("ID бронювання: "))
        days, price_per_day, total = booking_service.get_reservation_price_details(res_id)
        print("\nДані про вартість послуг:")
        print(f"Кількість діб: {days}")
        print(f"Вартість за одну добу: {price_per_day}")
        print(f"Загальна вартість: {total}")

    elif choice == "7":
        hotel_id = normalize_id(input("ID готелю: "))
        clients = booking_service.get_clients_with_reservations(hotel_id)
        if not clients:
            print("Немає клієнтів з активними бронюваннями в цьому готелі.")
        else:
            print("Клієнти з бронюваннями в цьому готелі:")
            for c in clients:
                print(f"[{c.id}] {c.last_name} {c.first_name}, {c.phone}, {c.email}")

    elif choice == "0":
        return

    else:
        print("Невірний вибір меню.")


def handle_search(search_service: SearchService):
    print("\n--- Пошук ---")
    print("1. Пошук готелів")
    print("2. Пошук клієнтів")
    print("0. Назад")

    choice = input("Ваш вибір: ").strip()

    if choice == "1":
        keyword = input("Ключове слово: ")
        hotels = search_service.search_hotels(keyword)
        if not hotels:
            print("Нічого не знайдено.")
        else:
            for h in hotels:
                print(f"[{h.id}] {h.name} – {h.description}")

    elif choice == "2":
        keyword = input("Ключове слово: ")
        clients = search_service.search_clients(keyword)
        if not clients:
            print("Нічого не знайдено.")
        else:
            for c in clients:
                print(f"[{c.id}] {c.last_name} {c.first_name}, {c.phone}, {c.email}")

    elif choice == "0":
        return

    else:
        print("Невірний вибір меню.")
