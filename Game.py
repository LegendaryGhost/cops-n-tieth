from map.Map import Map


class Game:

    def __init__(self):
        self._map = Map()

    def start(self):
        game_stopped = False
        thief_escaped = False
        thief_can_move = True

        while not game_stopped and not thief_escaped and thief_can_move:
            print()
            self._map.draw()
            print()
            game_stopped = self.ask_user_action()
            thief_escaped = self._map.thief.escaped()
            thief_can_move = self._map.thief.can_move()

        print()
        self._map.draw()
        print()

        if game_stopped:
            print("\nAu revoir !\n")
        elif thief_escaped:
            print("\nLe voleur s'est échappé !")
        else:
            print("\nLe voleur a été capturé !\n")

    def get_available_options(self):
        options = ['Q']
        for edges in self._map.thief.possible_paths():
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
