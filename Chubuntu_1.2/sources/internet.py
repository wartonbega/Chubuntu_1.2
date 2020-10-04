from tkinter import*
import webbrowser
import time
nb=0


def rechercher():
    global nb
    url = recherche.get()
    googleresearch = ''
    if url == 'https://pastebin.com/G4XjWmfb':
        hisoric.insert(END, "bien joué?\n")
        nb+=1
        hisoric.insert(END, "recherche n°"+str(nb)+" : "+url+"\n" )
        webbrowser.open(url)
        hisoric.insert(END,"ou pas?\n")

    elif url[0] == 'https://':
        nb+=1
        hisoric.insert(END, "recherche n°"+str(nb)+" : "+url+"\n" )
        webbrowser.open(url)
    elif url[0:4] == 'www.':
        nb+=1
        webbrowser.open("https://"+url)
        hisoric.insert(END, "recherche n°"+str(nb)+" : "+url+"\n" )
    else:
        nb+=1
        for i in range(len(url)):
            if url[i] == ' ':
                googleresearch+='+'
            else:
                googleresearch+=url[i]
        webbrowser.open('https://www.google.com/search?channel=fs&client=ubuntu&q='+googleresearch)
        hisoric.insert(END,"recherche n°"+str(nb)+' : recherche google : '+url)
    

window = Tk()

def destroy(event):
    window.destroy()


window.bind("<Control_L>"+"q", destroy)


window.geometry('300x550')
window.title("navigateur")

titre = Label(window, text="entrez l'url du site a rechercher : ")
titre.pack(side='top', expand=YES)
recherche = Entry(window)
recherche.pack(side='top', expand=YES)
recherchebut = Button(window,text="rechercher", command=rechercher)
recherchebut.pack(side='top', expand=YES)

historiclabel = Label(window, text = "historique : ")
hisoric = Text(window)
hisoric.pack(side='bottom', expand=NO)

historiclabel.pack(side='bottom', expand=YES)

file = open('./settings/sombre','r')
sombre = file.read()
file.close()
if sombre == 'oui':
    window.config(bg='black')
    titre.config(bg='black',fg='white')
    historiclabel.config(bg='black',fg='white')
    hisoric.config(bg='black',fg='white')


window.mainloop()
