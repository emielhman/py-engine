import sys, pygame

class Renderer:
    def __init__(self, game):
        """Renderer(game)"""
        self._game = game

    # Draws a circle with a radius and color at a position.
    # If width = 0 the circle will be filled.
    # Example: draw_circle( (255, 0.5, 0.5), (50, 50), 40)
    def draw_circle(self, color, pos, radius, width = 0):
        """draw_circle(color, pos, radius, width = 0))"""
        pygame.draw.circle(self._game.display._get_screen(), color, [int(x) for x in pos], radius, width)

    # Draws a rectangle with width
    # The Rect(x,y,w,h) is drawn from the topleft-corner.
    # Example: draw_rect( (0, 255, 0), (75, 75, 150, 150), 3)
    def draw_rect(self, color, rect, width = 0):
        """draw_rect(color, rect, width = 0)"""
        pygame.draw.rect(self._game.display._get_screen(), color, [int(x) for x in rect], width)

    # Draws a line from start_pos to end_pos with width
    # Example: draw_line( (0, 0, 255), [0, 0], [300, 300], 5)
    def draw_line(self, color, start_pos, end_pos, width = 1):
        """draw_line(color, start_pos, end_pos, width = 1)"""
        pygame.draw.line(self._game.display._get_screen(), color, [int(x) for x in start_pos], [int(x) for x in end_pos], width)

    # Draws a set of lines from point to point with width.
    # If closed is true a final line will also be drawn between the first and last point.
    # Example: draw_lines( (255, 0, 255), True, [ [0, 0], [300, 300], [0, 300]], 10)
    def draw_lines(self, color, closed, points, width = 1):
        """draw_lines(color, closed, points, width = 1)"""
        pygame.draw.lines(self._game.display._get_screen(), color, closed, [[int(x) for x in point] for point in points], width)
