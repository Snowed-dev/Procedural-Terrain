from tkinter import *
import subprocess

def clicked():
    subprocess.Popen(["python", "noisemap.py"])

root = Tk()  
root.title("Terrain Generation")
root.geometry('500x500')

btn = Button(root, text="Generate Button", fg="red", command=clicked)
btn.pack()

root.mainloop()
