import sys, os, time, tkinter as tk, msvcrt

RESET = "\033[0m"
wipe = lambda: print("\033[2J", end="")  # clear screen once

def bg(r,g,b): return f"\033[48;2;{r};{g};{b}m"

# ---------------------------------------------------------
# IMAGE CLASS
# ---------------------------------------------------------
class Image:
    def __init__(self, path):
        # Make relative paths work like your old img_path logic
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
        # v == "" (empty string) is how PhotoImage represents full transparency
        if v == "" or v is None:
            return None  # transparent pixel

        if isinstance(v, str) and v.startswith("#") and len(v) == 7:
            return int(v[1:3],16), int(v[3:5],16), int(v[5:7],16)

        if isinstance(v, tuple) and len(v) >= 3:
            return v[:3]

        return None  # treat unknown as transparent

    def size(self, w):
        """Resize image to terminal width w."""
        ow, oh = self.ow, self.oh
        h = int(w * (oh/ow) * 0.5)
        sx, sy = ow/w, oh/h

        sprite=[]
        for y in range(h):
            row=[]
            for x in range(w):
                px = int(x*sx)
                py = int(y*sy)
                row.append(self._parse_pixel(self.img.get(px, py)))
            sprite.append(row)

        self.sprite = sprite
        return self  # allow chaining

# ---------------------------------------------------------
# POSITION + COLLISION
# ---------------------------------------------------------
class Position:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

def aabb_collision(ent1, ent2):
    img1, pos1 = ent1
    img2, pos2 = ent2

    if img1.sprite is None or img2.sprite is None:
        return False

    w1, h1 = len(img1.sprite[0]), len(img1.sprite)
    w2, h2 = len(img2.sprite[0]), len(img2.sprite)

    return not (
        pos1.x + w1 <= pos2.x or
        pos1.x >= pos2.x + w2 or
        pos1.y + h1 <= pos2.y or
        pos1.y >= pos2.y + h2
    )

# ---------------------------------------------------------
# FRAMEBUFFER
# ---------------------------------------------------------
class Framebuffer:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.fb = [[(0,0,0) for _ in range(w)] for _ in range(h)]

    def clear(self, c=(0,0,0)):
        for y in range(self.h):
            for x in range(self.w):
                self.fb[y][x] = c

    def blit(self, sprite, px, py):
        if sprite is None: return
        sh, sw = len(sprite), len(sprite[0])
        for y in range(sh):
            fy = py + y
            if 0 <= fy < self.h:
                for x in range(sw):
                    fx = px + x
                    if 0 <= fx < self.w:
                        color = sprite[y][x]
                        if color is not None:  # skip transparent pixels
                            self.fb[fy][fx] = color

    def render(self):
        sys.stdout.write("\033[H")
        out=[]
        for row in self.fb:
            line=[]; last=None
            for r,g,b in row:
                if last!=(r,g,b):
                    line.append(bg(r,g,b)); last=(r,g,b)
                line.append("  ")
            out.append("".join(line)+RESET)
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
        action = {b'H':'up', b'P':'down', b'K':'left', b'M':'right'}.get(k)
    else:
        action = k.decode('ascii','ignore')

    start = last = time.perf_counter()

    while True:
        if msvcrt.kbhit():
            msvcrt.getch()
            last = time.perf_counter()
        if time.perf_counter() - last > 0.1:
            break

    return action, time.perf_counter() - start

# ---------------------------------------------------------
# ENGINE
# ---------------------------------------------------------
class Engine:
    def __init__(self, w=120, h=60):
        self.fb = Framebuffer(w, h)
        # entities: [Image, Position]
        self.entities = []
        self.running = True

    def add(self, image, x, y):
        self.entities.append([image, Position(x, y)])

    def run(self):
        wipe()  # clear once
        while self.running:
            act, dur = get_input()
            if act == "q":
                self.running = False

            # simple movement for first entity
            if self.entities:
                img, pos = self.entities[0]
                if act == "left":  pos.x -= 1
                if act == "right": pos.x += 1
                if act == "up":    pos.y -= 1
                if act == "down":  pos.y += 1

            # collision check between all pairs (placeholder behavior)
            if len(self.entities) > 1:
                for i in range(len(self.entities)):
                    for j in range(i+1, len(self.entities)):
                        if aabb_collision(self.entities[i], self.entities[j]):
                            # hook for your own collision response
                            pass

            self.fb.clear()
            for img, pos in self.entities:
                self.fb.blit(img.sprite, pos.x, pos.y)

            self.fb.render()
            time.sleep(1/30)

# ---------------------------------------------------------
# RUN DIRECTLY (library mode)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("standard_pygame loaded. Import it in another file to run a game.")
