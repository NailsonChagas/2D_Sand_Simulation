from Game.Utils import *
from Game.Cell import *

class Window:
    def __init__(self, name: str, savePath: str, load:bool = False) -> None:
        self.WINDOW = None
        self.name = name
        self.grid = Grid.loadGrid(savePath) if load else Grid(ROWS, COLS, "VOID")
        self.savePath = savePath

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
        if DRAW_GRID:
            for i in range(ROWS):
                pg.draw.line(
                    self.WINDOW, COLORS["BLACK"], 
                    (0, i * PX_SIZE), (WIDTH, i * PX_SIZE)
                )
            for j in range(COLS):
                pg.draw.line(
                    self.WINDOW, COLORS["BLACK"], 
                    (j * PX_SIZE, 0), (j * PX_SIZE, HEIGHT - TOOLBAR_HEIGHT)
                )

    def draw(self):
        self.drawGrid()
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
                        self.grid.saveGrid(self.savePath)
                        running = False
            self.draw()
        print("Quiting pygame")
        pg.quit()