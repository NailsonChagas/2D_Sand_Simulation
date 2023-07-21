from Game.Utils import *
from Game.Cell import *
from Game.button import Button

buttonY = HEIGHT - TOOLBAR_HEIGHT/2 - 25
widgetY = HEIGHT - TOOLBAR_HEIGHT

class Mouse:
    def __init__(self) -> None:
        self.selectedType = "BLOCK" # fazer um metodo de selecionar
        self.radius = 1 # 1 a 20

class Window:
    def __init__(self, name: str, savePath: str, load:bool = False) -> None:
        self.mouse = Mouse()
        self.WINDOW = None
        self.name = name
        self.grid = Grid.loadGrid(savePath) if load else Grid(ROWS, COLS, "VOID")
        self.posText = "Cell: (-1, -1)"
        self.buttons = [
            Button(
                (10, buttonY), (50,50), "BLACK"
            ),
            Button(
                (70, buttonY), (50,50), "CYAN"
            ),
            Button(
                (130, buttonY), (50,50), "YELLOW"
            ),
            Button(
                (190, buttonY), (50,50), "BROWN"
            ),
            Button(
                (250, buttonY), (50,50), "RED"
            ),
            Button(
                (310, buttonY), (50,50), "GRAY"
            ),
            Button(
                (370, buttonY), (50,50), "GREEN"
            )
        ]
        self.savePath = savePath

    def __openWindow(self):
        self.WINDOW = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(self.name)

    def __drawGrid(self):
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

    def __draw(self):
        widget = Button((WIDTH - 210, buttonY), (200,50), "WHITE", 
            f"Pos: {self.posText}  Radius: {self.mouse.radius}", t=18
        )
        self.WINDOW.fill(BG_COLOR)
        self.__drawGrid()
        widget.draw(self.WINDOW)
        for b in self.buttons: b.draw(self.WINDOW)
        pg.display.update()

    def __handleMouse(self):
        pos = getTruePos(pg.mouse.get_pos())
        if pos[0] == -1 or pos[1] == -1:
            if pg.mouse.get_pressed()[0]: #left
                for b in self.buttons:
                    if not b.clicked(getPos(pg.mouse.get_pos())): continue
                    match b.color:
                        case "YELLOW": self.mouse.selectedType = "SAND"
                        case "BLACK": self.mouse.selectedType = "BLOCK"
                        case "CYAN": self.mouse.selectedType = "WATER"
                        case "GREEN": self.mouse.selectedType = "ACID"
                        case "GRAY": self.mouse.selectedType = "GAS"
                        case "BROWN": self.mouse.selectedType = "WOOD"
                        case "RED": self.mouse.selectedType = "FIRE"
        else:
            if pg.mouse.get_pressed()[0]: #left
                self.grid.changeCell(pos, Cell(self.mouse.selectedType), self.mouse.radius)
            if pg.mouse.get_pressed()[2]: #right
                self.grid.changeCell(pos, Cell("VOID"), self.mouse.radius)

    def __handleEvents(self):
        for event in pg.event.get():
            self.__handleMouse()
            match event.type:
                case pg.QUIT: 
                    print("Event: close button"); self.grid.saveGrid(self.savePath)
                    return False
                case pg.MOUSEMOTION:
                    y, x = getTruePos(event.pos)
                    self.posText = f"Cell: ({x}, {y})"
                case pg.MOUSEBUTTONDOWN:
                    match event.button:
                        case 4: self.mouse.radius += 1 if self.mouse.radius + 1 <= 20 else 0 # scrolling up
                        case 5: self.mouse.radius -= 1 if self.mouse.radius - 1 >= 1 else 0 # scrolling down
        return True

    def run(self):
        clock = pg.time.Clock()
        self.__openWindow()

        while self.__handleEvents():
            clock.tick(FPS)
            self.__draw()

        print("Quiting pygame")
        pg.quit()