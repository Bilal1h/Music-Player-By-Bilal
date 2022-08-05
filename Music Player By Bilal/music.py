from pygame import mixer
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image 

root = Tk()
root.geometry("600x370")
root.resizable(False,False)
root.title("Music Player")
root.wm_iconbitmap("musicimage.ico")
mixer.init()

def openmusic():
    musfile = askopenfilename(defaultextension=".mp3",filetypes=[("Music Files","*.mp3*")])
    mixer.music.load(musfile)
def pause():
    mixer.music.pause()


def play():
    mixer.music.play()


def resume():
    mixer.music.unpause()

menu = Menu(root)
submenu = Menu(menu,tearoff=False)
submenu.add_command(label="Open",command=openmusic)
menu.add_cascade(label="File",menu=submenu)
# menu.add_cascade(label="Exit",menu=menu)

root.config(menu=menu)
# Label(root, text="Music Player By Bilal", font="lucidia 30 bold").place(x=200,y=100)
img = PhotoImage(file='C:/Users/TALAL/Documents/notepad/musicimagenor.png')
limg = Label(root,image=img)
limg.pack()
Button(root,text="Play", command=play,font="nexa 20 bold").place(x=259,y=285)
Button(root,text="Pause", command=pause,font="nexa 20 bold").place(x=5,y=285)
Button(root,text="Resume", command=resume,font="nexa 20 bold").place(x=460,y=285)

root.mainloop()
