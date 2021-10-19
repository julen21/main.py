# Import a library of functions called 'pygame'
import pygame
from main_functions import *

# Initialize the game engine
pygame.init()

#call main routine
ancho= int(input("Ancho de la ventana: "))
alto= int(input("alto de la ventana: "))
size=[1300,600]
size[0]=ancho
size[1]=alto
size = (ancho, alto)
color = (0, 255, 0)
título = input("titulo: ")
main2(size, título, color)