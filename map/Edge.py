class Edge:
    number = None
    neighbors = []

    def __init__(self, number: number, neighbors: list = None):
        if neighbors is None:
            neighbors = []
        self.number = number
        self.neighbors = neighbors

    def add_neighbor(self, neighbor):
        if not isinstance(neighbor, Edge):
            raise TypeError("neighbor must be an instance of Edge")
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)

    def set_neighbors(self, neighbors: list):
        self.neighbors = neighbors
