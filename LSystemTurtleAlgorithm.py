# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 23:09:43 2017

@author: dualstream799
"""
# Importing libraries
from turtle import *
from random import randrange
# ----------------------------------------------- USER INTERACTIONS -------------------------------------------------- #

# Tutorial de comandos para o usuário
tutorial = ("""
Olá, bem vido ao Core Fractal, aqui você poderá criar seus próprios fractais de um jeito super simples !!!
Nosso programa entende os seguintes comandos:
  E = eita nóis
  D = diacho
  F = fi da mãe
  T = tá preula
Fácil, não? :)
""")
print(tutorial)
# Comandos inseridos pelo usuário
init_string = input("Digite os comandos que você quiser:\n")
back_string = input("Agora de novo, digite os dados que serão substituídos (pra dar uma emoção hehe):\n")
count = int(input("Digite o número de repetições (quantas vezes você vai iterar o código):\n"))

# ----------------------------------------- INITIALIZATING TURTLE ---------------------------------------------------- #

# Definindo 'cursor' como 'turtle.Turtle''
cursor = Turtle()
cursor.speed(0)

# -------------------------------------------- STRING CORRECTOR ------------------------------------------------------ #

# Deixando as strings minúsculas (reduz o banco de dados)
init_string = init_string.lower()
back_string = back_string.lower()

# ------------------------------------------- COLOR IMPLEMENTATION --------------------------------------------------- #

fill_colors = ["#17FF60", "#E89E0C", "#FF0036", "#260CE8", "#0DFFD7"]
fill_index = randrange(0, len(fill_colors))
cursor.fillcolor(fill_colors[fill_index])
dot_colors = ["#7F001B", "#40000E", "#FF0036"]
dot_index = randrange(0, len(dot_colors))
cursor.pencolor("purple")
# ------------------------------------------------ MAIN LOOP --------------------------------------------------------- #

# Loop para criar repetição de inserções (L System)
for i in range(count):
    # Condição para inserir uma string na outra

    if "f" in init_string:
        init_string = init_string.replace("f", back_string)
    # Loop que define cada comando para o Turtle
    for letter in init_string:
        if letter == "f":
            cursor.forward(50)
            cursor.right(45)
        elif letter == "t":
            cursor.backward(20)
            cursor.circle(15)
        elif letter == "e":
            cursor.left(60)
            cursor.fillcolor(fill_colors[fill_index])
            cursor.stamp()
        elif letter == "d":
            cursor.right(60)
        else:
            cursor.right(90)
            cursor.forward(10)
            cursor.dot(1, dot_colors[dot_index])

    print(init_string)
done()
