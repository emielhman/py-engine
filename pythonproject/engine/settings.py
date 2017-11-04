import sys, pygame

class Settings:
    def __init__(self, game):
        """Settings(game)"""
        self._game = game
        self._fps = 60
        self._screen_width = 300
        self._screen_height = 300
        self._screen_flags =  pygame.GL_DOUBLEBUFFER |  pygame.RESIZABLE
        self._screen_clear_color = (0, 0, 0)

    def get_fps(self):
        """get_fps()"""
        return self._fps

    def get_actual_fps(self):
        """get_actual_fps()"""
        return self._game._clock.get_fps()

    def get_time_since_last_frame(self):
        """get_time_since_last_frame()"""
        return self._game._clock.get_time() / 1000

    def set_fps(self, fps):
        """set_fps(fps)"""
        self._fps = fps

    def get_screen_size(self):
        """get_screen_size()"""
        return [self._screen_width, self._screen_height]

    def set_screen_size(self, size):
        """set_screen_size(size)"""
        self._screen_width = size[0]
        self._screen_height = size[1]
        self._game.display._reset_screen()

    def get_screen_width(self):
        """get_screen_width()"""
        return self._screen_width

    def set_screen_width(self, width):
        """set_screen_width(width)"""
        self._screen_width = width
        self._game.display._reset_screen()

    def get_screen_height(self):
        """get_screen_height()"""
        return self._screen_height

    def set_screen_height(self, height):
        """set_screen_height(height)"""
        self._screen_height = height
        self._game.display._reset_screen()

    def get_screen_flags(self):
        """get_screen_flags()"""
        return self._screen_flags

    def set_screen_flags(self, flags):
        """set_screen_flags(flags)"""
        self._screen_flags = flags
        self._game.display._reset_screen()

    def get_clear_color(self):
        """get_clear_color()"""
        return self._screen_clear_color

    def set_clear_color(self, color):
        """set_clear_color(color)"""
        self._screen_clear_color = color
