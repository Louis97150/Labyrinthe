X=None; Y=None

N=[]; E=[]; S=[]; O=[]

murH=[]; murV=[]; coordonneeMurH=[]; coordonneeMurV=[]

tableXY = []

front = []; celChoisi = []; cave=[]; choix=[]

typeMur=''; numMur = 0

#La fonction contient vérifie si la valeur "x" se trouve dans la table. Elle retourne un booléen 
#selon si la table contient ou non la valeur "x"
def contient(tab,x):
    for i in range(len(tab)):
        if tab[i]==x:
            return True
    return False

#Cette fontion vérifie d'abord si la table contient déjà la valeur "x". Si ce n'est pas le cas, 
#elle ajoute la valeur à la fin de la table
def ajouter(tab,x):
    if contient(tab,x):
        return tab
    else:
        tab.append(x)
        return tab

#Cette fonction vérifie d'abord si la table contient la valeur "x". Si c'est le cas, elle
#retire "x" de la table.
def retirer(tab,x):
    if contient(tab,x):
        tab.remove(x)
        return tab
    else:
        return tab

#Cette fonction créée la liste des coordonnées (x,y) des cellules de la grille qui vont servir
#à créer le labyrinthe. Pour cela, elle prends deux nombres, soit nX (la longueur de la grille) 
#et nY (la hauteur de la grille).
def nombre(nX,nY):
    global tableXY
    for i in range(nY):
        for j in range(nX):
            tableXY.append([j,i])
    return tableXY

#La fonction murs prends deux paramétres en compte (nX et nY) et appelle la fonction nombre(x,y) 
#afin de retourne une liste pour chaque type de mur d'une cellule. Il s'agit de la liste des murs
#nord, est, sud et ouest pour chaque cellule.
def murs(nX,nY): 
    nombre(nX,nY)
    global N,S,E,O
    for i in range(len(tableXY)):
            N.append(tableXY[i][0]+tableXY[i][1]*nX)
            E.append(1+tableXY[i][0]+tableXY[i][1]*(nX+1))
            S.append(tableXY[i][0]+(tableXY[i][1]+1)*nX)
            O.append(tableXY[i][0]+tableXY[i][1]*(nX+1))
    return N,E,S,O

#La fonction mursH prends aussi deux nombres en paramétre qui sont nX et nY. Elle retourne la liste 
#des numéros des murs horizontaux intérieurs de la grille en faisant appelle à la fonction murs.
def mursH(nX,nY):
    global murH, N, S
    for i in N:
        if (i in S) == True:
            murH.append(i)
    return murH

#Cette fonction prends les mêmes paramétres que la fonction mursH et réalise la même chose, sauf que 
#ce sont la liste des murs verticaux intérieurs qui est retournée.
def mursV(nX,nY):
    global murV, E, O
    for i in O:
        if (i in E) == True :
            murV.append(i)
    return murV

#La fonction voisins prends quatre paramétres en compte : x et y qui sont les coordonnées de la cellule
#dont on veut trouver les numéros des cellules voisines ainsi que nX et nY. Elle retourne une liste
#composée des numéros des cellules voisines à la cellule (x,y).
def voisins(x,y,nX,nY):
    nombre(nX,nY)
    voisin=[]
    if [x,y-1] in tableXY:
        v4 = x+(y-1)*nX
        voisin.append(v4) 
    if [x-1,y] in tableXY:
        v2= (x-1)+y*nX
        voisin.append(v2)
    if [x,y+1] in tableXY:
        v3 = x+(y+1)*nX
        voisin.append(v3)
    if [x+1,y] in tableXY:
        v1 = (x+1)+y*nX
        voisin.append(v1) 
    return voisin


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
    print(cave)
    front.clear()
    v = voisins(x,y,nX,nY)
    for possibilite in range(0,len(v)):
        if contient(cave,tableXY[v[possibilite]]) == False:
            ajouter(front,v[possibilite])
    print(front)
    return front

print(voisins(3,3,3,3))


def choixMur(x,y,nX,nY) :
    global front
    print(front)
    print(cave)
    nbrVoisins = len(front)
    if nbrVoisins != 0 :
            decisionMur(x,y,nX,nY,nbrVoisins)
    else :
        for i in range(len(cave)-1,-1,-1):
            cellulePrecedente = cave[i]
            verifierVoisin(cellulePrecedente[0],cellulePrecedente[1],nX,nY)
            if len(front) != 0 :
                decisionMur(x,y,nX,nY,nbrVoisins)

def decisionMur(x,y,nX,nY,nbrVoisins):
    global typeMur, numMur, choix, front, tableXY, murV, murH
    print(murV), print(murH)
    choix = tableXY[front[math.floor(random()*nbrVoisins)]]
    print(choix)
    if choix[0] == x and choix[1] == y-1:                       #on cherche le mur entre la cellule et sa voisine
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
    print(numMur)
    return typeMur, numMur, choix

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


def coordonneMurH(nX,nY,largeurCase):
    coordonneesPixels(nX,nY,largeurCase)
    global coordonneeMurH
    for y in range(largeurCase+1,len(Y)-1,largeurCase+1):
        for x in range(1,len(X)-1,largeurCase+1):
            coordonneeMurH.append([x,y])
    return coordonneeMurH


#Cette fonction prends quatre nombres en paramétres (nX, nY, largeurCase et la 
#position, soit le numéro du mur à enlever. Elle permet de créer un passage 
#entre deux cellules voisines. C'est-à-dire qu'elle supprime le mur se trouvant 
#entre deux cellules.

def creerPassageH(nX,nY,largeurCase,position):
    coordonneMurH(nX,nY,largeurCase)
    print(coordonneeMurH)
    print(position)
    murEnlever = coordonneeMurH[position]
    for x in range (murEnlever[0],murEnlever[0]+largeurCase):
        setPixel(x,murEnlever[1],struct(r=15,g=15,b=15))


def creerPassageV(nX,nY,largeurCase,position):
    coordonneMurV(nX,nY,largeurCase)
    print(coordonneeMurV)
    print(position)
    murEnlever = coordonneeMurV[position]
    for y in range (murEnlever[1],murEnlever[1]+largeurCase):
        setPixel(murEnlever[0],y,struct(r=15,g=15,b=15))
    

def trace(nX,nY,largeurCase):
    setScreenMode(nX*largeurCase+(nX+1),nY*largeurCase+(nY+1))


#Cette fonction dessine la grille de pixel rectangulaire initialement pleine
#qui va permettre de générer le labyrinthe.
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


#Cette fonction prends trois nombres en paramétres : nX, nY et largeurCase. 
#Elle permet de créer la cavité initiale du labyrinthe en choisissant la
#première cellule au hasard qui aura un de ses murs supprimés.

def celluleInitiale(nX,nY,largeurCase):
    global cave, N
    celInitiale = math.floor(random()*(len(N)))
    celInitialeXY = tableXY[celInitiale]
    print(celInitialeXY)
    verifierVoisin(celInitialeXY[0],celInitialeXY[1],nX,nY)
    choixMur(celInitialeXY[0],celInitialeXY[1],nX,nY)
    if typeMur == 'nord' or typeMur== 'sud' :
        creerPassageH(nX,nY,largeurCase,numMur)
    else : creerPassageV(nX,nY,largeurCase,numMur)
    ajouter(cave,celInitiale)
    print(cave)
    return cave

def creationChemin(nX,nY,largeurCase):
    global cave
    repeter = True
    while repeter :
        global choix
        celluleSuivante = choix
        print(celluleSuivante)
        verifierVoisin(celluleSuivante[0],celluleSuivante[1],nX,nY)
        choixMur(celluleSuivante[0],celluleSuivante[1],nX,nY)
        if typeMur == 'nord' or typeMur == 'sud' :
            creerPassageH(nX,nY,largeurCase,numMur)
        else : creerPassageV(nX,nY,largeurCase,numMur)
        ajouter(cave,position(tableXY,celluleSuivante))
        if contient(cave,0)==True and contient(cave,len(N)-1)==True:
            repeter = False

def laby(nX, nY, largeurCase) :
    rectangle(nX,nY,largeurCase)
    murs(nX,nY); mursV(nX,nY); mursH(nX,nY)
    print(murV, murH)
    celluleInitiale(nX,nY,largeurCase)
    creationChemin(nX,nY,largeurCase)