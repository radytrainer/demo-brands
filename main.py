import tkinter as tk

window = tk.Tk()
window.geometry("600x600")
window.title("Demo")
# your code here
frame = tk.Frame(window)
frame.pack()

canvas = tk.Canvas(frame, width=500, height=500, bg="white")
canvas.pack()

canvas.create_rectangle(10, 10, 100, 100, fill="black")
window.mainloop()