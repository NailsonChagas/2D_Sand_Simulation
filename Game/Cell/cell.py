from Game.Utils import COLORS

class Cell:
    def __init__(self, type: str):
        self.type = None
        self.gravity = None
        self.color = None
        self.colision = None
        self.density = None

        match type:
            case "SAND":
                self.type = "SAND"
                self.gravity = 3
                self.color = COLORS["YELLOW"]
                self.colision = True
                self.density = 2
            case "WATER":
                self.type = "WATER"
                self.gravity = 3
                self.color = COLORS["CYAN"]
                self.colision = True
                self.density = 1
            case "GAS":
                self.type = "GAS"
                self.gravity = -3
                self.color = COLORS["GRAY"]
                self.colision = True
                self.density = 0
            case "BLOCK":
                self.type = "BLOCK"
                self.gravity = 0
                self.color = COLORS["BLACK"]
                self.colision = True
                self.density = -1 # não deve se mover por difereça de densidade
            case "VOID":
                self.type = "VOID"
                self.gravity = None
                self.color = COLORS["WHITE"]
                self.colision = None
                self.density = None

class Grid:
    def __init__(self, rows:int, cols:int):
        self.grid = [
            [Cell("VOID") for _ in range(cols)] for _ in range(rows)
        ]
    
    def changeCell(self, cellPosition: tuple[int, int], cell: Cell):
        row, col = cellPosition
        self.grid[row][col] = cell
    
    def swapCellsPosition(self, cellPosition1:tuple[int,int], cellPosition2:tuple[int,int]):
        row1, col1 = cellPosition1
        row2, col2 = cellPosition2
        temp_cell = self.grid[row1][col1]
        self.grid[row1][col1] = self.grid[row2][col2]
        self.grid[row2][col2] = temp_cell
