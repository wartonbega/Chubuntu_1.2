from tkinter import*
import os
import string
import random
from PIL import ImageTk,Image

MAX_ROWS = 36
FONT_SIZE = 10 # (pixels)

COLORS = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
    'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
    'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
    'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
    'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
    'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
    'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
    'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
    'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
    'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
    'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
    'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
    'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
    'indian red', 'saddle brown', 'sandy brown',
    'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
    'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
    'pale violet red', 'maroon', 'medium violet red', 'violet red',
    'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
    'thistle', 'snow2', 'snow3',
    'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
    'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
    'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
    'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
    'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
    'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
    'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
    'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
    'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
    'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
    'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
    'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
    'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
    'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
    'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
    'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
    'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
    'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
    'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
    'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
    'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
    'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
    'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
    'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
    'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
    'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
    'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
    'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
    'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
    'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
    'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
    'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
    'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
    'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
    'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
    'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
    'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
    'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
    'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
    'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
    'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
    'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
    'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
    'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
    'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
    'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
    'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',
    'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',
    'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',
    'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',
    'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',
    'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',
    'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',
    'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',
    'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',
    'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
    'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']

def color_choice():
    root = Tk()
    root.title("Named colour chart")
    row = 0
    col = 0
    for color in COLORS:
      e = Label(root, text=color, background=color, 
            font=(None, -FONT_SIZE))
      e.grid(row=row, column=col, sticky=E+W)
      row += 1
      if (row > 36):
        row = 0
        col += 1
    
    root.mainloop()


filen=os.listdir(os.getcwd())
files = []
for i in range(len(filen)):
    if '.py' in filen[i]:
        files.append(filen[i])

def refreshe():
    fichier = open("./settings/colors","r")
    couleur=fichier.read()
    fichier.close()
    window.config(bg=couleur)

def shutdown():
    os.popen("shutdown -f now","r")

def ba():
    global button0
    global files
    global barre
    
    barre = Tk()
    barre.geometry("80x140")
    barre.config(bg=couleur)
    barre.title("barre de lancement d'applications")
    button0=Listbox(barre,xscrollcommand='YES',yscrollcommand='YES')
    button0.pack()
    button0.bind('<Double-Button-1>',runa)
    button0.config(bg=couleur)
    if couleur == 'black':
        button0.config(fg='white')
    nbr=0
    fichier = open('./settings/sombre','r')
    sombre = fichier.read()
    fichier.close()
    
    if sombre == 'oui':
        button0.config(bg='black',fg='white')
    else:
        barre.config(bg=couleur)
    for name in files:
        nbr+=1
        if name[:-3]=='accueuil':
            continue
        elif name[:-3]=='main':
            continue
        elif name[:-3]=='current':
            continue
        elif name[:-3]=='game':
            continue
        elif name[:-3]=='test':
            continue
        elif name[:-3]=='player':
            continue
        elif name[:-3]=='window':
            continue
        
        elif name[-3:]=='.py':
            a=name[:-3]
            button0.insert(END,name[:-3])
    button0.insert(END,'réglages')
        
def runa(event):
    if button0.get(button0.curselection()[0]) == 'réglages':
        reglages()
    else:
        os.popen('python3 '+button0.get(button0.curselection()[0])+'.py','r')
    
def butge(a):
    alea = random.randint(0,10)
    if alea == 4:
        fichier = open("./settings/jeu.txt","w")
        fichier.write(a)
        fichier.close()
        os.popen("python3 test.py")
    else:
        a=os.popen("python3 "+a+".py","r").read()
        print(a)

def sobre():
    global mode
    global barre
    if mode == 'oui':
        fichier = open("./settings/sombre","w")
        fichier.write('non')
        fichier.close()
        window.config(bg=couleur)
        mode = 'non'
        if barre :
            barre.config(bg=couleur)
            if couleur == 'black':
                button0.config(bg=couleur,fg='white')
            else:
                button0.config(bg=couleur,fg='black')
    elif mode == 'non':
        fichier = open("./settings/sombre","w")
        fichier.write('oui')
        fichier.close()
        window.config(bg='black')
        mode = 'oui'
        if barre :
            barre.config(bg='black')
            button0.config(bg='black',fg='white')
        
def reglages():
    file = open('./settings/sombre','r')
    so = file.read()
    file.close()
    
    global color_change
    global emplacementent
    global mode
    global hello
    sett = Tk()
    sett.title("settings")
    sett.geometry("400x400")
    hello=StringVar()
    entre = Button(sett,text = "valider la couleure", command=couleure)
    refresh = Button(sett, text = "rafraichir l'écran", command=refreshe)
    sombritude = Checkbutton(sett, text='mode sombre',command=sobre)
    sombritude.pack()
    different_colors=Button(sett, text='toutes les couleurs',command=color_choice)
    different_colors.pack()
    if so == 'oui':
        sombritude.select()
        mode = 'oui'
    elif so =='non':
        sombritude.deselect()
        mode='non'
    color_change = Entry(sett)
    label_color = Label(sett, text="Entrez la couleure : ")
    
    label_color.pack()
    color_change.pack()
    entre.pack()
    refresh.pack()

def couleure():
    global couleur
    couleur=str(color_change.get())
    if couleur == 'anton appel est la plus belle personne qui existe sur terre':
        file=open('./fichiers/texte/wp.txt','w')
        file.write('Anton est effectivement la plus jolie personne au monde mais pas besoin de le crier sur tous les toits, on le sait déja tous x).')
        file.close()
        color_change.delete(0,END)
        color_change.insert(END,'/texte/wp.txt')
    else:
        try:
            if couleur == 'sombre':
                fichier = open("./settings/sombre",'w')
                fichier.write('oui')
                fichier.close()
                window.config(bg='black')
            else:
                window.config(bg=couleur)
                fichier = open("./settings/colors", "w")
                fichier.write(couleur)
                fichier.close()
                
        except TclError:
            color_change.delete(0,END)
            color_change.insert(END,'Mauvaise couleur indiquée')

def navigateur():
    os.popen("python3 internet.py", "r")


def destroy(event):
    window.destroy()



#configuration des couleurs
fichier=open("./settings/colors", "r")
couleur=fichier.read()
fichier.close()



# configuration de la fenetre
window = Tk()

window.bind("<Control_L>"+"q",destroy)
window.title("bureau")
window.attributes('-fullscreen', True)

window.config(bg=couleur)

file = open('./settings/sombre','r')
so = file.read()
file.close()

if so == 'oui':
    window.config(bg = 'black')

window.minsize(480, 360)
frame = Frame(window, bg='black')
right_frame = Frame(frame, bg='black',)
left_frame = Frame(frame, bg='black',)
right_frame.grid(row=0, column=0, sticky=W)
left_frame.grid(row=0, column=2, sticky=W)

frame.pack(expand=YES)

barre_menu = Button(left_frame, text="barre d'application", command=ba)
barre_menu.pack()

barre_de_menu = Menu(window)

menu_fichier = Menu(barre_de_menu, tearoff=0)
menu_app = Menu(barre_de_menu, tearoff=0)


menu_fichier.add_command(label="quitter", command=window.destroy)
menu_fichier.add_command(label="éteindre", command=shutdown)
menu_app.add_command(label="barre d'application", command=ba)

barre_de_menu.add_cascade(label="quitter",menu=menu_fichier)
barre_de_menu.add_cascade(label="programmes",menu=menu_app)

window.config(menu=barre_de_menu)


window.mainloop()