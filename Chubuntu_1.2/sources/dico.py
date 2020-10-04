from tkinter import*
import codecs


liste = r"liste_francais.txt"
encoding = 'latin-1'
mots=['aaron',]
maj=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
majuscules={'A':'a','B':'b','C':'c','D':'d','E':'e','F':'f','G':'g','H':'h','I':'i','J':'j','K':'k','L':'l','M':'m','N':'n','O':'o','P':'p','Q':'q','R':'r','S':'s','T':'t','U':'u','V':'v','W':'w','X':'x','Y':'y','Z':'z'}


with codecs.open(liste, 'r', encoding) as lines:
    a=1
    for i in lines:
        mots.append(i)
        for y in range(len(maj)):
            if mots[a][0]==maj[y]:
                mots[a]=mots[a].replace(mots[a][0],majuscules[maj[y]],1)
                break
        a+=1


def search_dico():
    text.delete('1.0', END)
    for i in range (len(mots)):
        if dico_search.get() in mots[i]:
            text.insert(END,mots[i][:-2]+'\n')

def dico_search(event):
    text.delete('1.0', END)
    a=0
    for i in range (len(mots)):
        if dico_search.get() in mots[i]:
            text.insert(END,mots[i][:-2]+'\n')
        a+=1

dico = Tk()

def destroy(event):
    dico.destroy()


dico.bind("<Control_L>"+"q", destroy)
dico.bind("<Return>",dico_search)
dico.title("dictionnaire français")
dico.geometry("480x500")
dico.config(background='black')
dico.minsize(480, 360)
scrollbar = Scrollbar(dico)
text = Text( dico ,bg="black", fg="white", yscrollcommand=scrollbar.set)
scrollbar.config(command=text.yview)
scrollbar.pack(side='left', fill='y')
text.pack(side='bottom', expand=0, fill='both')
dico_search = Entry(dico, bg="black", fg="white")
dico_search.pack()
dico_search_button= Button(dico, text="rechercher",command=search_dico )
dico_search_button.pack()


barre = Menu(dico)

fermer=Menu(barre,tearoff=0)
fermer.add_command(label="fermer", command=dico.destroy)
barre.add_cascade(label='fermer', menu=fermer)

dico.config(menu=barre)
inzoo=dico_search.get()
dico.mainloop()