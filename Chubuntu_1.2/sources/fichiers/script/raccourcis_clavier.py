from tkinter import*

def quitter(event):
    window.destroy()

window = Tk()

window.title("commandes clavier")
window.bind('<Control_L>'+'q',quitter)

window.mainloop()




