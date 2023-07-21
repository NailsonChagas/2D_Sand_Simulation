from Game.Utils import *
from Game.Cell import *

class Mouse:
    def __init__(self) -> None:
        self.selectedType = "SAND" # fazer um metodo de selecionar
        self.radius = 1 # 1 a 17

class Window:
    def __init__(self, name: str, savePath: str, load:bool = False) -> None:
        self.mouse = Mouse()
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

    def handleEvents(self):
        for event in pg.event.get():
            match event.type:
                case pg.QUIT: 
                    print("Event: close button")
                    self.grid.saveGrid(self.savePath)
                    return False
                case pg.MOUSEMOTION:
                    x, y = getTruePos(event.pos)
                    if y != -1 or x != -1: 
                        print("Cell: X =", x, "Y =", y)
                case pg.MOUSEBUTTONDOWN:
                    pos = getTruePos(event.pos)
                    match event.button:
                        case 1: # LEFT 
                            if pos[0] != -1 or pos[1] != -1: 
                                self.grid.changeCell(pos, Cell(self.mouse.selectedType), self.mouse.radius)
                        case 3: # RIGHT
                            if pos[0] != -1 or pos[1] != -1: 
                                self.grid.changeCell(pos, Cell("VOID"), self.mouse.radius) 
                        case 4: # scrolling up
                            self.mouse.radius += 1 if self.mouse.radius + 1 <= 17 else 0
                        case 5: # scrolling down
                            self.mouse.radius -= 1 if self.mouse.radius - 1 >= 1 else 0
        return True

    def run(self):
        running = True
        clock = pg.time.Clock()
        self.__openWindow()

        while running:
            clock.tick(FPS)
            running = self.handleEvents()
            self.draw()
            
        print("Quiting pygame")
        pg.quit()