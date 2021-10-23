#Auteurs : Louis Duong et Romy Mahieu
#Date de création : 24 octobre 2021

#Ce programme crée un labyrinthe rectangulaire aléatoire qui posséde une solution unique

tableXY=[]
N=[]
E=[]
S=[]
O=[]

X=None
Y=None

murH=[]
murV=[]

cavite=[]
front=[]

#Fonction qui crée une liste de nombre de 0 à n-1
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

#print(coordonnees(3,3,3))

#Fonction qui vérifie si une valeur x est dans la table
def contient(tab,x):
    for i in range(len(tab)):
        if tab[i]==x:
            return True
    return False

#Fonction qui vérifie si une valeur x est dans la table, et si elle n'y est pas, l'ajoute à la fin
def ajouter(tab,x):
    if contient(tab,x):
        return tab
    else:
        tab.append(x)
        return tab

#Fonction qui vérifie si une valeur x est dans la table, et la retire si elle s'y trouve
def retirer(tab,x):
    if contient(tab,x):
        tab.remove(x)
        return tab
    else:
        return tab

#Fonction qui crée la liste des coordonnées (x,y) des cases de la grille
#qui va servir à créer le labyrinthe
def nombre(x,y):
    global tableXY
    for i in range(y):
        for j in range(x):
            tableXY.append([j,i])
    return tableXY

 
#Valeurs des murs Nord, Est, Sud et Ouest
def murs(x,y): 
    nombre(x,y)
    #print(tableXY)
    global N,S,E,O
    for i in range(len(tableXY)):
            N.append(tableXY[i][0]+tableXY[i][1]*x)
            E.append(1+tableXY[i][0]+tableXY[i][1]*(x+1))
            S.append(tableXY[i][0]+(tableXY[i][1]+1)*x)
            O.append(tableXY[i][0]+tableXY[i][1]*(x+1))
    return N,E,S,O
#print(murs(3,3))

#Sépare les coordonnées x et y des cases du labytinthe en deux listes respectives
def coordonnéesCases(x,y):
    murs(x,y)
    caseX=[]
    caseY=[]
    for i in range(x):
        caseX.append(tableXY[i][0])
    for i in range(0,len(N),x):
        caseY.append(tableXY[i][1])
    return caseX,caseY
print(coordonnéesCases(3,3))

#Donne la liste des numéros de cellules voisines à (x,y)
def voisin(x,y,nX,nY):
    nombre(nX,nY)
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
#print(voisin(1,1,3,3))

def mursH():
    global murH
    for i in range(len(N)):
        murH.append(N[i])
    for j in S:
        if (j in N) == False:
            murH.append(j)
    return murH


def mursV():
    global murV
    for i in O:
        murV.append(i)
    for j in E:
        if (j in O) == False:
            murV.append(j)
    for i in range(1, len(murV)): 
        k = murV[i] 
        j = i-1
        while j >= 0 and k < murV[j] : 
                murV[j + 1] = murV[j] 
                j -= 1
        murV[j + 1] = k
    return murV

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
    sup(nX,nY,largeurCase) 

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
        
def cave(x,y):
    murs(x,y)
    mursH()
    mursV()
    global cavite, front
    X = tableXY[(math.floor(random()*(len(N)-1)))]
    if X== tableXY[x-1][0] and X== tableXY[x-1][1]:
        ajouter(cavite,tableXY[(math.floor(random()*(len(N)-1)))])
        ajouter(front,voisin(cavite[0][0],cavite[0][1],x,y))
    for j in range(x):
        for i in range(len(cavite)):
            retirer(N,cavite[i][0]+cavite[i][1]*x)
            retirer(murH,cavite[i][0]+cavite[i][1]*x)
            retirer(murV,cavite[i][0]+cavite[i][1]*x)
            retirer(tableXY, cavite[i])
        if X!= tableXY[x-1][0] and X!= tableXY[x-1][1]:
            v=front[(math.floor(random()*(len(front)-1)))][(math.floor(random()*(len(front)-1)))] 
            cavite.append(tableXY[v]) 
        
    return cavite,N

def coordonneMurV(nX,nY,largeurCase):
    coordonnees(nX,nY,largeurCase)
    coordonneMurV=[]
    for y in range(1,len(Y)-1,largeurCase+1):
        for x in range(largeurCase+1,len(X)-1,largeurCase+1):
            coordonneMurV.append([x,y])
    return coordonneMurV
            
def coordonneMurH(nX,nY,largeurCase):
    coordonnees(nX,nY,largeurCase)
    coordonneMurH=[]
    for y in range(largeurCase+1,len(Y)-1,largeurCase+1):
        for x in range(1,len(X)-1,largeurCase+1):
            coordonneMurH.append([x,y])
    return coordonneMurH

def creerPassageH(nX,nY,largeurCase):
    mur = math.floor(random()*(len(coordonneMurH(nX,nY,largeurCase))))
    murEnlever = coordonneMurH(nX,nY,largeurCase)[mur]
    for x in range (murEnlever[0],murEnlever[0]+largeurCase):
        setPixel(x,murEnlever[1],struct(r=15,g=15,b=15))
    return murEnlever

def creerPassageV(nX,nY,largeurCase):
    mur = math.floor(random()*(len(coordonneMurV(nX,nY,largeurCase))))
    murEnlever = coordonneMurV(nX,nY,largeurCase)[mur]
    for y in range (murEnlever[1],murEnlever[1]+largeurCase):
        setPixel(murEnlever[0],y,struct(r=15,g=15,b=15))
    return murEnlever

def sup(nX,nY,largeurCase):
    cave(nX,nY)
    for i in range(len(cavite)):
        setPixel(cavite[i][0],cavite[i][1],struct(r=15,g=15,b=15))


def laby(nX,nY,largeurCase):
    rectangle(nX,nY,largeurCase)
    
#Test les fonctions
def test(): 
    assert iota(4)== [0,1,2,3]
    assert contient([1,2,3],3) == True
    assert contient([1,2,3,4],5) == False
    assert ajouter([1,2,3],4) == [1,2,3,4]
    assert retirer([1,2,3,4],4) == [1,2,3]