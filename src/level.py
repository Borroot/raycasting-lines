import random

from maze import Maze, EMPTY


"""
Generate a maze using depth-first search recursive backtracking.

The algorithm is implemented as follows:
    1. Make the initial cell the current cell and mark it as visited
    2. While there are unvisited cells
        1. If the current cell has any neighbours which have not been visited
            1. Choose randomly one of the unvisited neighbours
            2. Push the current cell to the stack
            3. Remove the wall between the current cell and the chosen cell
            4. Make the chosen cell the current cell and mark it as visited
        2. Else if the visited stack is not empty
            1. Pop a cell from the visited stack
            2. Make it the current cell
"""


def neighbours_unvisited(maze, current, unvisited):
    neighbours = []
    for offset in [(-2, 0), (0, -2), (2, 0), (0, 2)]:
        neighbour = (current[0] + offset[0], current[1] + offset[1])
        if neighbour in unvisited:
            neighbours.append(neighbour)
    return neighbours


def remove_wall(maze, cell1, cell2):
    maze.grid[(cell1[1] + cell2[1]) // 2][(cell1[0] + cell2[0]) // 2] = EMPTY


def generate(width, height):
    maze = Maze(width, height)
    visited = []
    unvisited = set(maze.cells())

    current = unvisited.pop()
    visited.append(current)

    while len(unvisited) > 0:
        if len(neighbours:=neighbours_unvisited(maze, current, unvisited)) > 0:
            neighbour = random.choice(neighbours)
            remove_wall(maze, current, neighbour)

            current = neighbour
            unvisited.remove(current)
            visited.append(current)
        elif len(visited) > 0:
            current = visited.pop()

    return maze
