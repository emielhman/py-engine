import sys, pygame

class Input:
    def __init__(self, game):
        """Input(game)"""
        self._game = game
        self._down_keys = {}
        self._up_keys = {}
        self._held_keys = {}
        self._down_buttons = [False] * 5
        self._up_buttons = self._down_buttons
        self._held_buttons = self._down_buttons
        pygame.key.set_repeat(1, 1)

    def _begin_new_frame(self):
        """_begin_new_frame()"""
        self._up_keys = self._up_keys.fromkeys(self._up_keys, False)
        self._down_keys = self._down_keys.fromkeys(self._up_keys, False)
        self._down_buttons = [False] * 5
        self._up_buttons = [False] * 5

    def _key_down_event(self, key):
        """_key_down_event(key)"""
        self._down_keys[key] = True
        self._held_keys[key] = True

    def _key_up_event(self, key):
        """_key_up_event(key)"""
        self._up_keys[key] = True
        self._held_keys[key] = False

    def _mouse_button_down_event(self, button):
        """_mouse_button_down_event(button)"""
        self._down_buttons[button-1] = True
        self._held_buttons[button-1] = True

    def _mouse_button_up_event(self, button):
        """_mouse_button_up_event(button)"""
        self._up_buttons[button-1] = True
        self._held_buttons[button-1] = False

    def key_down(self, key):
        """key_down(key)"""
        if key in self._down_keys:
            return self._down_keys[key]
        return False

    def key_up(self, key):
        """key_up(key)"""
        if key in self._up_keys:
            return self._up_keys[key]
        return False

    def key_held(self, key):
        """key_held(key)"""
        if key in self._held_keys:
            return self._held_keys[key]
        return False

    def button_down(self, button):
        """button_down(button)"""
        return self._down_buttons[button]

    def button_up(self, button):
        """button_up(button)"""
        return self._up_buttons[button]

    def button_held(self, button):
        """button_held(button)"""
        return self._held_buttons[button]

    def get_mouse_pos(self):
        """get_mouse_pos()"""
        return pygame.mouse.get_pos()

    def get_mouse_rel_pos(self):
        """get_mouse_rel_pos()"""
        return pygame.mouse.get_rel()

    def set_mouse_pos(self, pos):
        """set_mouse_pos(pos)"""
        pygame.mouse.set_pos(pos)
