class StackOverflowEventArgs:

    def __init__(self, attempted_value, capacity):
        self.attempted_value = attempted_value
        self.capacity = capacity
