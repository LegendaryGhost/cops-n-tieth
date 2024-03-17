from unit.Unit import Unit


class Edge:
    def __init__(self, number: int, neighbors: list = None):
        if neighbors is None:
            neighbors = []
        self._number = number
        self._neighbors = neighbors
        self._unit = None
        self._visited = False
        self._previous = None

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number: int):
        self._number = number

    @property
    def neighbors(self):
        return self._neighbors

    @neighbors.setter
    def neighbors(self, neighbors: list):
        if not all(isinstance(neighbor, Edge) for neighbor in neighbors):
            raise TypeError("All neighbors must be instances of Edge")
        self._neighbors = neighbors

    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, unit: Unit = None):
        self._unit = unit

    @property
    def visited(self):
        return self._visited

    @visited.setter
    def visited(self, visited):
        self._visited = visited

    @property
    def previous(self):
        return self._previous

    @previous.setter
    def previous(self, previous):
        self._previous = previous

    def add_neighbor(self, neighbor):
        if not isinstance(neighbor, Edge):
            raise TypeError("neighbor must be an instance of Edge")
        if neighbor not in self._neighbors:
            self._neighbors.append(neighbor)

    @property
    def is_occupied(self):
        return self._unit is not None

    def __str__(self):
        if self.is_occupied:
            return str(self._unit)
        return str(self._number).zfill(2)
