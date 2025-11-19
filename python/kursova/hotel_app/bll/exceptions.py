class DomainError(Exception):
    """Базовий виняток предметної області."""
    pass


class ValidationError(DomainError):
    """Помилка валідації даних, які ввів користувач."""
    pass


class NotFoundError(DomainError):
    """Сутність з таким ID не знайдена."""
    pass


class BookingError(DomainError):
    """Помилка при створенні бронювання (перетин дат, відсутній номер тощо)."""
    pass
