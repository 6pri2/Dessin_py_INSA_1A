from turtle import*

def parallelogramme (long,larg,angle,coul): #long, larg et angle de type entier et coul de type str
    #dessine un parallelogramme de longueur long et de largeur larg avec comme premier angle angle et de couleur coul
    color(coul)
    begin_fill()
    down()
    for i in range (2):
        forward(long)
        left(angle)
        forward(larg)
        left(180-angle)
    end_fill()
    up()

def rectangle (long,larg,coul): #long et larg de type entier et coul de type str
    #dessine un rectangle de longueur long et largeur larg de la couleur coul
    parallelogramme(long,larg,90,coul)
    

def carre(t,coul): #t type entier et coul type str
    #dessine un carré de coté t et de couleur coul
    rectangle(t,t,coul)

def rectangle_non_colorier(long,larg): #long et larg de type entier
    #dessine un rectangle non colorier exprès pour la tour de la mairie
    pensize(3)
    color("#a7967e")
    down()
    for _ in range (2):
        forward(long)
        left(90)
        forward(larg)
        left(90)
    up()

def arche_bas():
    #dessine l'arche du bas
    up()
    left(45)
    carre(30,"#a22430")
    for x in ["#ad0f61","#335577", "#d5a910", "#304146", "#c2551a", "#a22430", "#d5a910", "#a22430", "#304146", "#335577", "#5d893e", "#a22430", "#304146","#d5a910"]:
        forward(30)
        right (6.4)
        carre(30,x)
    forward(30)
    left(45)

def arche_haut_derriere() : 
    #dessine l'arche du haut, la partie en arrière plan
    up()
    x=89
    for k in ["#c2551a","#a22430","#335577","#304146","#d5a910","#5d893e","#a22430","#304146","#c2551a"]:
        parallelogramme(90,30,x,k)
        left(x)
        forward(32)
        right(x)
        x-=1
    parallelogramme(90,15,60,"#304146")

def arche_haut_devant() :
    #dessine la partie de devant de la seconde arche 
    x=91
    for c in ["#ad0f61", "#5d893e","#d5a910","#335577","#c2551a","#304146","#a22430","#d5a910","#ad0f61"]:
        parallelogramme(90,30,x,c)
        color("white")
        left(x)
        down()
        forward(32)
        up()
        right(x)
        x+=1
    parallelogramme(90,15,120,"#5d893e")
    color("white")
    left(120)
    down()
    forward(15)
    up()
    right(120)
    rectangle(90,2,"#a22430")

def tour_mairie():
    goto(150,-130)
    rectangle(60,250,"#cbbead") #ada08f
    goto(150,-130)
    rectangle_non_colorier(60,250)
    goto(165,-130)
    rectangle_non_colorier(30,250)
    goto(155,120)
    rectangle(50,50,"#cbbead")
    rectangle_non_colorier(50,50)
    goto(168,120)
    rectangle_non_colorier(24,50)
    goto(160,170)
    rectangle(40,20,"#cbbead")
    rectangle_non_colorier(40,20)
    goto(171,170)
    rectangle_non_colorier(18,20)
    goto(169,190)
    rectangle(21,35,"#cbbead")
    rectangle_non_colorier(21,35)
    goto(175,225)
    carre(10,"#cbbead")
    rectangle_non_colorier(10,10)
    goto(180,235)
    pensize(3)
    color("#cbbead")
    left(90)
    down()
    forward(15)
    up()
    right(90)

def immeuble():
    goto(-300,-175)
    rectangle(600,168,"#a7967e")
    goto(250,-7)
    rectangle(50,25,"#a7967e")
    #placement des fenetres
    for z in [-123,-94,-65,-36]:
        goto(-300,z)
        serie_fenetre()
    for x in [262,282]:
        goto(x,-7)
        fenetre()
    goto(-300,-175)
    rectangle(20,45,"black")
    for y in [-270,-213,-156,-99,-42,15,72,129,186,243]:
        goto(y,-175)
        fenetre_arche()
    goto(290,-175)
    rectangle(10,45,"black")
    goto(290,-175)
    left(90)
    down()
    color("white")
    forward(45)
    up()
    right(90)
    for k in [-126,-98,-69,-40,-11] :
        goto(-300,k)
        trait()
    goto(-295,-110)
    arche()

def trait():
    color("#D9C8B0")
    pensize(3)
    down()
    forward(600)
    up()
    pensize(1)


def fenetre(): #long et larg de type entier
    #dessine une fenetre de taille long x larg
    rectangle(16,21,"black")
    down()
    color("white")
    for _ in range (2):
        forward(16)
        left(90)
        forward(21)
        left(90)
    forward(8)
    left(90)
    forward(21)
    for _ in range (2) :
        backward(7)
        right(90)
        forward(8)
        backward(16)
        forward(8)
        left(90)
    backward(7)
    right(90)
    up()
    forward(8)

def serie_fenetre():
    #dessine une serie de 5 fenetre suivi d'un espace
    forward(2)
    for x in range(5):
        for _ in range (3) :
            fenetre()
            forward(4)
        forward(20)
        for _ in range(2):
            fenetre()
            forward(4)

def arche():
    down()
    pensize(10)
    color("#736D5A")
    forward(20)
    for _ in range(10):
        right(90)
        forward(70)
        backward(70)
        left(90)
        forward(57)
    up()
    pensize(1)

def fenetre_arche():
    down()
    rectangle(47,45,"black")
    color("white")
    for _ in range (2):
        forward(15)
        left(90)
        down()
        forward(45)
        backward(45)
        up()
        right(90)


    

#rectangle(120,90,"red")
#arche_bas()
up()
speed(1000)
#contour du cadre
goto(-307,-307)
carre(614,"#D79A10")
#on dessinera dans la partie du carré 300
#ciel
goto(-300,-300)
carre(600,"#96C3DC")
#mairie
tour_mairie()
pensize(1)
#immeuble
immeuble()
#digue :
goto(-300,-200)
rectangle(600,25,"#87816e")
#mer
goto(-300,-300)
rectangle(600,100,"#82A2CE")
#arche de contenaire :
goto(-125,-175)
arche_haut_derriere()
goto(-230,-175)
arche_bas()
goto(-55,-175)
arche_haut_devant()
#remise à la fin
color("black")
goto(307,-307)

input()

#taille 600 x 600, centre 0,0"""