from .settings import *
import pygame as pg
pg.init() 
pg.font.init()

def get_font(size):
    return pg.font.SysFont("comicsans", size)

def getTruePos(pos: tuple[int, int]):
    x, y = pos
    cellX = x // PX_SIZE if (y // PX_SIZE) < ROWS else -1 # -1 é nulo -> coluna
    cellY = y // PX_SIZE if (y // PX_SIZE) < ROWS else -1 # -1 é nulo -> linha
    return (cellY, cellX)