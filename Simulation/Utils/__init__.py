from .settings import *
import pygame as pg
import json
pg.init() 
pg.font.init()

def getFont(size):
    return pg.font.SysFont("comicsans", size)