# BB 1st Financial Calculator Project
#Import nessesary libraries
import msvcrt, time

#Clear screen function
wipe = lambda: print("\033c", end="")

print("text")
wipe()

#Get selection keys function and variable
key = msvcrt.getch()
def read_action():
    if key == b'\xe0':
        arrow_key = msvcrt.getch()
    return {b'H': 'up', b'P': 'down', b'K': 'left', b'M': 'right'}.get(arrow_key)

#make divide function
def mult(item): 
    pass

#Make menu
stuf = 0

time.perf_counter()
#Get action
#move through menu code
while True: 
    menu = [" yes", " no", " maby"]
    action = read_action()
    menu_sel = menu
    item = menu_sel[stuf%3]
    item.replace(" ", ">")
    if action == 'up': 
        stuf += 1
        time.sleep(0.01)
        print(item)
    elif action == 'down': 
        stuf -= 1
        time.sleep(0.01)
        print(item)
    elif action == 'left': 
        stuf -= 1
        time.sleep(0.01)
        print(item)
    elif action == 'right': 
        stuf += 1
        time.sleep(0.01)
        print(item)
        
    else: 
        time.sleep(0.01)
