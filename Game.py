from math import inf
from map.Map import Map, GameState
import pygame as pg


class Game:

    def __init__(self):
        self.SCREEN_WIDTH = 640
        self.SCREEN_HEIGHT = 480
        self._map = Map(screen_width=self.SCREEN_WIDTH, screen_height=self.SCREEN_HEIGHT)

        # Initialise pygame
        pg.init()

        self._window = pg.display.set_mode([self.SCREEN_WIDTH, self.SCREEN_HEIGHT])
        # Set the window name
        pg.display.set_caption('Cops and thief')

    def start(self):
        # Main loop, run until window closed
        running = True
        thief_moved = False
        # Define the font and size
        font = pg.font.Font(None, 60)

        # Render the thief victory text
        thief_victory_text = font.render("Le voleur s'est échappé!", True, (0, 255, 0))
        thief_victory_text_rect = thief_victory_text.get_rect(center=(self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 2))
        # Get the size of the text surface
        thief_text_width, thief_text_height = thief_victory_text.get_size()
        # Define the position of the rectangle (centered in this example)
        thief_rect_x = (self.SCREEN_WIDTH - thief_text_width) // 2
        thief_rect_y = (self.SCREEN_HEIGHT - thief_text_height) // 2

        # Render the cops victory text
        cops_victory_text = font.render("Le voleur a été capturé!", True, (255, 0, 0))
        cops_victory_text_rect = cops_victory_text.get_rect(center=(self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 2))
        # Get the size of the text surface
        cops_text_width, cops_text_height = cops_victory_text.get_size()
        # Define the position of the rectangle (centered in this example)
        cops_rect_x = (self.SCREEN_WIDTH - cops_text_width) // 2
        cops_rect_y = (self.SCREEN_HEIGHT - cops_text_height) // 2

        while running:

            # Check events
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.MOUSEBUTTONDOWN and not (self.game_over() and thief_moved):
                    mouse_pos = pg.mouse.get_pos()
                    for edge in self._map.thief.possible_paths:
                        if edge.clicked_inside(mouse_pos):
                            thief_moved = True
                            self._map.move_unit(self._map.thief.location.number, edge.number)
                            self.move_cops()

            # Clear the window
            self._window.fill((0, 0, 0))

            self._map.draw(self._window)

            # Draw the game over text on the screen
            if thief_moved and self.game_over():
                if self._map.thief.escaped:
                    pg.draw.rect(
                        self._window,
                        (255, 255, 255),
                        (thief_rect_x, thief_rect_y, thief_text_width, thief_text_height)
                    )
                    self._window.blit(thief_victory_text, thief_victory_text_rect)
                else:
                    pg.draw.rect(
                        self._window,
                        (255, 255, 255),
                        (cops_rect_x, cops_rect_y, cops_text_width, cops_text_height)
                    )
                    self._window.blit(cops_victory_text, cops_victory_text_rect)

            # Update the display
            pg.display.update()

        # close pygame
        pg.quit()

    def game_over(self):
        return self._map.thief.escaped or not self._map.thief.can_move

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
