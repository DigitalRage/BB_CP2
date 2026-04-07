import tkinter as tk

root = tk.Tk()

root.title("Testing")
root.configure(background="orange")
root.minsize(250,250)
root.maxsize(1000,1000)
root.geometry("300x300+100+100")
label = tk.Label(root, text="This is currently working!")
label.config(fg="blue", bg="orange", font=("Times New Roman", 14, "bold"))
#stuff about button
root.count=0
def add():
    root.count+=1
    num["text"]= root.count

btn = tk.Button(root, text="ADD", command=add)
btn.pack()
num = tk.Label(root, text = "0")
num.pack()
label.pack()
image = tk.PhotoImage(file="P:\Buckler, Blaine\BB_CP2\img\Imag.gif")
tk.Label(root, image=image).pack()

"""file_path = "P:\Buckler, Blaine\BB_CP2\img\Imag.gif"
frames = []
i = 0
while True:
    try:
        # Load each frame by index
        frame = tk.PhotoImage(file=file_path, format=f"gif -index {i}")
        frames.append(frame)
        i += 1
    except tk.TclError:
        break  # End of frames reached

# 2. Function to update the frame
def update_gif(index):
    frame = frames[index]
    label.configure(image=frame)
    # Loop back to start (index + 1) % total_frames
    root.after(100, update_gif, (index + 1) % len(frames))

label = tk.Label(root)
label.pack()

# Start the animation
root.after(0, update_gif, 0)
root.mainloop()"""


root.mainloop()