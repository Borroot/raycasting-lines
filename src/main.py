import threading

from world import World
from constants import *
from draw import draw_loop
from tick import tick_loop


def main():
    state = {'alive': True, 'world': World(SIZE_PART)}

    thread_draw = threading.Thread(target=draw_loop, args=(state, ))
    thread_tick = threading.Thread(target=tick_loop, args=(state, ))

    thread_draw.start()
    thread_tick.start()

    thread_draw.join()
    thread_tick.join()


if __name__ == '__main__':
    main()
