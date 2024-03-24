from unit.Unit import Unit
import pygame as pg


class Thief(Unit):
    center: int = 10
    color = (0, 0, 255)

    def __str__(self):
        return 'V '

    @property
    def escaped(self):
        return self.location.number == Thief.center

    def draw(self, window):
        pg.draw.circle(window, Thief.color, self._location.coordinate, Unit.radius)
