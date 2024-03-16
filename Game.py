from map.Map import Map


class Game:

    def __init__(self):
        self._map = Map()

    def start(self):
        should_stop = False
        while not should_stop:
            print()
            self._map.draw()
            print()
            should_stop = self.ask_user_action()

    def get_available_options(self):
        options = ['Q']
        thief_location = self._map.thief.location
        for edges in thief_location.neighbors:
            if not edges.is_occupied():
                options.append(str(edges.number))
        return options

    def ask_user_action(self):
        options = self.get_available_options()
        print('Saisissez "Q" pour quitter')
        print('Ou choisissez un numéro de case pour vous déplacer.')
        print('Voici les cases où vous pouvez vous déplacer :')
        print('\t' + ', '.join(options[1:]))
        choice = input("Votre choix :")

        while choice not in options:
            print("\nL'option que vous avez choisie n'est pas disponible\n")
            print('Saisissez "Q" pour quitter')
            print('Ou choisissez un numéro de case pour vous déplacer.')
            print('Voici les cases où vous pouvez vous déplacer :')
            print('\t' + ', '.join(options[1:]))
            choice = input("Votre choix :")

        if choice == 'Q':
            return True

        starting_edge_num = self._map.thief.location.number
        ending_edge_num = int(choice)
        self._map.move_unit(starting_edge_num, ending_edge_num)
        return False
