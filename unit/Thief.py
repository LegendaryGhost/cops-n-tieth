from unit.Unit import Unit


class Thief(Unit):
    def __str__(self):
        return 'T '

    def escaped(self):
        return self.location.number == 10
