from Simulation import Window
import os

win = Window("Simulation", os.path.join(".", "save.json"), True)
win.run()