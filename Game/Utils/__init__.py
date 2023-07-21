from .settings import *
import pygame as pg
pg.init() 
pg.font.init()


def getTruePos(pos: tuple[int, int]):
    x, y = pos
    cellX = x // PX_SIZE if (y // PX_SIZE) < ROWS else -1 # -1 é nulo
    cellY = y // PX_SIZE if (y // PX_SIZE) < ROWS else -1 # -1 é nulo
    return (cellY, cellX)