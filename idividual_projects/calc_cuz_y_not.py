# BB 1st Financial Calculator Project
#Import nessesary libraries
import msvcrt, time

#Clear screen function
def wipe(): 
    return print("\033c",end="")

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
    

#Make menu
stuf = 0


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
        time.sleep(0.05)
        print(item)
    elif action == 'down': 
        stuf -= 1
        time.sleep(0.05)
        print(item)
    elif action == 'left': 
        stuf -= 0.5
        time.sleep(0.05)
        print(item)
    elif action == 'right': 
        stuf += 0.5
        time.sleep(0.05)
        print(item)
        
    else: 
        time.sleep(0.05)
        print("Wait")
