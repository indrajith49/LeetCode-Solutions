class MinStack:

    def __init__(self):

        self.stack = []
        self.min_stack = []

    def push(self, value: int) -> None:

        self.stack.append(value)
        if not self.min_stack:  # If empty
            self.min_stack.append(value)
        else:
            # Take the SMALLER of: (new value, current minimum)
            current_min = self.min_stack[-1]
            if value < current_min:
                self.min_stack.append(value)  # New value is smaller
            else:
                self.min_stack.append(current_min)

    def pop(self) -> None:

        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:

        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

