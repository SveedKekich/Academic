
def find_first_char_delegate(func):
    return func


find_first_char = find_first_char_delegate(
    lambda text, ch: text.find(ch)
)
