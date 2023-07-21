from Game import Window

if __name__ == "__main__":
    simulation = Window("Simulation", "./grid.json", False)
    simulation.run()