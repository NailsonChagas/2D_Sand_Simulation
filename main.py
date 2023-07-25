from Simulation import Window
import os

win = Window("Simulation", os.path.join(".", "save.json"), False)
win.run()