import sys, pygame
from .display import *
from .renderer import *
from .input import *
from .constants import *
from .settings import *
from .ecs import *

class Game:
    def __init__(self):
        """Game()"""
        pygame.init()
        self.settings = Settings(self)
        self.display = Display(self)
        self.input = Input(self)
        self.renderer = Renderer(self)
        self.ecs = Ecs(self)

        self._clock = pygame.time.Clock()
        self._levels = {}
        self._current_level = ""
        self._start_level = ""
        self._running = False

    def start(self):
        """start()"""
        self.display._init()
        self._eventloop()
        self._quit()

    def quit(self):
        """quit"""
        self._running = False

    def _quit(self):
        """_quit()"""
        pygame.quit()

    def _eventloop(self):
        """_eventloop()"""
        self._running = True
        self._clock.tick(self.settings.get_fps())
        self.goto_level(self._start_level)
        while self._running:
            self.input._begin_new_frame()
            self._handle_events()
            if self.input.key_down(KEY.K_ESCAPE): self._running = False
            self.display._get_screen().fill(self.settings.get_clear_color())
            self.ecs._update(self._clock.get_time() / 1000)
            pygame.display.flip()
            self._clock.tick(self.settings.get_fps())

    def _handle_events(self):
        """_handle_events()"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT: self._running = False
            elif event.type == pygame.KEYDOWN: self.input._key_down_event(event.key)
            elif event.type == pygame.KEYUP: self.input._key_up_event(event.key)
            elif event.type == pygame.MOUSEBUTTONDOWN: self.input._mouse_button_down_event(event.button)
            elif event.type == pygame.MOUSEBUTTONUP: self.input._mouse_button_up_event(event.button)
            elif event.type == pygame.VIDEORESIZE: self.settings.set_screen_size(event.size)

    def add_level(self, name, init_func):
        """add_level(name, init_func)"""
        self._levels[name] = init_func
        if self._start_level == "":
            self._start_level = name

    def goto_level(self, name):
        """goto_level(name)"""
        self.ecs.delete_all()
        func = self._levels[name]
        func()
        self._current_level = name

    def current_level(self):
        """current_level()"""
        return self._current_level
