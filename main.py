import tkinter as tk

window = tk.Tk()
window.geometry("600x600")
window.title("Demo")
# your code here
canvas = tk.Canvas(frame, width=500, height=500, bg="white")
canvas.pack()
window.mainloop()