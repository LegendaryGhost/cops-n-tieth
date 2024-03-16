from map.Edge import Edge
from map.Graph import Graph
from unit.Cop import Cop
from unit.Thief import Thief


class Map:

    def __init__(self):
        self._graph = None
        self._cops = [Cop() for i in range(3)]
        self._thief = Thief()
        self.set_up_graph()

    def set_up_graph(self):
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

        edges[5].unit = self._cops[0]
        self._cops[0].location = edges[5]
        edges[9].unit = self._cops[1]
        self._cops[1].location = edges[9]
        edges[11].unit = self._cops[2]
        self._cops[2].location = edges[11]
        edges[10].unit = self._thief
        self._thief.location = edges[10]

        self._graph = Graph(edges)

    def draw(self):
        edges = self._graph.edges

        print('            ' + str(edges[0]) + '----' + str(edges[2]) + '----' + str(edges[3]))
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

        if not starting_edge.is_occupied():
            raise Exception("There's no unit to move on the edge " + str(starting_edge_num))

        if ending_edge.is_occupied():
            raise Exception("The edge " + str(ending_edge_num) + " is already occupied")

        ending_edge.unit = starting_edge.unit
        starting_edge.unit = None
        ending_edge.unit.location = ending_edge

    @property
    def thief(self):
        return self._thief
