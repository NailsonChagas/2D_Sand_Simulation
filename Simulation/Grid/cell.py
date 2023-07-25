from Simulation.Utils import COLORS

class Cell:
    def __init__(self, type:str):
        self.name = type
        self.color = ""
        self.move = False
        self.direction = None
        self.first = True
        match type:
            case "SMOKE": self.color = COLORS["GRAY"]; self.move = True; self.first = True
            case "SAND": self.color = COLORS["YELLOW"]; self.move = True
            case "WATER": self.color = COLORS["CYAN"]; self.move = True
            case "ROCK": self.color = COLORS["BLACK"]