from delegate import find_first_char
from stack import Stack


print("=== Пункт 1: виклик делегата ===")

text = "Hello world"
symbol = "o"

index = find_first_char(text, symbol)

print(f"Символ '{symbol}' у рядку '{text}' вперше зʼявляється на позиції: {index}")



def on_stack_overflow(sender, args):
    print(
        f"[ПОДІЯ] Переповнення стеку! "
        f"Спроба вставити: {args.attempted_value}, "
        f"максимальна місткість: {args.capacity}"
    )


print("\n=== Пункт 2–3: Стек з подією ===")

stack = Stack(capacity=3)

stack.subscribe(on_stack_overflow)

# Заповнюємо стек
stack.push(10)
stack.push(20)
stack.push(30)

# Спроба переповнення
stack.push(40) 

