from Simulation.Grid.cell import Cell
from Simulation.Utils import ROWS, COLS, json

class Grid:
    def __init__(self):
        self.matrix = [
            [None for _ in range(COLS)] for _ in range(ROWS)
        ]
    
    def reset(self):
        self.matrix = [
            [None for _ in range(COLS)] for _ in range(ROWS)
        ]

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
        self.matrix[row1][col1], self.matrix[row2][col2] = self.matrix[row2][col2], self.matrix[row1][col1]

    def saveGrid(self, path: str):
        grid_data = [
            [cell.name if cell is not None else "None" for cell in row] for row in self.matrix
        ]
        with open(path, 'w') as json_file:
            json.dump(grid_data, json_file, indent=4)

    def getNeighbors(self, pos: tuple[int, int]):
        i, j = pos
        neighbors = [{"row": None, "col": None, "Cell": None} for _ in range(8)]
        
        # Define as posições dos vizinhos em torno da célula (i, j).
        for idx, (row, col) in enumerate([
            (i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
            (i, j - 1), (i, j + 1),
            (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)
        ]):
            if 0 <= row < ROWS and 0 <= col < COLS:
                neighbors[idx]["row"] = row
                neighbors[idx]["col"] = col
                neighbors[idx]["Cell"] = self.matrix[row][col]
        
        return neighbors


    @staticmethod
    def loadGrid(path:str):
        aux = Grid()
        with open(path, "r") as data:
            gridJson = json.load(data)
        for i, row in enumerate(gridJson):
            for j, c in enumerate(row):
                if c == "None": aux.paintCell((i,j), None)
                else: aux.paintCell((i,j), Cell(c))
        return aux