import context
from engine import *
                                                                                                              
class Position:
    def __init__(self, position):
        self.position = position

class Velocity:
    def __init__(self, velocity):
        self.velocity = velocity

class MoveSystem(game.System):
    def __init__(self):
        super().__init__()

    def update(self, dt):
        for ent, (pos, vel) in self.game.ecs.get_components(Position, Velocity):
            pos.position[0] += vel.velocity[0] * dt
            pos.position[1] += vel.velocity[1] * dt
            print(str(pos.position[0]) + " - " + str(pos.position[1]))

def level_1():
    print("start 'level_1':")
    game.ecs.create_entity(Position([30, 30]), Velocity([2, 1]))

game = Game()
game.settings.set_screen_size((300, 300))
game.add_level("level_1", level_1)
game.ecs.add_system(MoveSystem())
game.start()
