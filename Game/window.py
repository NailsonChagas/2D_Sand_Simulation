from Game.Utils import *
from Game.Cell import *

class Window:
    def __init__(self, name) -> None:
        self.WINDOW = None
        self.name = name
        self.grid = Grid(ROWS, COLS)

    def __openWindow(self):
        self.WINDOW = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(self.name)

    def draw(self):
        self.WINDOW.fill(BG_COLOR)
        pg.display.update()

    def run(self):
        running = True
        clock = pg.time.Clock()
        self.__openWindow()

        while running:
            clock.tick(FPS)
            for event in pg.event.get():
                match event.type:
                    case pg.QUIT: 
                        print("Event: close button")
                        running = False
            self.draw()
        print("Quiting pygame")
        pg.quit()