import turtle as tr 
#jai importer turtle

tableXY=[]
N=[]
E=[]
S=[]
O=[]

X=[]
Y=[]

#Sort une liste alant de 0 a n-1
def iota(n):
    liste = []
    for i in range(n):
        liste.append(i)
    return liste

#Verifier si valeur dans liste
def contient(tab,x):
    for i in range(len(tab)):
        if tab[i]==x:
            return True
    return False

#Ajoute une valeur dans fin tab si exsite pas
def ajouter(tab,x):
    if contient(tab,x):
        return tab
    else:
        tab.append(x)
        return tab

#Retire x si il est dans le tableau
def retirer(tab,x):
    if contient(tab,x):
        tab.remove(x)
        return tab
    else:
        return tab

#Donne toutes les coordonnees x,y
def nombre(x,y):
    global tableXY
    for i in range(y):
        for j in range(x):
            tableXY.append([j,i])
    return tableXY

#Valeurs de N,E,S,O
def murs(x,y):
    nombre(x,y)
    global N,S,E,O
    for i in range(len(tableXY)):
            N.append(tableXY[i][0]+tableXY[i][1]*x)
            E.append(1+tableXY[i][0]+tableXY[i][1]*x)
            S.append(tableXY[i][0]+(tableXY[i][1]+1)*x)
            O.append(tableXY[i][0]+tableXY[i][1]*(x+1))

#Donne valeur de x puis de y
def XY(x,y):
    murs(x,y)
    for i in range(x):
        X.append(tableXY[i][0])
    for i in range(0,len(N),8):
        Y.append(tableXY[i][1])
    return X,Y

#Verifie les voisins
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

def mursH(x,y):
    murs(x,y)
    murH=[]
    print(N)
    print(S)
    for i in range(len(N)):
        murH.append(N[i])
    print(murH)
    for i in range(len(N)):
        if N[i] in S:
            S.pop(N[i])
    return murH

print(mursH(8,4))

#Test les fonction
def test():
    assert iota(4)== [0,1,2,3]
    assert contient([1,2,3],3) == True
    assert contient([1,2,3,4],5) == False
    assert ajouter([1,2,3],4) == [1,2,3,4]
    assert retirer([1,2,3,4],4) == [1,2,3]

#Dessine un rectangle
def rectangle(x,y,z):
    for _ in range(2):
        tr.fd((x-1)*z)
        tr.penup()
        tr.fd(z)
        tr.pendown()
        tr.lt(90)
        tr.fd(y*z)
        tr.lt(90)

#Dessine les colonnes
def largeur(x,y,z):
    for _ in range(x-1):
        tr.penup()
        tr.fd(z)
        tr.left(90)
        tr.pendown()
        tr.forward(y*z)
        tr.penup()
        tr.left(180)
        tr.fd(y*z)
        tr.pendown()
        tr.left(90)

def hauteur(x,y,z):
    tr.penup()
    tr.goto(0,0)
    tr.left(90)
    for _ in range(y-1):
        tr.fd(z)
        tr.right(90)
        tr.pendown()
        tr.fd(x*z)
        tr.penup()
        tr.right(180)
        tr.fd(x*z)
        tr.right(90)

    
#Dessine la grille       
def grille(nX,nY,largeurCase):
    rectangle(nX,nY,largeurCase)
    largeur(nX,nY,largeurCase)
    hauteur(nX,nY,largeurCase)

def blanc(x,y,z):
    grille(x,y,z)
    tr.pendown()
    tr.color("white")
    tr.fd(z)

# tr.mainloop()