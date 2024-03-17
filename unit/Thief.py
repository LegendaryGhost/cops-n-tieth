from unit.Unit import Unit


class Thief(Unit):
    center: int = 10

    def __str__(self):
        return 'T '

    @property
    def escaped(self):
        return self.location.number == Thief.center
