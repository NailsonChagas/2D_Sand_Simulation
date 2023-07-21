from Game.Utils import *

class Button:
    def __init__(self, pos:tuple[int,int], res:tuple[int,int], color:str, text:str=None, textColor:str="BLACK", t:int=22):
        self.pos = pos # (X, Y)
        self.res = res # width height
        self.color = color
        self.text = text
        self.textColor = COLORS[textColor]
        self.t = t

    def draw(self, window:pg.Surface):
        pg.draw.rect(
            window, COLORS[self.color], 
            (
                self.pos[0], self.pos[1],
                self.res[0], self.res[1]
            )
        )
        pg.draw.rect(
            window, COLORS["BLACK"], 
            (
                self.pos[0], self.pos[1],
                self.res[0], self.res[1]
            ), 2
        )
        if self.text:
            font = get_font(self.t)
            text = font.render(self.text, 1, self.textColor)
            window.blit(
                text, 
                (
                    self.pos[0] + self.res[0]/2 - text.get_width()/2, 
                    self.pos[1] + self.res[1]/2 - text.get_height()/2
                )
            )

    def clicked(self, mousePos:tuple[int,int]):
        x, y = mousePos
        if not (x >= self.pos[1] and x <= self.pos[1] + self.res[1]):
            return False
        if not (y >= self.pos[0] and y <= self.pos[0] + self.res[0]):
            return False
        return True