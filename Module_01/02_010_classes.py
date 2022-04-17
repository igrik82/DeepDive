class Human:
    def __init__(self, head: int, arm: int, leg: int) -> None:
        self.head = head
        self.arm = arm
        self.leg = leg

    def count(self):
        return self.arm + self.head + self.leg

    def __str__(self):
        return "Head - {0}, arm - {1}, leg - {2}"\
            .format(self.head, self.arm, self.leg)

    def __repr__(self) -> str:
        return "Head - {0}, arm - {1}, leg - {2}"\
            .format(self.head, self.arm, self.leg)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Human):
            return self.arm == other.arm and self.head == other.head and\
                     self.leg == other.leg
        else:
            return False


person1 = Human(1, 2, 2)
person2 = Human(1, 2, 2)

# print variable
print(person1.arm)
print(person1.leg)
print(person1.head)

# print method
print(person1.count())

# print string representation through str method
print(str(person1))

# print class string representation
print(person1)

# compare two classes through eq method
print(person1 == person2)
print(person1 == 100)
