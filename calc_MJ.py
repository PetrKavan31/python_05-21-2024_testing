class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def maximum(self, a, b):
        return max(a, b)

    def minimum(self, a, b):
        return min(a, b)

    def percentage(self, a, b):
        return (a * b) / 100

    def power(self, a, b):
        return a ** b