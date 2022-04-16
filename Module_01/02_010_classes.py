class Human:
    def __init__(self, head: int, arm: int, leg: int) -> None:
        self.head = head
        self.arm = arm
        self.leg = leg


person = Human(1, 2, 2)

print(person.arm)
print(person.leg)
print(person.head)
