from tkinter import *
from PIL import Image, ImageTk

root =Tk()
root.title("Introduction to Tkinter makey app")
root.geometry("800x500")
root.configure(bg="green")
root.resizable(False,False)
panda = Image.open(".png")
panda1 = ImageTk.PhotoImage(panda)
root.iconphoto(False, panda1)

root.mainloop

from tkinter import *
from PIL import Image, ImageTk

# Start your own intro for your Tkinter app/page title
root =Tk()
root.title("Introduction to Tkinter makey app")
root.geometry("800x500") # Getting your size
root.configure(bg="green")# Getting your inside background
root.resizable(False,False)#Continue your size
# Your image now
Sonic = Image.open("sonic_colors_4_.png")
Sonic1 = ImageTk.PhotoImage(panda)
root.iconphoto(False, panda1)