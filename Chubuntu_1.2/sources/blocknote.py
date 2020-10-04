from tkinter import*
import codecs
import os
import webbrowser

Nom = open('./settings/Nom.txt','r')
Titre = Nom.read()
Nom.close()

def reglages():
    global color_change
    global sett
    sett = Tk()
    sett.title("reglages")
    sett.geometry("400x200")
    entre = Button(sett,text = "valider la couleure", command=coulure)
    color_change = Entry(sett)
    color_change.bind('<Return>',couleure)
    label_color = Label(sett, text="entre la couleure : ")
    label_color.pack()
    color_change.pack()
    entre.pack()

def couleure(event):
    coulure()

def coulure():
    global couleur
    couleur=str(color_change.get())
    textfield.config(bg=couleur, fg='black')
    if couleur=='black':
        textfield.config(fg='white')
    fichier = open("./settings/color", "w")
    fichier.write(couleur)
    fichier.close()

def urlc():
    webbrowser.open('http://'+url)

def urlc2():
    webbrowser.open(urla)

def saveb(event):
    global Titre
    titre=str(title.get())
    content=str(textfield.get(0.0,END))
    if str(titre[-3:])=='.py':
        fichier = open("./fichiers/"+titre, "w")
        fichier.write(content+' ')
        fichier.close()
        fichier = open("./settings/Nom.txt",'w')
        Titre = fichier.write(titre)
        fichier.close()
        save.destroy()
    else:
        fichier = open("./fichiers/"+titre+'.txt', "w")
        fichier.write(content)
        fichier.close()
        fichier = open("./settings/Nom.txt",'w')
        Titre = fichier.write(titre)
        fichier.close()
        save.destroy()

def savec(event):
    global title
    global save
    save = Tk()
    save.title("sauvegarder")
    save.bind("<Return>",saveb)
    title = Entry(save)
    title.pack()
    fichier = open("./settings/Nom.txt",'r')
    Titre = fichier.read()
    fichier.close()
    title.insert(END,Titre)

def openec(event):
    global ouvr
    global tutre
    global Titre
    urlbut.forget()
    urlbut2.forget()
    ouvr = Tk()
    ouvr.bind("<Return>",ouvrir)
    ouvr.title("ouvrir")
    tutre = Entry(ouvr)
    tutre.bind("<Return>",ouvrir)
    tutre.pack()
    fichier = open("./settings/Nom.txt",'r')
    Titre = fichier.read()
    fichier.close()
    tutre.insert(END,Titre)


def ouvrir(event):
    try:
        global url
        global urla
        url=''
        urla=''

        titre=tutre.get()
        fichier = open("./settings/Nom.txt",'w')
        Titre = fichier.write(titre)
        fichier.close()
        textfield.delete(0.0, END)
        existing = 0
        if titre[-3:]=='.py':
            with open("./fichiers/"+titre, "r") as ligne:
                a = ligne.read()
                textfield.insert(0.0,a)

        else:
            with open("./fichiers/"+titre+'.txt', "r") as ligne:
                a = ligne.read()
                textfield.insert(0.0,a)

        if existing==0:
            if 'https://' in a:
                existing=1
                for i in range(len (a)):
                    if str(a[i]+a[i+1]+a[i+2]+a[i+3]+a[i+4]+a[i+5]+a[i+6]+a[i+7])=='https://':
                        urla+=a[i]+a[i+1]+a[i+2]+a[i+3]+a[i+4]+a[i+5]+a[i+6]+a[i+7]
                        c=8
                        for x in range(len(a)):
                            if urla[-1]==' ':
                                urlbut2.pack(side="right")
                                break
                            urla+=str(a[i+c])
                            c+=1
                        break
        if existing==0:
            if 'www.' in a:
                existing=1
                for i in range(len (a)):
                    if str(a[i]+a[i+1]+a[i+2]+a[i+3])=='www.':
                        url+=a[i]+a[i+1]+a[i+2]+a[i+3]
                        c=4
                        for x in range(len(a)):
                            if url[-1]==' ':
                                urlbut.pack(side="right")
                                break
                            url+=str(a[i+c])
                            c+=1
                        break
        ouvr.destroy()
    except FileNotFoundError:
        tutre.delete(0,END)
        tutre.insert(END,'fichier non trouvé')

def destroy(event):
    main.destroy()

def contz(event):
    try:
        global url
        global urla
        url=''
        urla=''
        file = open('./settings/Nom.txt','r')
        titre = file.read()
        file.close()
        textfield.delete(0.0, END)
        existing = 0
        if titre[-3:]=='.py':
            with open("./fichiers/"+titre, "r") as ligne:
                a = ligne.read()
                textfield.insert(0.0,a)

        else:
            with open("./fichiers/"+titre+'.txt', "r") as ligne:
                a = ligne.read()
                textfield.insert(0.0,a)

        if existing==0:
            if 'https://' in a:
                existing=1
                for i in range(len (a)):
                    if str(a[i]+a[i+1]+a[i+2]+a[i+3]+a[i+4]+a[i+5]+a[i+6]+a[i+7])=='https://':
                        urla+=a[i]+a[i+1]+a[i+2]+a[i+3]+a[i+4]+a[i+5]+a[i+6]+a[i+7]
                        c=8
                        for x in range(len(a)):
                            if urla[-1]==' ':
                                urlbut2.pack(side="right")
                                break
                            urla+=str(a[i+c])
                            c+=1
                        break
        if existing==0:
            if 'www.' in a:
                existing=1
                for i in range(len (a)):
                    if str(a[i]+a[i+1]+a[i+2]+a[i+3])=='www.':
                        url+=a[i]+a[i+1]+a[i+2]+a[i+3]
                        c=4
                        for x in range(len(a)):
                            if url[-1]==' ':
                                urlbut.pack(side="right")
                                break
                            url+=str(a[i+c])
                            c+=1
                        break
    except FileNotFoundError:
        tutre.delete(0,END)
        tutre.insert(END,'fichier non trouvé')
        

def prct(event):
    a=textfield.get(0.0,END)
    print(a)

fichier=open("./settings/color", "r")
couleur=fichier.read()
fichier.close()

main = Tk()
main.bind("<Control_L>"+"q", destroy)
main.title("bloc note")
scrollbar = Scrollbar(main)
textfield = Text(main,bg=couleur,yscrollcommand=scrollbar.set)
if couleur=='black':
    textfield.config(fg='white')
scrollbar.config(command=textfield.yview)
scrollbar.pack(side='right', fill='y')
textfield.bind("<Control_L>"+"s",savec)
textfield.bind("<Control_L>"+"o",openec)
textfield.bind("<Control_L>"+"z",contz)
textfield.bind('<Control_L>'+'m',prct)
textfield.pack(side='right', fill='both')

urlbut2=Button(main, text="accès au site", command= urlc2)
urlbut=Button(main, text="accès au site", command= urlc)

reglage=Button(main, text='reglages', command=reglages)
reglage.pack(side='right',expand='YES')

file = open('./settings/sombre','r')
sombre = file.read()
file.close()
if sombre == 'oui':
    main.config(bg='black')
    textfield.config(bg='black',fg='white')
    
main.mainloop()

