from tkinter import*
import os
import time


infos=[["test","anton",],["test","ruta5056baga",],["X","X",]]
recherche=['',]
got=0



def login():
    log_ps.pack()

    log_pseudo.pack()
    log_md.pack()
    log_mdp.pack()
    log_valider.pack()
    log_deja.forget()
    log_biena.forget()
    log_error.forget()
    log_de.forget()

    log_md.pack()
    log_pseudo.pack()
    log_mdp.pack()

def log():
    log_deja.forget()
    log_biena.forget()
    log_error.forget()
    log_de.forget()
    hey=0
    z=0
    for i in range(len(infos[0])):
        if infos[0][hey]==log_pseudo.get()+'*':
            log_deja.pack()
            z=1
            break
        if log_pseudo.get()==infos[0][hey]:
            if z<1:

                z+=1

            if log_mdp.get()==infos[1][hey]:
                infos[0][hey]+='*'
                log_ps.forget()
                log_md.forget()
                log_pseudo.forget()
                log_mdp.forget()
                log_valider.forget()

                a=infos[0][hey]
                fichier=open("./settings/login.txt","w")
                fichier.write(a)
                fichier.close()
                file=open("./settings/admin.txt","w")
                file.write(infos[2][hey])
                file.close()
                log_biena.pack()
                time.sleep(5)
                os.popen("python3 main.py","r")
                window.destroy()
                break
            else:
                log_error.pack()
        hey+=1
    if z!=1:
        log_de.pack()

def destroy(event):
    window.destroy()


window = Tk()

window.bind("<Control_L>"+"q",destroy)

window.title("zapaovi")
window.attributes('-zoomed', True)
window.config(background='#2f3034')
window.minsize(480, 360)

frame = Frame(window, bg='#2f3034')

right_frame = Frame(frame, bg='#2f3034',)
left_frame = Frame(frame, bg='#2f3034',)


right_frame.grid(row=0, column=0, sticky=W)
left_frame.grid(row=0, column=2, sticky=W)

log_ps = Label(left_frame, text="votre pseudo : ", font=("Helvetica", 13), bg='#2f3034', fg='#fdcd5e')
log_md = Label(left_frame, text="votre mot de passe : ", font=("Helvetica", 13), bg='#2f3034', fg='#fdcd5e')
log_pseudo = Entry(left_frame, font=("helvetica", 13), bg='#2f3034', fg='#fdcd5e' )
log_mdp = Entry(left_frame, font=("helvetica", 13), bg='#2f3034', fg='#fdcd5e' )
log_valider = Button(left_frame, text="se loguer", font=("helvetica", 13), bg='#2f3034', fg='#fdcd5e', command=log)
log_deja = Label(left_frame, text="deja connécté", font=("Helvetica", 13), bg='#2f3034', fg='#fdcd5e')
log_biena = Label(left_frame, text="bien connécté", font=("Helvetica", 13), bg='#2f3034', fg='#fdcd5e')
log_error = Label(left_frame, text="mauvais mot de passe", font=("Helvetica", 13), bg='#2f3034', fg='#fdcd5e')
log_de = Label(left_frame, text="ce compte n'existe pas", font=("Helvetica", 13), bg='#2f3034', fg='#fdcd5e')


frame.pack(expand=YES)

barre_de_menu = Menu(window)
menu_fichier = Menu(barre_de_menu, tearoff=0)
menu_gestion = Menu(barre_de_menu, tearoff=0)
menu_acces = Menu(barre_de_menu, tearoff=0)
menu_compte = Menu(barre_de_menu, tearoff=0)
menu_alimentation = Menu(barre_de_menu, tearoff=0)


menu_gestion.add_command(label="se connecter", command=login)
menu_fichier.add_command(label="quitter", command=window.destroy)


barre_de_menu.add_cascade(label="fichier",menu=menu_fichier)
barre_de_menu.add_cascade(label="gestion",menu=menu_gestion)

window.config(menu=barre_de_menu)

login()
window.mainloop()
