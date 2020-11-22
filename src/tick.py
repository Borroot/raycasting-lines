import pygame

from constants import *
from world import World


def update_move(state):
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        state['world'].update(move=MOVE_NORTH)
    if pressed[pygame.K_d]:
        state['world'].update(move=MOVE_EAST)
    if pressed[pygame.K_a]:
        state['world'].update(move=MOVE_WEST)
    if pressed[pygame.K_s]:
        state['world'].update(move=MOVE_SOUTH)

    if pressed[pygame.K_j]:
        state['world'].update(turn=TURN_WEST)
    if pressed[pygame.K_k]:
        state['world'].update(turn=TURN_EAST)


def update_state(state):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state['alive'] = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                state['world'] = World(SIZE_PART)
            if event.key == pygame.K_q:
                state['alive'] = False


def tick_loop(state):
    clock = pygame.time.Clock()
    while state['alive']:
        clock.tick(UPS)
        update_move(state)
        update_state(state)
