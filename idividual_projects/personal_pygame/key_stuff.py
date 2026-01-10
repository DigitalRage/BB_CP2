import msvcrt, time

def get_held_action():
    while not msvcrt.kbhit():
        time.sleep(0.001)

    k = msvcrt.getch()
    if k == b'\xe0':  # arrow prefix
        k = msvcrt.getch()
        action = {b'H':'up', b'P':'down', b'K':'left', b'M':'right'}.get(k)
    else:
        action = k.decode('ascii', 'ignore')

    start = last = time.perf_counter()

    while True:
        if msvcrt.kbhit():
            msvcrt.getch()
            if k in (b'H', b'P', b'K', b'M') and msvcrt.kbhit():
                msvcrt.getch()
            last = time.perf_counter()

        if time.perf_counter() - last > 0.1:
            break

    return action, time.perf_counter() - start


# Example
while True:
    act, dur = get_held_action()
    print(act, f"{dur:.2f}s")
