from map.Edge import Edge


class Graph:
    def __init__(self, edges: list = None):
        self._edges = edges if edges is not None else []

    @property
    def edges(self):
        return self._edges

    @edges.setter
    def edges(self, edges):
        if not all(isinstance(edge, Edge) for edge in edges):
            raise TypeError("All edges must be instances of Edge")
        self._edges = edges

    def add_edge(self, new_edge):
        if not isinstance(new_edge, Edge):
            raise TypeError("new_edge must be an instance of Edge")
        if new_edge not in self._edges:
            self._edges.append(new_edge)
