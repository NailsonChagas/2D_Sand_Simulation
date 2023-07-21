COLORS: dict[str, tuple[int, int, int]] = {
    "WHITE": (255, 255, 255),
    "BLACK": (0, 0, 0),
    "GRAY": (128, 128, 128),
    "YELLOW": (255, 255, 0),
    "CYAN": (0, 255, 255),
}
FPS:int = 120
WIDTH, HEIGHT = (800, 900)
ROWS = COLS = 200
TOOLBAR_HEIGHT = HEIGHT - WIDTH
PX_SIZE = WIDTH // COLS
BG_COLOR = COLORS["WHITE"]
DRAW_GRID = True
GRAVITY = 1 # 1px/tick²