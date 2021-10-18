import turtle as tr

# #Dessine un rectangle
# def rectangle(x,y,z):
#     for _ in range(2):
#         tr.fd((x-1)*z)
#         tr.penup()
#         tr.fd(z)
#         tr.pendown()
#         tr.lt(90)
#         tr.fd(y*z)
#         tr.lt(90)

# #Dessine les colonnes
# def largeur(x,y,z):
#     for _ in range(x-1):
#         tr.penup()
#         tr.fd(z)
#         tr.left(90)
#         tr.pendown()
#         tr.forward(y*z)
#         tr.penup()
#         tr.left(180)
#         tr.fd(y*z)
#         tr.pendown()
#         tr.left(90)

# def hauteur(x,y,z):
#     tr.penup()
#     tr.goto(0,0)
#     tr.left(90)
#     for _ in range(y-1):
#         tr.fd(z)
#         tr.right(90)
#         tr.pendown()
#         tr.fd(x*z)
#         tr.penup()
#         tr.right(180)
#         tr.fd(x*z)
#         tr.right(90)

    
# #Dessine la grille       
# def grille(nX,nY,largeurCase):
#     rectangle(nX,nY,largeurCase)
#     largeur(nX,nY,largeurCase)
#     hauteur(nX,nY,largeurCase)

# grille(8,4,20)


def carre(x):
    for _ in range(4):
        tr.fd(x)
        tr.lt(90)
        tr.fd(x)

def carreBlanc(x):
    carre(x)
    tr.color("white")
    for _ in range(4):
        tr.fd(x)
        tr.lt(90)
        tr.fd(x)

carreBlanc(90)

tr.mainloop()