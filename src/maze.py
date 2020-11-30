EMPTY = 0
WALL = 1


class Maze:

    def __init__(self, width, height):
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


    def walls(self):
        """ Return all the walls which can be used for drawing the maze. """
        pass
