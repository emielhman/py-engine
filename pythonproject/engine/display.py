import sys, pygame

class Display:
    def __init__(self, game):
        """Display(game)"""
        self._game = game
        self._screen = None

    def _init(self):
        """_init()"""
        self._screen =  pygame.display.set_mode(self._game.settings.get_screen_size(), self._game.settings.get_screen_flags())

    def _get_screen(self):
        """_get_screen()"""
        return self._screen

    def _reset_screen(self):
        """_reset_screen()"""
        if self._screen != None:
            self._screen =  pygame.display.set_mode(self._game.settings.get_screen_size(), self._game.settings.get_screen_flags())
