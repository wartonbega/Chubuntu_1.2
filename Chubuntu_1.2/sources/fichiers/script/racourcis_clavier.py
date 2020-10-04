from tkinter import*

def quitter(event):
    window.destroy()

window = tk()

window.title("commandes clavier")
widow.bind('<Control_L>'+'q',quitter)

window.mainloop()


