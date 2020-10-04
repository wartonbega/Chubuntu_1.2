import tkinter as tk
import os

def terminaux():
    os.popen('konsole','r')
    os.popen('konsole','r')

window = tk.Tk()
window.title('discord')

runbut=tk.Button(window,text='lancer discord',command=terminaux)
runbut.pack()

frame = tk.Label(window, text='executer dans la première console, la commande : <./c1_1DBR.sh>\npuis dans la deuxième : <./c1_1DBS.sh>\n assurez vous que quelqu un active votre chat en rentrant dans #général:\n*debut')
frame.pack()

window.mainloop()