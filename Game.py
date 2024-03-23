from math import inf
from map.Map import Map, GameState
import pygame as pg


class Game:

    def __init__(self):
        self._map = Map()
        self.SCREEN_WIDTH = 640
        self.SCREEN_HEIGHT = 480

        # Initialise pygame
        pg.init()

        self._window = pg.display.set_mode([self.SCREEN_WIDTH, self.SCREEN_HEIGHT])
        # Set the window name
        pg.display.set_caption('Cops and thief')

    def start(self):
        # Main loop, run until window closed
        running = True
        while running:

            # Check events
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

            # Clear the window
            self._window.fill((0, 0, 0))

            self._map.draw(self._window, self.SCREEN_WIDTH, self.SCREEN_HEIGHT)

            # Update the display
            pg.display.update()

        # close pygame
        pg.quit()

        # TODO: Delete this old code
        # game_stopped = False
        # thief_escaped = False
        # thief_can_move = True
        #
        # while not game_stopped and not thief_escaped and thief_can_move:
        #     print()
        #     self._map.draw()
        #     print()
        #     game_stopped = self.ask_user_action()
        #     thief_escaped = self._map.thief.escaped
        #     if game_stopped or thief_escaped:
        #         break
        #     self.move_cops()
        #     thief_can_move = self._map.thief.can_move
        #
        # print()
        # self._map.draw()
        # print()
        #
        # if game_stopped:
        #     print("\nAu revoir !\n")
        # elif thief_escaped:
        #     print("\nLe voleur s'est échappé !")
        # else:
        #     print("\nLe voleur a été capturé !\n")

    def get_available_options(self):
        options = ['Q']
        for edges in self._map.thief.possible_paths:
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

    def move_cops(self):
        correct_move = self._map
        correct_move_score = -inf
        for move in self._map.cops_moves():
            score = self.minimax(move, 4, False)
            if score > correct_move_score:
                correct_move = move
                correct_move_score = score
        self._map = correct_move.to_map()

    def minimax(self, map_state: GameState, depth, should_maximize):
        if depth == 0 or not map_state.thief_can_move or map_state.thief_escaped:
            score = map_state.evaluate
            if should_maximize:
                score -= depth
            else:
                score += depth
            return score

        if should_maximize:
            value = -inf
            for move in map_state.cops_moves:
                value = max(value, self.minimax(move, depth - 1, False))
            return value
        else:
            value = inf
            for move in map_state.thief_moves:
                value = min(value, self.minimax(move, depth - 1, True))
            return value
