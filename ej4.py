class Numeros:
    def __init__(self, n):
        self.n = n
    def __iter__(self):
        self.i = 0
        return self
    def __next__(self):
        if self.i < self.n:
            self.i += 1
            return self.i
        else:
            raise StopIteration