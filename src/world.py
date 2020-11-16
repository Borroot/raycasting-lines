from player import Player


class World:

    def __init__(self, player=None, lines=[]):
        self.player = player if player is not None else Player((400, 400))
        self.lines = lines


    def draw(self, surface):
        self.player.draw(surface)
        for line in self.lines:
            line.draw(surface)
