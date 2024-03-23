from map.Edge import Edge
from map.Graph import Graph
from unit.Cop import Cop
from unit.Thief import Thief


class Map:

    def __init__(self, cop1_pos=5, cop2_pos=9, cop3_pos=11, thief_pos=10):
        self._graph = None
        self._cops = [Cop() for _ in range(3)]
        self._thief = Thief()
        self.set_up_graph(cop1_pos, cop2_pos, cop3_pos, thief_pos)

    def set_up_graph(self, cop1_pos, cop2_pos, cop3_pos, thief_pos):
        edges = []
        for i in range(0, 21):
            edges.append(Edge(i))

        edges[0].add_neighbor(edges[1])
        edges[0].add_neighbor(edges[3])
        edges[0].add_neighbor(edges[4])

        edges[1].add_neighbor(edges[2])
        edges[1].add_neighbor(edges[3])
        edges[1].add_neighbor(edges[0])

        edges[2].add_neighbor(edges[6])
        edges[2].add_neighbor(edges[3])
        edges[2].add_neighbor(edges[1])

        edges[3].add_neighbor(edges[2])
        edges[3].add_neighbor(edges[5])
        edges[3].add_neighbor(edges[0])
        edges[3].add_neighbor(edges[1])

        edges[4].add_neighbor(edges[0])
        edges[4].add_neighbor(edges[8])
        edges[4].add_neighbor(edges[7])

        edges[5].add_neighbor(edges[11])
        edges[5].add_neighbor(edges[10])
        edges[5].add_neighbor(edges[9])
        edges[5].add_neighbor(edges[3])

        edges[6].add_neighbor(edges[13])
        edges[6].add_neighbor(edges[12])
        edges[6].add_neighbor(edges[2])

        edges[7].add_neighbor(edges[8])
        edges[7].add_neighbor(edges[14])
        edges[7].add_neighbor(edges[4])

        edges[8].add_neighbor(edges[9])
        edges[8].add_neighbor(edges[14])
        edges[8].add_neighbor(edges[7])
        edges[8].add_neighbor(edges[4])

        edges[9].add_neighbor(edges[5])
        edges[9].add_neighbor(edges[10])
        edges[9].add_neighbor(edges[15])
        edges[9].add_neighbor(edges[8])

        edges[10].add_neighbor(edges[11])
        edges[10].add_neighbor(edges[15])
        edges[10].add_neighbor(edges[9])
        edges[10].add_neighbor(edges[5])

        edges[11].add_neighbor(edges[12])
        edges[11].add_neighbor(edges[15])
        edges[11].add_neighbor(edges[10])
        edges[11].add_neighbor(edges[5])

        edges[12].add_neighbor(edges[6])
        edges[12].add_neighbor(edges[13])
        edges[12].add_neighbor(edges[16])
        edges[12].add_neighbor(edges[11])

        edges[13].add_neighbor(edges[16])
        edges[13].add_neighbor(edges[12])
        edges[13].add_neighbor(edges[6])

        edges[14].add_neighbor(edges[8])
        edges[14].add_neighbor(edges[18])
        edges[14].add_neighbor(edges[7])

        edges[15].add_neighbor(edges[11])
        edges[15].add_neighbor(edges[17])
        edges[15].add_neighbor(edges[9])
        edges[15].add_neighbor(edges[10])

        edges[16].add_neighbor(edges[20])
        edges[16].add_neighbor(edges[12])
        edges[16].add_neighbor(edges[13])

        edges[17].add_neighbor(edges[20])
        edges[17].add_neighbor(edges[19])
        edges[17].add_neighbor(edges[18])
        edges[17].add_neighbor(edges[15])

        edges[18].add_neighbor(edges[19])
        edges[18].add_neighbor(edges[14])
        edges[18].add_neighbor(edges[17])

        edges[19].add_neighbor(edges[20])
        edges[19].add_neighbor(edges[18])
        edges[19].add_neighbor(edges[17])

        edges[20].add_neighbor(edges[16])
        edges[20].add_neighbor(edges[19])
        edges[20].add_neighbor(edges[17])

        edges[cop1_pos].unit = self._cops[0]
        self._cops[0].location = edges[cop1_pos]
        edges[cop2_pos].unit = self._cops[1]
        self._cops[1].location = edges[cop2_pos]
        edges[cop3_pos].unit = self._cops[2]
        self._cops[2].location = edges[cop3_pos]
        edges[thief_pos].unit = self._thief
        self._thief.location = edges[thief_pos]

        self._graph = Graph(edges)

    def draw(self):
        edges = self._graph.edges

        print('            ' + str(edges[0]) + '----' + str(edges[1]) + '----' + str(edges[2]))
        print('          /   \\   |   /   \\')
        print('        /       \\ | /       \\')
        print('      /           ' + str(edges[3]) + '          \\')
        print('    /             |             \\')
        print('  /               |               \\')
        print(str(edges[4]) + '                ' + str(edges[5]) + '                ' + str(edges[6]))
        print('| \\             / | \\             / |')
        print('|   \\         /   |   \\         /   |')
        print(str(edges[7]) + '----' + str(edges[8]) + '----' + str(edges[9]) + '----' + str(edges[10]) + '----'
              + str(edges[11]) + '----' + str(edges[12]) + '----' + str(edges[13]))
        print('|   /         \\   |   /         \\   |')
        print('| /             \\ | /             \\ |')
        print(str(edges[14]) + '                ' + str(edges[15]) + '                ' + str(edges[16]))
        print('  \\               |               /')
        print('    \\             |             /')
        print('      \\           ' + str(edges[17]) + '          /')
        print('        \\       / | \\       /')
        print('          \\   /   |   \\   /')
        print('            ' + str(edges[18]) + '----' + str(edges[19]) + '----' + str(edges[20]))

    def move_unit(self, starting_edge_num: int, ending_edge_num: int):
        starting_edge = self._graph.edges[starting_edge_num]
        ending_edge = self._graph.edges[ending_edge_num]

        if not starting_edge.is_occupied:
            raise Exception("There's no unit to move on the edge " + str(starting_edge_num))

        if ending_edge.is_occupied:
            raise Exception("The edge " + str(ending_edge_num) + " is already occupied")

        ending_edge.unit = starting_edge.unit
        starting_edge.unit = None
        ending_edge.unit.location = ending_edge

    @property
    def thief(self):
        return self._thief

    @property
    def graph(self):
        return self._graph

    def cops_moves(self):
        moves = []
        thief_pos = self._thief.location.number
        for index in range(len(self._cops)):
            cops_pos = [
                self._cops[0].location.number,
                self._cops[1].location.number,
                self._cops[2].location.number
            ]
            for edge in self._cops[index].possible_paths:
                cops_pos[index] = edge.number
                moves.append(GameState(cops_pos[0], cops_pos[1], cops_pos[2], thief_pos))

        return moves

    def thief_moves(self):
        moves = []
        cops_pos = [
            self._cops[0].location.number,
            self._cops[1].location.number,
            self._cops[2].location.number
        ]
        for edge in self._thief.possible_paths:
            thief_pos = edge.number
            moves.append(GameState(cops_pos[0], cops_pos[1], cops_pos[2], thief_pos))

        return moves

    def evaluate(self):
        if not self._thief.can_move:
            return 10000

        if self._thief.escaped:
            return -10000

        score = 0
        # The cops receive a malus if they are far from the thief (-1 / edge)
        for cop in self._cops:
            score -= len(cop.path_to(self, self._thief.location)) - 1

        # The cops receive a malus for each edge the thief can move to (-10 / edge)
        score -= len(self._thief.possible_paths) * 10

        # The cops receive a bonus depending on the distance of the thief to the center (+100 / edge)
        step_to_center = len(self._thief.path_to(self, self._graph.edges[Thief.center])) - 1
        if step_to_center == 0:
            step_to_center = 10
        score += step_to_center * 100

        return score

    def set_positions(self, cop1_pos, cop2_pos, cop3_pos, thief_pos):
        edges = self._graph.edges
        for edge in edges:
            edge.unit = None

        edges[cop1_pos].unit = self._cops[0]
        self._cops[0].location = edges[cop1_pos]
        edges[cop2_pos].unit = self._cops[1]
        self._cops[1].location = edges[cop2_pos]
        edges[cop3_pos].unit = self._cops[2]
        self._cops[2].location = edges[cop3_pos]
        edges[thief_pos].unit = self._thief
        self._thief.location = edges[thief_pos]


class GameState:
    projection_map = Map()

    def __init__(self, cop1_pos, cop2_pos, cop3_pos, thief_pos):
        self._cop1_pos = cop1_pos
        self._cop2_pos = cop2_pos
        self._cop3_pos = cop3_pos
        self._thief_pos = thief_pos

    @property
    def evaluate(self):
        GameState.projection_map.set_positions(self._cop1_pos, self._cop2_pos, self._cop3_pos, self._thief_pos)
        return GameState.projection_map.evaluate()

    @property
    def thief_moves(self):
        GameState.projection_map.set_positions(self._cop1_pos, self._cop2_pos, self._cop3_pos, self._thief_pos)
        return GameState.projection_map.thief_moves()

    @property
    def cops_moves(self):
        GameState.projection_map.set_positions(self._cop1_pos, self._cop2_pos, self._cop3_pos, self._thief_pos)
        return GameState.projection_map.cops_moves()

    def to_map(self):
        return Map(self._cop1_pos, self._cop2_pos, self._cop3_pos, self._thief_pos)

    @property
    def thief_can_move(self):
        GameState.projection_map.set_positions(self._cop1_pos, self._cop2_pos, self._cop3_pos, self._thief_pos)
        return GameState.projection_map.thief.can_move

    @property
    def thief_escaped(self):
        GameState.projection_map.set_positions(self._cop1_pos, self._cop2_pos, self._cop3_pos, self._thief_pos)
        return GameState.projection_map.thief.escaped
