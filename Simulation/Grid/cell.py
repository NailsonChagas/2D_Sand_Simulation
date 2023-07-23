from Simulation.Utils import COLORS

class Cell:
    def __init__(self, type:str):
        self.name = type
        self.color = ""
        match type:
            case "SMOKE": self.color = COLORS["GRAY"]
            case "SAND": self.color = COLORS["YELLOW"]
            case "WATER": self.color = COLORS["CYAN"]
            case "ROCK": self.color = COLORS["BLACK"]