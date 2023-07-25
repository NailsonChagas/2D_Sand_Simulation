from Simulation.Utils import *
#from Simulation.Grid import Grid, Cell
from Simulation.Grid import Simulation, Cell

INDEX = (-1, -1)
RADIUS = 1

class Window:
    def __init__(self, name: str, savePath: str, load:bool = False) -> None:
        self.savePath = savePath
        self.events = Events()
        self.WINDOW = None
        self.grid = Simulation() if not load else Simulation.loadGrid(savePath)
        self.name = name

    def __openWindow(self):
        self.WINDOW = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(self.name)
    
    def __drawOptionalGrid(self):
        for i in range(ROWS + 1):
            pg.draw.line(
                self.WINDOW, COLORS["BLACK"], 
                (0, i * PX_SIZE), (WIDTH, i * PX_SIZE)
            )
        for j in range(COLS):
            pg.draw.line(
                self.WINDOW, COLORS["BLACK"], 
                (j * PX_SIZE, 0), (j * PX_SIZE, HEIGHT - TOOLBAR_HEIGHT)
            )
    
    def __drawGrid(self):
        for i, row in enumerate(self.grid.matrix):
            for j, pixel in enumerate(row):
                pg.draw.rect(
                    self.WINDOW, pixel.color if pixel is not None else COLORS["WHITE"], 
                    (
                        j * PX_SIZE, i * PX_SIZE,
                        PX_SIZE, PX_SIZE
                    )
                )

    def __drawInfo(self):
        font = getFont(30)
        text = font.render(
            f"INDEX: {INDEX}  Radius: {RADIUS} Pause:{self.grid.pause}", 
            1, COLORS["BLACK"]
        )
        self.WINDOW.blit(
            text, 
            (
                WIDTH - 700 + (WIDTH - 210)/2 - text.get_width()/2, 
                (HEIGHT - TOOLBAR_HEIGHT/2 - 25) + TOOLBAR_HEIGHT/2 - text.get_height()/2
            )
        )

    def __draw(self):
        self.WINDOW.fill(BG_COLOR)
        
        self.__drawGrid()
        self.grid.update()
        if DRAW_GRID: self.__drawOptionalGrid()
        self.__drawInfo()
        pg.display.update()
    
    def run(self):
        clock = pg.time.Clock()
        self.__openWindow()

        while self.events.handleEvents(self.grid):
            clock.tick(FPS)
            self.__draw()
        
        self.grid.saveGrid(self.savePath)
        pg.quit()

class Mouse:
    def __init__(self):
        self.r = 1
        self.selectedType = "SAND"
    def scrow(self, num:int):
        global RADIUS
        if (self.r + num) >= 1 and (self.r + num) <= 20: 
            self.r = self.r + num 
            RADIUS = self.r
    def getIndex(self, pos: tuple[int, int]):
        x, y = pos
        if y // PX_SIZE < ROWS: return (y // PX_SIZE, x // PX_SIZE)
        return (-1, -1)
    def getPos(pos: tuple[int, int]):
        x, y = pos; return (y, x)

class Events:
    def __init__(self):
        self.mouse = Mouse()

    def __handleMouse(self, grid: Simulation):
        pos = self.mouse.getIndex(pg.mouse.get_pos())
        if pg.mouse.get_pressed()[0]: #left
            grid.paintCell(pos, Cell(self.mouse.selectedType), self.mouse.r)
        if pg.mouse.get_pressed()[2]: #right
            grid.paintCell(pos, None, self.mouse.r)

    def handleEvents(self, grid: Simulation):
        global INDEX
        for event in pg.event.get():
            self.__handleMouse(grid)
            match event.type:
                case pg.QUIT: 
                    print("Event: close button")
                    return False
                case pg.MOUSEMOTION:
                    INDEX = self.mouse.getIndex(event.pos)
                case pg.MOUSEBUTTONDOWN:
                    match event.button:
                        case 4: self.mouse.scrow(1)
                        case 5: self.mouse.scrow(-1)
                case pg.KEYDOWN:
                    match event.key:
                        case pg.K_1: self.mouse.selectedType = "SAND"
                        case pg.K_2: self.mouse.selectedType = "WATER"
                        case pg.K_3: self.mouse.selectedType = "ROCK"
                        case pg.K_4: self.mouse.selectedType = "SMOKE"
                        case pg.K_r: grid.reset()
                        case pg.K_p: grid.pause = not grid.pause   
        return True