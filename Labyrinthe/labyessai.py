#Auteurs : Louis Duong et Romy Mahieu (20201858)
#Date de création : 1 novembre 2021

#Ce programme crée un labyrinthe rectangulaire aléatoire qui posséde une solution unique.

X=None; Y=None

N=[]; E=[]; S=[]; O=[]

murH=[]; murV=[]; coordonneeMurH=[]; coordonneeMurV=[]

tableXY = []

front = []; celChoisi = []; cave=[]; choix=[]

typeMur=''; numMur = 0; murChoisi = 0


#La fonction contient vérifie si la valeur "x" se trouve dans la table. 
#Elle retourne un booléen selon si la table contient ou non la valeur "x"
def contient(tab,x):
    for i in range(len(tab)):
        if tab[i]==x:
            return True
    return False

#Cette fontion vérifie d'abord si la table contient déjà la valeur "x". 
#Si ce n'est pas le cas, elle ajoute la valeur à la fin de la table
def ajouter(tab,x):
    if contient(tab,x):
        return tab
    else:
        tab.append(x)
        return tab

#Cette fonction vérifie d'abord si la table contient la valeur "x". 
#Si c'est le cas, elle retire "x" de la table.
def retirer(tab,x):
    if contient(tab,x):
        tab.remove(x)
        return tab
    else:
        return tab

#Cette fonction créée la liste des coordonnées (x,y) des cellules de la 
#grille qui vont servir à créer le labyrinthe. Pour cela, elle prends deux
#nombres, soit nX (la longueur de la grille) et nY (la hauteur de la grille).
def nombre(nX,nY):
    global tableXY
    for i in range(nY):
        for j in range(nX):
            tableXY.append([j,i])
    return tableXY

#La fonction murs prends deux paramétres en compte (nX et nY) et appelle 
#la fonction nombre(x,y) afin de retourne une liste pour chaque type 
#de mur d'une cellule. Il s'agit de la liste des murs nord, est, sud et 
# ouest pour chaque cellule.
def murs(nX,nY): 
    nombre(nX,nY)
    global N,S,E,O
    for i in range(len(tableXY)):
            N.append(tableXY[i][0]+tableXY[i][1]*nX)
            E.append(1+tableXY[i][0]+tableXY[i][1]*(nX+1))
            S.append(tableXY[i][0]+(tableXY[i][1]+1)*nX)
            O.append(tableXY[i][0]+tableXY[i][1]*(nX+1))
    return N,E,S,O

#La fonction mursH prends aucun paramétre. Elle retourne la 
#liste des numéros des murs horizontaux intérieurs de la grille 
#en faisant appelle à la fonction murs.
def mursH():
    global murH, N, S
    for i in N:
        if (i in S) == True:
            murH.append(i)
    return murH

#Cette fonction est similaire à mursH. Elle retourne la liste des murs 
#verticaux intérieurs.
def mursV():
    global murV, E, O
    for i in O:
        if (i in E) == True :
            murV.append(i)
    return murV

#La fonction voisins prends trois paramétres en compte : x et y qui 
#sont les coordonnées de la cellule dont on veut trouver les numéros des 
#cellules voisines ainsi que nX. Elle retourne une liste composée des 
#numéros des cellules voisines à la cellule (x,y).
def voisins(x,y,nX):
    global tableXY
    voisins=[]
    if [x,y-1] in tableXY:
        v4 = x+(y-1)*nX
        voisins.append(v4) 
    if [x-1,y] in tableXY:
        v2= (x-1)+y*nX
        voisins.append(v2)
    if [x,y+1] in tableXY:
        v3 = x+(y+1)*nX
        voisins.append(v3)
    if [x+1,y] in tableXY:
        v1 = (x+1)+y*nX
        voisins.append(v1) 
    return voisins


#Cette fonction prends deux paramétres en charge, soit une table et une valeur dont on
#veut trouver la position dans la table. Elle retourne un nombre qui est la position
#de la valeur dans la table. Le code de cette fonction provient des notes de cours de 
# IFT1015 et a été conçu par Marc Feeley qui en a permis l'usage.

def position(table,valeur):
    for position in range(len(table)) :
        if table[position] == valeur :
            return position



#La fonction verifierVoisin prends quatre nombres en paramétres, soit x et y 
#(les coordonnées de la cellule) et nX et nY. En faisant appelle à la fonction
#voisins, elle trouve les voisins de la cellule et vérifie ensuite si la
#liste cave (liste qui contient les numéros de cellule faisant partie de la cavité
#du labyrinthe) contient ces cellules. Si ce n'est pas le cas, elle ajoute le
#numéro de cellule à la liste front.

def verifierVoisin(x,y,nX,nY):
    global front, cave
    front.clear()
    v = voisins(x,y,nX,nY)
    for possibilite in range(0,len(v)):
        if contient(cave,v[possibilite]) == False:
            ajouter(front,v[possibilite])
    return front


#Cette fonction prends 4 nombres en paramètres : x, y, nX et nY.
#Elle va vérifier si le noombre de voisins à la cellule de
#coordonnée (x,y) donné en paramètre est suffisant (>0) pour
#choisir aléatoirement un mur à enlever en appelant la fonction
#décision mur. Si le nombre de voisin est 0, alors elle va
#chercher la première cellule dans "cave" qui a un nombre de voisin
#potentiel supérieure à 0, puis appeler decisionMur pour choisir
#le mur à enlever.

def choixMur(x,y,nX,nY) :
    global front, tableXY
    nbrVoisins = len(front)
    if nbrVoisins > 0 :
            decisionMur(x,y,nX,nY,nbrVoisins)
    if nbrVoisins == 0:
        for i in range(len(cave)-1,-1,-1):
            celPrecedente = tableXY[cave[i]]
            verifierVoisin(celPrecedente[0],celPrecedente[1],nX,nY)
            nbrVoisins = len(front)
            if nbrVoisins > 0 :
                decisionMur(celPrecedente[0],celPrecedente[1],nX,nY,nbrVoisins)
            else : continue


#Cette fonction prends 4 nombres en paramètre : la coordonnée (x,y) de 
#la cellule dont on veut enlever un mur. Elle choisit une cellule 
#voisine de cette dernière de manière aléatoire et va chercher le 
#numéro du mur qui les sépare et son type (Nord,Sud,Est ou Ouest) ainsi
#que la position de ce mur dans la liste murV ou murH selon qui contient
#le mur en question. Elle retourne ces 3 valeurs.

def decisionMur(x,y,nX,nbrVoisins):
    global typeMur, numMur, choix, front, tableXY, murV, murH, murChoisi
    choix = tableXY[front[math.floor(random()*nbrVoisins)]]
    print(choix)
    if choix[0] == x and choix[1] == y-1:                       
            murChoisi = x+y*nX 
            typeMur = 'nord'
            numMur = position(murH,murChoisi)
    elif choix[0] == x and choix[1] == y+1 :
            murChoisi = x+(y+1)*nX
            typeMur = 'sud'
            numMur = position(murH,murChoisi)
    elif choix[0] == x-1 and choix[1] == y: 
            murChoisi = x+y*(nX+1)
            typeMur = 'ouest'
            numMur = position(murV,murChoisi)
    elif choix[0] == x+1 and choix[1] == y:
            murChoisi = 1+x+y*(nX+1)
            typeMur = 'est'
            numMur = position(murV,murChoisi)
    return typeMur, numMur, choix, murChoisi


#Cette fonction prends un nombre "n" en paramètre et retourne une 
#liste qui commence à 0 jusqu'à "n" par bond de 1.

def iota(n):
    liste = []
    for i in range(n):
        liste.append(i)
    return liste


#Cette fonction prends 3 nombres en paramétres : nX, nY et largeurCase. Elle retourne
#deux listes (X et Y) qui sont respectivement composées de toute les valeurs que 
#peuvent prendre les coordonnées des pixels qui composent la grille en x et en y.à

def coordonneesPixels(nX,nY,largeurCase):
    global X,Y
    X=iota(nX*largeurCase+(nX+1))
    Y=iota(nY*largeurCase+(nY+1))
    return X,Y


#La fonction coordonneMurV prends trois nombres en paramétre (nX, nY et largeurCase).
#Elle retourne une liste de coordonnée (x,y) correspondant à la coordonnée du premier
#pixel de chaque mur vertical.

def coordonneMurV(nX,nY,largeurCase):
    coordonneesPixels(nX,nY,largeurCase)
    global coordonneeMurV
    for y in range(1,len(Y)-1,largeurCase+1):
        for x in range(largeurCase+1,len(X)-1,largeurCase+1):
            coordonneeMurV.append([x,y])
    return coordonneeMurV


#La fonction coordonneMurH prends trois nombres en paramétre (nX, nY et largeurCase).
#Elle retourne une liste de coordonnées (x,y) correspondant à la coordonnée du premier
#pixel de chaque mur horixontal.

def coordonneMurH(nX,nY,largeurCase):
    coordonneesPixels(nX,nY,largeurCase)
    global coordonneeMurH
    for y in range(largeurCase+1,len(Y)-1,largeurCase+1):
        for x in range(1,len(X)-1,largeurCase+1):
            coordonneeMurH.append([x,y])
    return coordonneeMurH


#Cette fonction prends deux nombres en paramétres (largeurCase et la 
#position, soit le numéro du mur à enlever). Elle permet de créer un passage 
#entre deux cellules voisines l'une au dessus de l'autre. C'est-à-dire 
#qu'elle supprime le mur horizontal se trouvant entre les deux cellules.

def creerPassageH(largeurCase,position):
    global coordonneeMurH
    murEnlever = coordonneeMurH[position]
    for x in range (murEnlever[0],murEnlever[0]+largeurCase):
        setPixel(x,murEnlever[1],struct(r=15,g=15,b=15))


#Cette fonction prends deux nombres en paramétres (largeurCase et la 
#position, soit le numéro du mur à enlever). Elle permet de créer un passage 
#entre deux cellules voisines l'une à côté de l'autre. C'est-à-dire 
#qu'elle supprime le mur vertical se trouvant entre les deux cellules.

def creerPassageV(largeurCase,position):
    global coordonneeMurV
    murEnlever = coordonneeMurV[position]
    for y in range (murEnlever[1],murEnlever[1]+largeurCase):
        setPixel(murEnlever[0],y,struct(r=15,g=15,b=15))
    

#Cette fonction prends trois paramètre en compte (nX,nY et largeurCase).
#Elle trace la grille rectangulaire de pixel noir, dont on va ajouter
#les murs horizontaux et verticaux par la suite.

def trace(nX,nY,largeurCase):
    setScreenMode(nX*largeurCase+(nX+1),nY*largeurCase+(nY+1))



#Cette fonction dessine la grille de pixel rectangulaire initialement pleine
#(avec tous les murs présent) qui va permettre de générer le labyrinthe.

def rectangle(nX,nY,largeurCase):  
    color(nX,nY,largeurCase)
    coteV(nX,nY,largeurCase)
    coteH(nX,nY,largeurCase)
    entree(nX,largeurCase)
    sortie(nX,nY,largeurCase)



#Cette fonction prends trois nombre en paramètre (nX,nY et largeurCase)
#et colorie l'intérieur du rectangle en blanc.

def color(nX,nY,largeurCase):
    trace(nX,nY,largeurCase)
    x = nX*largeurCase+nX
    y = nY*largeurCase+nY
    for i in range(1,x):
        for j in range(1,y):
            setPixel(i,j,struct(r=15,g=15,b=15))



#Cette fonction prends trois nombres en paramètre (nX,nY et largeurCase)
#et trace les murs verticaux à l'intérieur du rectangle initialment vide

def coteV(nX,nY,largeurCase):
    x = nX*largeurCase+nX
    y = nY*largeurCase+nY
    for i in range(0,x,largeurCase+1):
        for j in range(0,y):
            setPixel(i,j,struct(r=0,g=0,b=0))



#Cette fonction prends trois nombres en paramètre (nX,nY et largeurCase)
#et trace les murs horizontaux à l'intérieur du rectangle initialment vide.
            
def coteH(nX,nY,largeurCase):
    x = nX*largeurCase+nX
    y = nY*largeurCase+nY
    for k in range(0,y,largeurCase+1):
        for b in range(0,x):
            setPixel(b,k,struct(r=0,g=0,b=0))


#Cette fonction prends un nombre en paramètre (largeurCase)
#et créée l'entrée du labyrinthe.

def entree(largeurCase):
    for i in range(1,largeurCase+1):
        setPixel(i,0,struct(r=15,g=15,b=15))


#Cette fonction prends un nombre en paramètre (largeurCase)
#et créée la sortie du labyrinthe. 
   
def sortie(nX,nY,largeurCase):
    y = nY*largeurCase+nY
    x1 = (nX-1)*largeurCase+nX
    x2 = nX*largeurCase+nX
    for i in range(x1,x2):
        setPixel(i,y,struct(r=15,g=15,b=15))


#Cette fonction prends trois nombres en paramétres : nX, nY et largeurCase. 
#Elle permet de créer la cavité initiale du labyrinthe en choisissant la
#première cellule au hasard qui aura un de ses murs supprimés.

def celluleInitiale(nX,nY,largeurCase):
    global cave, N
    celInitiale = math.floor(random()*(len(N)))
    celInitialeXY = tableXY[celInitiale]
    verifierVoisin(celInitialeXY[0],celInitialeXY[1],nX,nY)
    choixMur(celInitialeXY[0],celInitialeXY[1],nX,nY)
    if typeMur == 'nord' or typeMur== 'sud' :
        creerPassageH(nX,nY,largeurCase,numMur)
    else : creerPassageV(nX,nY,largeurCase,numMur)
    ajouter(cave,celInitiale)
    return cave



#Cette fonction prends trois paramètres (nX,nY et largeurCase) et 
#trace un chemin de façon aléatoire grâce aux fonctions choixMur
#et verifierVoisin, ainsi que creerPassageH/V. Elle enléve les
#murs au fur et à mesure.

def creationChemin(nX,nY,largeurCase):
    global cave, murChoisi
    while len(cave)!=len(N):
        global choix
        celluleSuivante = choix
        ajouter(cave,position(tableXY,celluleSuivante))
        verifierVoisin(celluleSuivante[0],celluleSuivante[1],nX,nY)
        choixMur(celluleSuivante[0],celluleSuivante[1],nX,nY)
        if typeMur == 'nord' or typeMur == 'sud' :
            creerPassageH(nX,nY,largeurCase,numMur)
        else : 
            creerPassageV(nX,nY,largeurCase,numMur)
               

#Cette fonction prends trois nombres en paramètre : nX, nY et 
#largeurCase. Elle créée le labyrinthe en appelant les 
#différentes fonctions créées précédement.

def laby(nX, nY, largeurCase) :
    rectangle(nX,nY,largeurCase)
    murs(nX,nY); mursV(nX,nY); mursH(nX,nY)
    coordonneMurH(nX,nY,largeurCase); coordonneMurV(nX,nY,largeurCase)
    celluleInitiale(nX,nY,largeurCase)
    creationChemin(nX,nY,largeurCase)
