import sys
import os
import tkinter as tk

RESET = "\033[0m"

def bg(r, g, b):
    return f"\033[48;2;{r};{g};{b}m"

def load_image(path):
    root = tk.Tk()
    root.withdraw()
    return tk.PhotoImage(file=path)

def parse_pixel(value):
    if isinstance(value, str):
        if value.startswith("#") and len(value) == 7:
            try:
                return (
                    int(value[1:3], 16),
                    int(value[3:5], 16),
                    int(value[5:7], 16)
                )
            except ValueError:
                return (0, 0, 0)
        return (0, 0, 0)

    if isinstance(value, tuple):
        if len(value) >= 3:
            return value[:3]
        return (0, 0, 0)

    return (0, 0, 0)

def print_image_as_ansi(path, width=80):
    img = load_image(path)

    orig_w = img.width()
    orig_h = img.height()

    aspect = orig_h / orig_w
    height = int(width * aspect * 0.5)

    scale_x = orig_w / width
    scale_y = orig_h / height

    # Cache ANSI codes for speed
    ansi_cache = {}

    for y in range(height):
        src_y = int(y * scale_y)
        line_parts = []

        for x in range(width):
            src_x = int(x * scale_x)

            pixel = img.get(src_x, src_y)
            r, g, b = parse_pixel(pixel)

            key = (r, g, b)
            if key not in ansi_cache:
                ansi_cache[key] = f"\033[48;2;{r};{g};{b}m"

            line_parts.append(ansi_cache[key])
            line_parts.append("  ")  # two-space pixel

        sys.stdout.write("".join(line_parts) + RESET + "\n")

if __name__ == "__main__":
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    IMAGE_PATH = os.path.join(SCRIPT_DIR, "Noctis Shirt.png")

    print_image_as_ansi(IMAGE_PATH, width=300)
