class Unit:
    def __init__(self):
        self._location = None

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        self._location = location

    def possible_paths(self):
        available_paths = []
        for edge in self._location.neighbors:
            if not edge.is_occupied():
                available_paths.append(edge)
        return available_paths

    def can_move(self):
        return len(self.possible_paths()) != 0
