from Game.Utils import COLORS, ROWS, COLS
import json

class Cell:
    def __init__(self, type: str):
        self.type = None
        self.gravity = None
        self.color = None
        self.colision = None
        self.density = None
        self.acelerationXY = [0,0]
        self.velocityXY = [0,0]

        match type:
            case "WOOD":
                self.type = "WOOD"
                self.gravity = False
                self.color = COLORS["BROWN"]
                self.colision = True
                self.density = 3
            case "SAND":
                self.type = "SAND"
                self.gravity = True
                self.color = COLORS["YELLOW"]
                self.colision = True
                self.density = 3
            case "WATER":
                self.type = "WATER"
                self.gravity = True
                self.color = COLORS["CYAN"]
                self.colision = True
                self.density = 2
            case "ACID":
                self.type = "ACID"
                self.gravity = True
                self.color = COLORS["GREEN"]
                self.colision = True
                self.density = 1
            case "GAS":
                self.type = "GAS"
                self.gravity = True
                self.color = COLORS["GRAY"]
                self.colision = True
                self.density = 0
            case "FIRE":
                self.type = "FIRE"
                self.gravity = False
                self.color = COLORS["RED"]
                self.colision = False
                self.density = 0
            case "BLOCK":
                self.type = "BLOCK"
                self.gravity = False
                self.color = COLORS["BLACK"]
                self.colision = True
                self.density = -1 # não deve se mover por difereça de densidade
            case "VOID":
                self.type = "VOID"
                self.gravity = None
                self.color = COLORS["WHITE"]
                self.colision = None
                self.density = None

    def toDict(self):
        return {
            "type": self.type,
            "acelerationXY": self.acelerationXY,
            "velocityXY": self.velocityXY
        }
    
    @staticmethod
    def loadCell(type:str, aceleration:list[int], velocity:list[int]):
        aux = Cell(type)
        aux.acelerationXY = aceleration
        aux.velocityXY = velocity
        return aux

class Grid:
    def __init__(self, rows:int, cols:int, t:str="VOID"):
        self.grid = [
            [Cell(t) for _ in range(cols)] for _ in range(rows)
        ]

    def changeCell(self, cellPosition: tuple[int, int], cell: Cell, radius:int = 1):
        row, col = cellPosition
        if radius == 1:
            self.grid[row][col] = cell
            return 
        rad = radius - 1
        for r in range(row - rad, row + rad + 1):
            for c in range(col - rad, col + rad + 1):
                if 0 <= r < ROWS and 0 <= c < COLS:
                    distance = ((r - row) ** 2 + (c - col) ** 2) ** 0.5
                    if distance <= rad:
                        self.grid[r][c] = cell
    
    def swapCellsPosition(self, cellPosition1:tuple[int,int], cellPosition2:tuple[int,int]):
        row1, col1 = cellPosition1
        row2, col2 = cellPosition2
        temp_cell = self.grid[row1][col1]
        self.grid[row1][col1] = self.grid[row2][col2]
        self.grid[row2][col2] = temp_cell

    def saveGrid(self, path: str):
        print("Saving state")
        grid_data = [[cell.toDict() for cell in row] for row in self.grid]
        with open(path, 'w') as json_file:
            json.dump(grid_data, json_file, indent=4)
    
    def getNeighbors(self, pos:tuple[int,int]):
        """
        return: [
            0 1 2
            3 X 4
            5 6 7
        ]
        """
        i, j = pos
        neighbors = []
        indices = [ # Define os índices dos vizinhos em torno da célula (i, j)
            (i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
            (i, j - 1),                 (i, j + 1),
            (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)
        ]
        for (row, col) in indices:
            if 0 <= row < ROWS and 0 <= col < COLS: 
                neighbors.append({"row": row, "col":col, "Cell":self.grid[row][col]})
            else:
                neighbors.append({"row": row, "col":col, "Cell":None})
        return neighbors 

    def update(self): # To DO: atualizar grid
        pass
    
    @staticmethod
    def loadGrid(path: str):
        print("Loading state")
        grid = Grid(ROWS, COLS)

        with open(path, "r") as data:
            gridJson = json.load(data)
        
        for i, row in enumerate(gridJson):
            for j, c in enumerate(row):
                grid.changeCell((i,j), Cell.loadCell(c["type"], c["acelerationXY"], c["velocityXY"]))
        return grid