from wall import Wall
from vector import add, mul


EMPTY = 0
WALL = 1


class Maze:

    def __init__(self, width, height):
        assert width > 0 and height > 0
        self.grid = [[WALL if x % 2 == 0 or y % 2 == 0 else EMPTY
            for x in range(2*width +1)] for y in range(2*height +1)]


    def __str__(self):
        builder = ''
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x] == EMPTY:
                    builder += ' '
                else:  # maze[y][x] == WALL
                    if y % 2 == 0:
                        if x % 2 == 0:
                            builder += '+'
                        else:
                            builder += '-'
                    else:
                        builder += '|'
                builder += ' '
            if y < len(self.grid) - 1:
                builder += '\n'
        return builder


    def __repr__(self):
        return self.__str__()


    def cells(self):
        """ Return all the cell coordinates on the grid. """
        cells = []
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if not (x % 2 == 0 or y % 2 == 0):
                    cells.append((x, y))
        return cells


    def walls(self, width, height):
        """ Return all the walls which can be used for drawing the maze. """
        maze_width, maze_height = len(self.grid[0]), len(self.grid)

        scalex, scaley = width / maze_width, height / maze_height
        scale = min(scalex, scaley)

        centerx = (width -  scale * (maze_width  - 1)) / 2
        centery = (height - scale * (maze_height - 1)) / 2
        center = (centerx, centery)

        walls = []

        # Draw all the horizontal going walls.
        for y in range(maze_height):
            lines = ''.join(map(str, self.grid[y])).split(str(EMPTY))
            offset = 0
            for line in lines:
                if len(line) > 1:
                    start = add(center, mul((offset, y), scale))
                    end = add(center, mul(((offset + len(line)-1), y), scale))
                    walls.append(Wall(start, end))
                    offset += len(line) + 1
                else:
                    offset += 2

        # Draw all the vertical going walls.
        grid_transposed = [list(x) for x in zip(*self.grid)]
        for x in range(maze_width):
            lines = ''.join(map(str, grid_transposed[x])).split(str(EMPTY))
            offset = 0
            for line in lines:
                if len(line) > 1:
                    start = add(center, mul((x, offset), scale))
                    end = add(center, mul((x, (offset + len(line)-1)), scale))
                    walls.append(Wall(start, end))
                    offset += len(line) + 1
                else:
                    offset += 2

        return walls
