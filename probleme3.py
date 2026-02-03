import turtle
import random
ecran = turtle.Screen()
ecran.bgcolor("white")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
def dessiner_carre(taille):
    for _ in range(4):
        t.forward(taille)
        t.right(90)
def dessiner_triangle(taille):
    for _ in range(3):
        t.forward(taille)
        t.left(120)
def dessiner_cercle(taille):
    t.circle(taille)

N = int(input("Entrez un nombre entier entre 0 et 9 : "))
for _ in range(N):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    t.penup()
    t.goto(x, y)
    t.pendown()

    r = random.random()
    g = random.random()
    b = random.random()
    t.color(r, g, b)

    taille = random.randint(20, 400)

    forme = random.choice(["carre", "triangle", "cercle"])

    if forme == "carre":
        dessiner_carre(taille)
    elif forme == "triangle":
        dessiner_triangle(taille)
    else:
        dessiner_cercle(taille)

