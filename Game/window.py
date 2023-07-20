from Game.Utils import *
from Game.Cell import *

class Window:
    def __init__(self, name) -> None:
        self.WINDOW = None
        self.name = name
        self.grid = Grid(ROWS, COLS, "WATER")

    def __openWindow(self):
        self.WINDOW = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(self.name)

    def drawGrid(self):
        for i, row in enumerate(self.grid.grid):
            for j, pixel in enumerate(row):
                pg.draw.rect(
                    self.WINDOW, pixel.color, 
                    (
                        j * PX_SIZE, i * PX_SIZE,
                        PX_SIZE, PX_SIZE
                    )
                )
        pg.display.update()

    def draw(self):
        pass

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
            self.drawGrid()
        print("Quiting pygame")
        pg.quit()