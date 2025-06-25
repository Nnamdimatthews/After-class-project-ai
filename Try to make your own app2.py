from tkinter import *
from PIL import Image, ImageTk

root =Tk()
root.title("Introduction to Tkinter makey app")
root.geometry("800x500")
root.configure(bg="green")
root.resizable(False,False)
panda = Image.open("Double panda.png")
panda1 = ImageTk.PhotoImage(panda)
root.iconphoto(False, panda1)

root.mainloop