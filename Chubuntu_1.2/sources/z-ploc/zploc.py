import math
from termcolor import colored,cprint

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#IN

def dedans(A, B):
    if type(A) == int or type(B) == int:
        return 'les objets "int" ne peuvent pas être comparés'

    if len(A)>len(B):
        return False

    a = True
    b = 0
    lenA=len(A)
    lenB=len(B)
    while a:
        if est_prefix(A, B[b: b + lenA]):
            return True
        b += 1
        if b + len(A) >= lenB + 1:
            return False

def est_prefix(A, C):
    # Renvoie True si la chaîne A est égale à C
    n = len(A)   # également longueur de C
    for i in range(n):
        if A[i] != C[i]:
            return False
    return True

def egalitebis(A, C):
    # Renvoie True si la chaîne A est égale à C
    n = len(A)   # également longueur de C
    i = 0
    while i < n and A[i] == C[i] : # Merci l'évaluation paresseuse !
        i += 1
    return i == n

# ==

def eq(A,B):
    if A != B:
        return False
    else:
        return True

# !=
def neq(A,B):
    if A!=B:
        return True
    else:
        return False

# >
def sup(A,B):
    if type(A) == str or type(B) == str:
        return 'erreure, impossible de comparer les chaines de caractère'
    if A>B:
        return True
    else:
        return False


# <
def inf(A,B):
    if type(A) == str or type(B) == str:
        return 'erreure, impossible de comparer les chaines de caractère'
    if A>B:
        return False
    else:
        return True


class test:
    def si_in( elma, elmb,fonctionretour=None,option1=None,option2=None,option3=None,autrement=None,fonction2=None ,optionf21=None):
        if dedans(elma,elmb)==False:
            print( fonction2(optionf21))
            return dedans(elma, elmb)
        else:
            if fonctionretour!=None:
                if option3 != None:
                    print(fonctionretour(option1, option2, option3 ))
                elif option2 != None:
                    print(fonctionretour(option1,option2))
                elif option1 != None :
                    print(fonctionretour(option1))
            return dedans(elma,elmb)

    def si_eq( elma, elmb,fonctionretour=None,option1=None,option2=None,option3=None ):
        if eq(elma,elmb)==False:
            return eq(elma, elmb)
        else:
            if fonctionretour!=None:
                if option3 != None:
                    print(fonctionretour(option1, option2, option3 ))
                elif option2 != None:
                    print(fonctionretour(option1,option2))
                elif option1 != None :
                    print(fonctionretour(option1))
            return eq(elma,elmb)

    def si_neq( elma, elmb,fonctionretour=None,option1=None,option2=None,option3=None ):
        if eq(elma,elmb)==False:
            return neq(elma, elmb)
        else:
            if fonctionretour!=None:
                if option3 != None:
                    print(fonctionretour(option1, option2, option3 ))
                elif option2 != None:
                    print(fonctionretour(option1,option2))
                elif option1 != None :
                    print(fonctionretour(option1))
            return neq(elma,elmb)


    def si_sup(elma, elmb,fonctionretour=None,option1=None,option2=None,option3=None ):
        if eq(elma,elmb)==False:
            return sup(elma, elmb)
        else:
            if fonctionretour!=None:
                if option3 != None:
                    print(fonctionretour(option1, option2, option3 ))
                elif option2 != None:
                    print(fonctionretour(option1,option2))
                elif option1 != None :
                    print(fonctionretour(option1))
            return sup(elma,elmb)

    def si_inf( elma, elmb,fonctionretour=None,option1=None,option2=None,option3=None ):
        if inf(elma,elmb)==False:
            return inf(elma, elmb)
        else:
            if fonctionretour!=None:
                if option3 != None:
                    print(fonctionretour(option1, option2, option3 ))
                elif option2 != None:
                    print(fonctionretour(option1,option2))
                elif option1 != None :
                    print(fonctionretour(option1))
            return inf(elma,elmb)

class boucle:
    def pour(fin,action,option1 = None, option2 = None, option3=None, option4=None):
        for i in range(fin):
            if action == sortie.imprimme:
                print(colored("erreure : la fonction sortie.imprimme n'est pas utilisable dans les boucles. Veuillez utiliser la fonction sortie.imprimme_boucle","red"))
                break
            if option1 == nbr:
                if option4 != None:
                    print(action(i,option2, option3,option4))
                elif option3 != None:
                    print(action(i,option2, option3))
                elif option2 != None:
                    print(action(i,option2))
                elif option1 != None:
                    print(action(i))
            elif option2 == nbr:
                if option4 != None:
                    print(action(option1,i, option3,option4))
                elif option3 != None:
                    print(action(option1,i, option3))
                elif option2 != None:
                    print(action(option1,i))
                elif option1 != None:
                    print(action(option1))

            elif option3 == nbr:
                if option4 != None:
                    print(action(option1,option2, i,option4))
                elif option3 != None:
                    print(action(option1,option2, i))
                elif option2 != None:
                    print(action(option1,option2))
                elif option1 != None:
                    print(action(option1))

            elif option4 == nbr:
                if option4 != None:
                    print(action(option1,option2, option3,i))
                elif option3 != None:
                    print(action(option1,option2, option3))
                elif option2 != None:
                    print(action(option1,option2))
                elif option1 != None:
                    print(action(option1))

            else:
                a = action()
                if a == "erreure : pas d'objet indiqué":
                    print(action())
                    break
                else:
                    print(action())
            if action == sortie.retourne:
                break


    def tant_que(condition,action,option1 = None, option2 = None, option3=None,option4=None):
        i=0
        while condition:
            i +=1
            if option4 != None:
                print(action(option1,option2, option3,option4))
            elif option3 != None:
                print(action(option1,option2, option3))
            elif option2 != None:
                print(action(option1,option2))
            elif option1 != None:
                print(action(option1))
            else:
                print(action())
            if action == sortie.retourne:
                break
class sortie:
    def imprimme(objet=None,objet2=None,objet3=None,objet4=None,objet5=None, objet6=None):
        if objet == None:
            return "erreure : pas d'objet indiqué"

        if objet6 != None:
            print (objet ,objet2, objet3,objet4,objet5,objet6)
        elif objet5 != None:
            print (objet ,objet2, objet3,objet4,objet5)
        elif objet4 != None:
            print (objet ,objet2, objet3, objet4)
        elif objet3 != None:
            print (objet ,objet2, objet3)
        elif objet2 != None:
            print (objet ,objet2)
        else:
            print(objet)
    def imprimme_boucle(objet=None,objet2=None,objet3=None,objet4=None,objet5=None, objet6=None):
        if objet == None:
            return "erreure : pas d'objet indiqué"
        if objet6 != None:
            return objet ,objet2, objet3,objet4,objet5,objet6
        elif objet5 != None:
            return objet ,objet2, objet3,objet4,objet5
        elif objet4 != None:
            return objet ,objet2, objet3, objet4
        elif objet3 != None:
            return objet ,objet2, objet3
        elif objet2 != None:
            return objet ,objet2
        else:
            return(objet)

    def retourne(objet=None,objet2=None):
        return objet

    def entree(rentree=''):
        var = input(rentree)
        return var

fonctions=[]
nbr=0

class fonction:

    def definir(contenu,effet1=None, effet2=None, effet3=None):
        global nbr
        fonctions.append(contenu)
        a = len(fonctions)
        a-=1
        return a

    def executer(nmr,variable1=None,variable2=None, variable3=None, variable4=None):
        if variable4 != None:
            return fonctions[nmr](variable1, variable2,variable3,variable4)
        elif variable3 !=None:
            return fonctions[nmr](variable1,variable2,variable3)

        elif variable2 !=None:
            return fonctions[nmr](variable1,variable2)

        elif variable1 !=None:
            return fonctions[nmr](variable1)
        else:
            return fonctions[nmr]()
quotient = 0
reste=1
class maths:

    def racine_carre(nombre):
        racine = math.sqrt(nombre)
        return racine
    def puissance(nombre, exposant):
        return nombre**exposant
    def division_euclidienne(nombre, diviseur):


        division = nombre//diviseur
        resto = nombre%diviseur
        return division, resto
