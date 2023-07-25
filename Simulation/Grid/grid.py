import random
from Simulation.Grid.cell import Cell
from Simulation.Utils import ROWS, COLS, json

class Grid:
    def __init__(self):
        self.matrix = [
            [None for _ in range(COLS)] for _ in range(ROWS)
        ]
    
    def reset(self): self.matrix = [[None for _ in range(COLS)] for _ in range(ROWS)]

    def paintCell(self, cellPosition: tuple[int, int], cell: Cell, radius: int = 1):
        row, col = cellPosition
        if radius == 1:
            self.matrix[row][col] = cell
            return
        for r in range(max(0, row - radius), min(ROWS, row + radius + 1)):
            for c in range(max(0, col - radius), min(COLS, col + radius + 1)):
                if ((r - row) ** 2 + (c - col) ** 2) <= radius**2:
                    self.matrix[r][c] = cell

    def swapCellsPosition(self, cellPosition1: tuple[int, int], cellPosition2: tuple[int, int]):
        (row1, col1), (row2, col2) = cellPosition1, cellPosition2
        if row1 >= ROWS or row2 >= ROWS: return #colisão baixo
        if col1 >= COLS or col2 >= COLS: return #colisão direita
        if col1 < 0 or col2 < 0: return #colisão esquerda
        self.matrix[row1][col1], self.matrix[row2][col2] = self.matrix[row2][col2], self.matrix[row1][col1]

    def saveGrid(self, path: str):
        grid_data = [
            [cell.name if cell is not None else "None" for cell in row] for row in self.matrix
        ]
        with open(path, 'w') as json_file: json.dump(grid_data, json_file, indent=4)

    def getNeighbors(self, pos: tuple[int, int]):
        i, j = pos
        neighbors = [{"pos": None, "cell": None} for _ in range(8)]
        # Define as posições dos vizinhos em torno da célula (i, j).
        for idx, (row, col) in enumerate([
            (i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
            (i, j - 1),                     (i, j + 1),
            (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)
        ]):
            neighbors[idx]["pos"] = (row, col)
            if 0 <= row < ROWS and 0 <= col < COLS:
                neighbors[idx]["cell"] = self.matrix[row][col]  
        return neighbors

class Simulation(Grid):
    def __init__(self, debug:bool=False): 
        super().__init__() 
        self.debug = debug
        self.debugAux = 0
        self.pause = True

    @staticmethod
    def loadGrid(path:str):
        aux = Simulation()
        with open(path, "r") as data:
            gridJson = json.load(data)
        for i, row in enumerate(gridJson):
            for j, c in enumerate(row):
                if c == "None": aux.paintCell((i,j), None)
                else: aux.paintCell((i,j), Cell(c))
        return aux
    
    def update(self):
        if self.pause: return
        processed_cells = set()

        for i, line in enumerate(self.matrix):
            for j, cell in enumerate(line):
                if cell is None or (i, j) in processed_cells: continue
                neighbors = self.getNeighbors((i,j))
                aux = self.__cellularAutomata((i,j), neighbors)
                processed_cells.add(aux if aux is not None else (i,j))

    def __cellularAutomata(self, pos:tuple[int,int], neighbors:list[None | Cell]):
        i, j = pos
        if not self.matrix[i][j].move: return
        if self.debug: 
            print(f"i:{self.debugAux} / pos:{pos} / cell: {self.matrix[i][j].name}")
            self.debugAux += 1

        # queda simples
        if neighbors[6]["cell"] == None:
            self.swapCellsPosition(pos, neighbors[6]["pos"])
            return neighbors[6]["pos"]
        
        match self.matrix[i][j].name:
            case "SAND": 
                # densidade
                if neighbors[6]["cell"].name == "WATER": 
                    self.swapCellsPosition(pos, neighbors[6]["pos"])
                    return neighbors[6]["pos"]
                # colisão com outra célula
                if neighbors[6]["cell"] != None:  
                    l = neighbors[5]["cell"] is None or neighbors[5]["cell"].name == "WATER"
                    r = neighbors[7]["cell"] is None or neighbors[7]["cell"].name == "WATER"
                    if l == False and r == False: return
                    if l == False and r == True:
                        self.swapCellsPosition(pos, neighbors[7]["pos"])
                        return neighbors[7]["pos"]
                    if l == True and r == False:
                        self.swapCellsPosition(pos, neighbors[5]["pos"])
                        return neighbors[5]["pos"]
                    aux = random.choice([neighbors[5]["pos"], neighbors[7]["pos"]])
                    self.swapCellsPosition(pos, aux)
                    return aux

            case "WATER": 
                # colisão em baixo com outra célula
                if neighbors[6]["cell"] != None:  
                    l = neighbors[5]["cell"] is None
                    r = neighbors[7]["cell"] is None
                    if l == False and r == False: return
                    if l == False and r == True:
                        self.swapCellsPosition(pos, neighbors[7]["pos"])
                        return neighbors[7]["pos"]
                    if l == True and r == False:
                        self.swapCellsPosition(pos, neighbors[5]["pos"])
                        return neighbors[5]["pos"]
                    aux = random.choice([neighbors[5]["pos"], neighbors[7]["pos"]])
                    self.swapCellsPosition(pos, aux)
                    return aux

            case "SMOKE": pass
            case "ROCK": pass