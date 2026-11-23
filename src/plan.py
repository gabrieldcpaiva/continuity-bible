"""Floor plan for the worked example.

One geometry description feeds two renderers: a monospace plan for the editable
Markdown files, and a vector plan for the PDF. Same numbers, so the two cannot
disagree.

Coordinates are metres from the south-west corner of the room. x runs west->east
(0 to 4.2), y runs south->north (0 to 3.2). Cameras all sit on the south side.
"""

ROOM = (4.2, 3.2)
DOOR = dict(side="east", y0=1.35, y1=2.25)
ON_AIR = dict(side="east", y0=2.05, y1=2.35)
DESK = dict(x0=1.2, y0=1.55, x1=2.8, y1=2.25)
MIXER = dict(x0=1.45, y0=2.00, x1=2.25, y1=2.25)
CHAIR = (1.9, 2.52)
MIC = (2.45, 2.15)
MUG = (1.34, 1.86)
CLIP = (2.30, 1.80)
LAMP = (2.72, 1.66)
CORK = dict(x0=0.25, x1=1.15)
CLOCK = dict(x0=3.15, x1=3.60)

CAMERAS = [
    ("S1 / S6", 0.65, 0.45, "24 mm"),
    ("S2", 1.55, 0.75, "40 mm"),
    ("S3", 2.00, 1.75, "35 mm"),
    ("S4", 2.50, 0.90, "50 mm"),
    ("S5", 1.95, 0.60, "85 mm"),
]


def ascii_plan():
    """Monospace floor plan with a symbol key.

    One character per object, so the plan stays aligned in any monospace font,
    prints small, and can be edited by hand for your own scene.
    """
    COLS, ROWS = 36, 22
    g = [[" "] * COLS for _ in range(ROWS)]
    L, R, T, B = 2, 32, 2, 20

    def cx(x):
        return 2 + int(round(x * (R - L) / ROOM[0]))

    def ry(y):
        return (B - 1) - int(round(y * (B - T - 1) / ROOM[1]))

    def put(r, c, s):
        for i, ch in enumerate(s):
            if 0 <= r < ROWS and 0 <= c + i < COLS:
                g[r][c + i] = ch

    for c in range(L, R + 1):
        g[T][c] = "-" if c not in (L, R) else "+"
        g[B][c] = "-" if c not in (L, R) else "+"
    for r in range(T, B + 1):
        g[r][L] = "|" if r not in (T, B) else "+"
        g[r][R] = "|" if r not in (T, B) else "+"

    for r in range(ry(DOOR["y1"]), ry(DOOR["y0"]) + 1):
        g[r][R] = "D"

    put(T, cx(CORK["x0"]), "FF")
    put(T, cx(CLOCK["x0"]), "GGG")

    dx0, dx1 = cx(DESK["x0"]), cx(DESK["x1"])
    dy0, dy1 = ry(DESK["y0"]), ry(DESK["y1"])
    for c in range(dx0, dx1 + 1):
        g[dy0][c] = "-"
        g[dy1][c] = "-"
    for r in range(dy1, dy0 + 1):
        g[r][dx0] = "|"
        g[r][dx1] = "|"

    put(ry(MIXER["y1"]) + 1, cx(MIXER["x0"]) + 1, "MMMMM")
    put(ry(MIC[1]), cx(MIC[0]), "A")
    put(ry(MUG[1]), cx(MUG[0]) + 1, "U")
    put(ry(CLIP[1]), cx(CLIP[0]) + 1, "C")
    put(ry(LAMP[1]), cx(LAMP[0]) + 1, "L")
    put(ry(CHAIR[1]), cx(CHAIR[0]), "R")

    for label, x, y, lens in CAMERAS:
        mark = "X" if "/" in label else label.replace("S", "")
        put(ry(y), cx(x), mark)

    put(T - 1, L, "NORTH")

    for rr in (dy0, dy1):
        g[rr][dx0] = "+"
        g[rr][dx1] = "+"

    body = "\n".join("".join(row).rstrip() for row in g).rstrip()
    body += "\n  SOUTH   every camera stands on this side of the line"
    key = (
        "\n\n  Key  +--+ room edge   D door, gap in the east wall   R RAE and chair\n"
        "       F corkboard      G clock ghost (empty)      A microphone   U mug\n"
        "       M mixer          C clipboard              L desk lamp\n"
        "       X camera for shots 1 and 6 (same position)   2-5 camera for that shot\n"
        "       3 is an overhead camera: it sits above the desk, inside the desk outline.\n"
        "       Room is 4.2 m east-west by 3.2 m north-south. One cell is about 0.15 m."
    )
    return body + key


if __name__ == "__main__":
    print(ascii_plan())
