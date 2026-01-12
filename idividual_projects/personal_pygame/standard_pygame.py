import sys, os, time, tkinter as tk, msvcrt
from music_controller import MusicController   # <-- ADDED

RESET = "\033[0m"
wipe = lambda: print("\033[2J", end="")

# ---------------------------------------------------------
# IMAGE CLASS (black & white are transparent)
# ---------------------------------------------------------
class Image:
    def __init__(self, path):
        if not os.path.isabs(path):
            base = os.path.dirname(os.path.abspath(__file__))
            path = os.path.join(base, path)
        self.path = path
        self._load()

    def _load(self):
        root = tk.Tk(); root.withdraw()
        self.img = tk.PhotoImage(file=self.path)
        self.ow, self.oh = self.img.width(), self.img.height()
        self.sprite = None

    def _parse_pixel(self, v):
        if v == "" or v is None:
            return None
        if isinstance(v, str) and v.startswith("#") and len(v) == 7:
            r = int(v[1:3], 16)
            g = int(v[3:5], 16)
            b = int(v[5:7], 16)
            if (r, g, b) in [(0, 0, 0), (255, 255, 255)]:
                return None
            return (r, g, b)
        if isinstance(v, tuple) and len(v) >= 3:
            r, g, b = v[:3]
            if (r, g, b) in [(0, 0, 0), (255, 255, 255)]:
                return None
            return (r, g, b)
        return None

    def size(self, w):
        ow, oh = self.ow, self.oh
        h = int(w * (oh / ow))
        sx, sy = ow / w, oh / h
        sprite = []
        for y in range(h):
            row = []
            for x in range(w):
                px = int(x * sx)
                py = int(y * sy)
                row.append(self._parse_pixel(self.img.get(px, py)))
            sprite.append(row)
        self.sprite = sprite
        return self

# ---------------------------------------------------------
# POSITION
# ---------------------------------------------------------
class Position:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

# ---------------------------------------------------------
# FRAMEBUFFER (▀ renderer)
# ---------------------------------------------------------
class Framebuffer:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.fb = [[(0, 0, 0) for _ in range(w)] for _ in range(h * 2)]

    def clear(self, c=(0, 0, 0)):
        for y in range(self.h * 2):
            for x in range(self.w):
                self.fb[y][x] = c

    def blit(self, sprite, px, py):
        if sprite is None:
            return
        sh, sw = len(sprite), len(sprite[0])
        for y in range(sh):
            fy = py + y
            if 0 <= fy < self.h * 2:
                for x in range(sw):
                    fx = px + x
                    if 0 <= fx < self.w:
                        color = sprite[y][x]
                        if color is not None:
                            self.fb[fy][fx] = color

    def render(self):
        sys.stdout.write("\033[H")
        out = []
        for row in range(0, self.h * 2, 2):
            line = []
            last_fg = None
            last_bg = None
            for x in range(self.w):
                top = self.fb[row][x]
                bottom = self.fb[row + 1][x]
                if top != last_fg or bottom != last_bg:
                    line.append(
                        f"\033[38;2;{top[0]};{top[1]};{top[2]}m" +
                        f"\033[48;2;{bottom[0]};{bottom[1]};{bottom[2]}m"
                    )
                    last_fg = top
                    last_bg = bottom
                line.append("▀")
            line.append(RESET)
            out.append("".join(line))
        sys.stdout.write("\n".join(out))
        sys.stdout.flush()

# ---------------------------------------------------------
# INPUT
# ---------------------------------------------------------
def get_input():
    if not msvcrt.kbhit():
        return None, 0
    k = msvcrt.getch()
    if k == b'\xe0':
        k = msvcrt.getch()
        action = {
            b'H': 'up',
            b'P': 'down',
            b'K': 'left',
            b'M': 'right'
        }.get(k)
    else:
        action = k.decode('ascii', 'ignore')
    start = last = time.perf_counter()
    while True:
        if msvcrt.kbhit():
            msvcrt.getch()
            last = time.perf_counter()
        if time.perf_counter() - last > 0.1:
            break
    return action, time.perf_counter() - start

# ---------------------------------------------------------
# ENGINE (with move‑mode toggle + MUSIC)
# ---------------------------------------------------------
class Engine:
    def __init__(self, w=120, h=30):
        self.fb = Framebuffer(w, h)
        self.entities = []
        self.running = True

        self.cam_x = 0
        self.cam_y = 0
        self.move_with_background = True

        # -------------------------
        # MUSIC SETUP
        # -------------------------
        base = os.path.dirname(os.path.abspath(__file__))
        requested = {
            "battle": "Organization Battle.wav",
            "town": "Twilight Town.wav",
            "destiny": "Destiny Islands.wav",
            "final1": "KH-CoM Final Battle1.wav",
            "final2": "KH-CoM Final Battle2.wav",
        }

        tracks = {}
        for key, fname in requested.items():
            p = os.path.join(base, fname)
            if os.path.exists(p):
                tracks[key] = p

        self.music = MusicController(tracks)

    def add(self, image, x, y, layer=0):
        self.entities.append([image, Position(x, y), layer])

    def run(self):
        wipe()

        # Start default music
        if "town" in self.music.tracks:
            self.music.play("town")

        while self.running:
            act, dur = get_input()

            # Quit
            if act == "q":
                self.music.stop_all()
                self.running = False

            # Toggle movement mode
            if act == "b":
                self.move_with_background = not self.move_with_background

            # MUSIC CONTROLS
            if act == "1": self.music.play("town")
            if act == "2": self.music.play("battle")
            if act == "3": self.music.play("destiny")
            if act == "4": self.music.play("final1")
            if act == "5": self.music.play("final2")
            if act == "m": self.music.pause()
            if act == "n": self.music.resume()
            if act == "x": self.music.stop()

            # Player (first entity)
            img, pos, layer = self.entities[0]

            # MODE A: Background moves
            if self.move_with_background:
                cam_speed = 2
                if act == "left":  self.cam_x -= cam_speed
                if act == "right": self.cam_x += cam_speed
                if act == "up":    self.cam_y -= cam_speed
                if act == "down":  self.cam_y += cam_speed

            # MODE B: Player moves
            else:
                move_speed = 1
                if act == "left":  pos.x -= move_speed
                if act == "right": pos.x += move_speed
                if act == "up":    pos.y -= move_speed
                if act == "down":  pos.y += move_speed

            # Draw
            self.fb.clear()
            for img, pos, layer in sorted(self.entities, key=lambda e: e[2]):
                sx = pos.x - self.cam_x
                sy = pos.y - self.cam_y
                self.fb.blit(img.sprite, int(sx), int(sy))

            self.fb.render()
            time.sleep(1 / 30)

# ---------------------------------------------------------
# LIBRARY MODE
# ---------------------------------------------------------
if __name__ == "__main__":
    print("standard_pygame loaded.")
