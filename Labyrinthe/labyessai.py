#Je me base sur l'idée d'un labyrinthe par exploration exhaustive de wikipédia

import math
import random

X=None; Y=None

N=[]; E=[]; S=[]; O=[]

murH=[]; murV=[]; coordonneeMurH=[]; coordonneeMurV=[]

tableXY = []

front = []; celChoisi = []; cave=[]; celluleSuivante=[]

typeMur=''; numMur = 0


def contient(tab,x):
    for i in range(len(tab)):
        if tab[i]==x:
            return True
    return False

def ajouter(tab,x):
    if contient(tab,x):
        return tab
    else:
        tab.append(x)
        return tab

def retirer(tab,x):
    if contient(tab,x):
        tab.remove(x)
        return tab
    else:
        return tab

def nombre(nX,nY):
    global tableXY
    for i in range(nY):
        for j in range(nX):
            tableXY.append([j,i])
    return tableXY

def murs(nX,nY): 
    nombre(nX,nY)
    global N,S,E,O
    for i in range(len(tableXY)):
            N.append(tableXY[i][0]+tableXY[i][1]*nX)
            E.append(1+tableXY[i][0]+tableXY[i][1]*(nX+1))
            S.append(tableXY[i][0]+(tableXY[i][1]+1)*nX)
            O.append(tableXY[i][0]+tableXY[i][1]*(nX+1))
    return N,E,S,O


def mursH(nX,nY):
    murs(nX,nY)
    global murH
    for i in N:
        if (i in S) == True:
            murH.append(i)
    return murH

def mursV(nX,nY):
    murs(nX,nY)
    global murV
    for i in O:
        if (i in E) == True :
            murV.append(i)
    return murV

def voisins(x,y,nX,nY):
    murs(nX,nY)
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

def position(table,valeur):
    for position in range(len(table)) :
        if table[position] == valeur :
            return position

def verifierVoisin(x,y,nX,nY):
    global front
    v = voisins(x,y,nX,nY)
    for choix in range(0,len(v)):
        if contient(cave,v[choix]) == False:
            ajouter(front,v[choix])
    return front

def choixMur(x,y,nX,nY) :
    global typeMur, numMur, celluleSuivante
    verifierVoisin(x,y,nX,nY)
    nbrVoisins = len(front)                                         #trouve les voisins
    if len(front) >= 1 :
        choix = tableXY[front[math.floor(random()*nbrVoisins)]]     #choisi le voisin et donne son numéro de cellule          
        celluleSuivante = choix
        if choix[0] == x and choix[1] == y-1:                                    #on cherche le mur entre la cellule et sa voisine
            murChoisi = x+y*nX 
            typeMur = 'nord'
            numMur = position(mursH(nX,nY),murChoisi)
            return typeMur, numMur, celluleSuivante
        elif choix[0] == x and choix[1] == y+1 :
            murChoisi = x+(y+1)*nX
            typeMur = 'sud'
            numMur = position(mursH(nX,nY),murChoisi)
            return typeMur, numMur, celluleSuivante
        elif choix[0] == x-1 and choix[1] == y: 
            murChoisi = x+y*(nX+1)
            typeMur = 'ouest'
            numMur = position(mursV(nX,nY),murChoisi)
            return typeMur, numMur, celluleSuivante
        elif choix[0] == x+1 and choix[1] == y:
            murChoisi = 1+x+y*(nX+1)
            typeMur = 'est'
            numMur = position(mursV(nX,nY),murChoisi)
            return typeMur, numMur, celluleSuivante    
    else :
        for i in range(len(cave)-1,-1,-1):
            cellulePrecedente = cave[i]
            choixMur(cellulePrecedente[0],cellulePrecedente[1],nX,nY)


def iota(n):
    liste = []
    for i in range(n):
        liste.append(i)
    return liste

def coordonneesPixels(nX,nY,largeurCase):
    global X,Y
    X=iota(nX*largeurCase+(nX+1))
    Y=iota(nY*largeurCase+(nY+1))
    return X,Y

def coordonneMurV(nX,nY,largeurCase):
    coordonneesPixels(nX,nY,largeurCase)
    global coordonneeMurV
    for y in range(1,len(Y)-1,largeurCase+1):
        for x in range(largeurCase+1,len(X)-1,largeurCase+1):
            coordonneeMurV.append([x,y])
    return coordonneeMurV
            
def coordonneMurH(nX,nY,largeurCase):
    coordonneesPixels(nX,nY,largeurCase)
    global coordonneeMurH
    for y in range(largeurCase+1,len(Y)-1,largeurCase+1):
        for x in range(1,len(X)-1,largeurCase+1):
            coordonneeMurH.append([x,y])
    return coordonneeMurH

def creerPassageH(nX,nY,largeurCase,position):
    murEnlever = coordonneMurH(nX,nY,largeurCase)[position]
    for x in range (murEnlever[0],murEnlever[0]+largeurCase):
        setPixel(x,murEnlever[1],struct(r=15,g=15,b=15))
    retirer(coordonneeMurH,murEnlever)


def creerPassageV(nX,nY,largeurCase,position):
    murEnlever = coordonneMurV(nX,nY,largeurCase)[position]
    for y in range (murEnlever[1],murEnlever[1]+largeurCase):
        setPixel(murEnlever[0],y,struct(r=15,g=15,b=15))
    retirer(coordonneeMurV,murEnlever)

def trace(nX,nY,largeurCase):
    setScreenMode(nX*largeurCase+(nX+1),nY*largeurCase+(nY+1))

#Fonction qui dessine la grille de pixel rectangulaire initialement pleine
#afin de générer le labyrinthe
def rectangle(nX,nY,largeurCase):  
    color(nX,nY,largeurCase)
    coteV(nX,nY,largeurCase)
    coteH(nX,nY,largeurCase)
    entree(nX,largeurCase)
    sortie(nX,nY,largeurCase)

def color(nX,nY,largeurCase):
    trace(nX,nY,largeurCase)
    x = nX*largeurCase+nX
    y = nY*largeurCase+nY
    for i in range(1,x):
        for j in range(1,y):
            setPixel(i,j,struct(r=15,g=15,b=15))
                        
def coteV(nX,nY,largeurCase):
    x = nX*largeurCase+nX
    y = nY*largeurCase+nY
    for i in range(0,x,largeurCase+1):
        for j in range(0,y):
            setPixel(i,j,struct(r=0,g=0,b=0))
            
def coteH(nX,nY,largeurCase):
    x = nX*largeurCase+nX
    y = nY*largeurCase+nY
    for k in range(0,y,largeurCase+1):
        for b in range(0,x):
            setPixel(b,k,struct(r=0,g=0,b=0))

def entree(nX,largeurCase):
    for i in range(1,largeurCase+1):
        setPixel(i,0,struct(r=15,g=15,b=15))
        
def sortie(nX,nY,largeurCase):
    y = nY*largeurCase+nY
    x1 = (nX-1)*largeurCase+nX
    x2 = nX*largeurCase+nX
    for i in range(x1,x2):
        setPixel(i,y,struct(r=15,g=15,b=15))

def celluleInitiale(nX,nY,largeurCase):
    murs(nX,nY)
    global cave
    celInitiale = math.floor(random()*(len(N)))
    print(celInitiale)
    celInitialeXY = tableXY[celInitiale]
    print(celInitialeXY)
    choixMur(celInitialeXY[0],celInitialeXY[1],nX,nY)
    if typeMur == 'nord' or typeMur== 'sud' :
        creerPassageH(nX,nY,largeurCase,numMur)
    else : creerPassageV(nX,nY,largeurCase,numMur)
    ajouter(cave,celInitiale)
    return cave

def laby(nX, nY, largeurCase) :
    rectangle(nX,nY,largeurCase)
    celluleInitiale(nX,nY,largeurCase)
   
    while len(cave) <= (nX*nY)-2 :
        choixMur(celluleSuivante[0],celluleSuivante[1],nX,nY)
        if typeMur == 'nord' or typeMur == 'sud' :
            creerPassageH(nX,nY,largeurCase,numMur)
        else : creerPassageV(nX,nY,largeurCase,numMur)
        ajouter(cave,celluleSuivante)



    
       

