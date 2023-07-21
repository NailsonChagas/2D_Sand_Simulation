from Game import Window
import os

if __name__ == "__main__":
    simulation = Window("Simulation", os.path.join(".", "grid.json"), False)
    simulation.run()