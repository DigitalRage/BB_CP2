def wipe(): 
    return print("\033c",end="")

print("text")
wipe()