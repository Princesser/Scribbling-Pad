

from cgitb import text
from tkinter.filedialog import *
import tkinter as tk

  
def saveFile():
    new_file = askopenfile(mode= 'w', filetype= [('text files', '.txt')])
    if new_file is None:
      return
    text = str(entry.get (1.0, tk.END))
    new_file.write(text)
    new_file.close()


def openFile():
  file = askopenfile(mode= 'r', filetype= [('text files', '*.txt')])
  if file is not None:
    content = file.read()
    entry.insert(tk.INSERT, content)

def clearFile():
  entry.delete(1.0, tk.END)

tk.Canvas = tk.Tk()
tk.Canvas.geometry("400x600")
tk.Canvas.title("Notepad")
tk.Canvas.config(bg= "white")
top = tk.Frame(tk.Canvas)
top.pack(padx= 10, pady= 5, anchor= 'nw')

b1 = tk.Button(tk.Canvas, text= "Open", bg= "white", command= openFile)
b1.pack(in_= top, side= tk.LEFT)

b2 = tk.Button(tk.Canvas, text= "Save", bg= "white", command= saveFile)
b2.pack(in_=top, side= tk.LEFT)

b3 = tk.Button(tk.Canvas, text= "Clear", bg= "white", command= clearFile)
b3.pack(in_=top, side= tk.LEFT)

b4 = tk.Button(tk.Canvas, text= "Exit", bg= "white", command= exit)
b4.pack(in_=top, side= tk.LEFT)

entry = tk.Text(tk.Canvas, wrap= tk.WORD, bg = "#728FCE", font = ("popins", 15))
entry.pack(padx= 10, pady= 5, expand= tk.TRUE, fill= tk.BOTH)



tk.Canvas.mainloop()