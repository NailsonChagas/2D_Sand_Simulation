from Simulation import Window
import os

win = Window("Simulation", os.path.join(".", "save.json"), True)
win.run()

# basear nisso para pegar em volta
# def getNeighbors(grid:list[list[Cell]], pos:tuple[int,int]):
#         """
#         pos:tuple[int,int] = (i, j)
#         return: [
#                     j - 1    j     j + 1
#             i - 1     C      C       C 
#             i         C      X       C
#             i + 1     C      C       C
#         ]
#         """
#         i, j = pos
#         neighbors = []
#         indices = [ # Define os índices dos vizinhos em torno da célula (i, j)
#             (i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
#             (i, j - 1),                 (i, j + 1),
#             (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)
#         ]
#         for (row, col) in indices:
#             if 0 <= row < ROWS and 0 <= col < COLS: 
#                 neighbors.append({"row": row, "col":col, "Cell":grid[row][col]})
#             else:
#                 neighbors.append({"row": row, "col":col, "Cell":None})
#         return neighbors 