class IntegerSet:
    def __init__(self, elements):
        self.elements = set(elements)

    def sum(self):
        return sum(self.elements)

    def mean(self):
        return sum(self.elements) / len(self.elements)

    def max(self):
        return max(self.elements)

    def min(self):
        return min(self.elements)

def main():
    int_set = IntegerSet([1, 2, 3, 4, 5])
    print(int_set.sum())
    print(int_set.mean())
    print(int_set.max())
    print(int_set.min())

if __name__ == "__main__":
    main()




