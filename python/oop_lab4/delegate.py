# delegate.py

# "Делегат": будь-яка функція з підписом (str, char) -> int або None
def find_first_char_delegate(func):
    """Приймає функцію-делегат і повертає її."""
    return func


# Лямбда-вираз згідно варіанту:
# "Визначення номера першого заданого символу в рядку"
find_first_char = find_first_char_delegate(
    lambda text, ch: text.find(ch)
)
