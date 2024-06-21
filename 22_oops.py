class room:
    # constructor
    def __init__(self, l, w):
        self.length = l  # instance variables
        self.width = w  # instance variables

    def show(self):
        print("Length = ", self.length)
        print("Width = ", self.width)

    def area(self):
        return self.length * self.width


r = room(12, 31)
r.show()
print(r.area())

r1 = room(4, 5)
print(r1.area())
r1.show()


class square:
    def __init__(self, s) -> None:
        self.side = s

    def show(self):
        print(self.side)

    def area(self):
        return self.side**2


s = square(12)
s.show()
print(s.area())
