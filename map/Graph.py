from Edge import Edge


class Graph:
    edges = []

    def __init__(self, edges: list = None):
        if edges is None:
            edges = []
        self.edges = edges

    def add_edge(self, new_edge):
        if not isinstance(new_edge, Edge):
            raise TypeError("new_edge must be an instance of Edge")
        if new_edge not in self.edges:
            self.edges.append(new_edge)
