class Sorting:
    sequence: list

    def __init__(self, sequence: list):
        self.sequence = sequence

    def bubble_sort(self, reverse_order: bool = True):
        if not self.sequence:
            raise ValueError("Array is empty")
        if reverse_order is True:
            for number in range(len(self.sequence) - 1):
                for j in range(len(self.sequence) - number - 1):
                    if self.sequence[j] > self.sequence[j + 1]:
                        self.sequence[j], self.sequence[j + 1] = self.sequence[j + 1], self.sequence[j]
        else:
            for number in range(len(self.sequence) - 1):
                for j in range(len(self.sequence) - number - 1):
                    if self.sequence[j] < self.sequence[j + 1]:
                        self.sequence[j], self.sequence[j + 1] = self.sequence[j + 1], self.sequence[j]


n = Sorting([1, 4, 6, 1, 8])
n.bubble_sort()
print(n.sequence)
