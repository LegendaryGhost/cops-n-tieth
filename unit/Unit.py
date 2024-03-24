from queue import Queue
import pygame as pg


class Unit:
    color = (255, 0, 0)
    radius = 10

    def __init__(self):
        self._location = None

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        self._location = location

    @property
    def possible_paths(self):
        available_paths = []
        for edge in self._location.neighbors:
            if not edge.is_occupied:
                available_paths.append(edge)
        return available_paths

    @property
    def can_move(self):
        return len(self.possible_paths) != 0

    def path_to(self, game_map, target_edge):
        # Mark the edges unvisited
        for edge in game_map.graph.edges:
            edge.visited = False
            edge.previous = None

        # BFS algorithm
        queue = Queue()
        self.location.visited = True
        queue.put(self.location)
        while not queue.empty():
            current_edge = queue.get()
            for neighbor in current_edge.neighbors:
                if not neighbor.visited and (not neighbor.is_occupied or neighbor == target_edge):
                    neighbor.visited = True
                    neighbor.previous = current_edge
                    queue.put(neighbor)
                    if neighbor == target_edge:
                        queue.empty()
                        break

        path = []
        current_edge = target_edge
        while current_edge is not None:
            path.append(current_edge.number)
            current_edge = current_edge.previous

        return path

    def draw(self, window):
        pg.draw.circle(window, Unit.color, self._location.coordinate, Unit.radius)
