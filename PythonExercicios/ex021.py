'''Exercício Python 21: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.'''
import pygame

pygame.init()
pygame.mixer.music.load('ex021.mp3')

pygame.mixer.music.play()
input()
pygame.event.wait()


# import pygame

# # Inicializando o mixer PyGame
# pygame.mixer.init()

# # Iniciando o Pygame
# pygame.init()

# pygame.mixer.music.load('ex021.mp3')
# pygame.mixer.music.play(loops=0, start=0.0)
# pygame.event.wait()
#========================================================================================

# import playsound
# playsound.playsound('ex021.mp3')
'''pygame.quit
import pygame

pygame.init()

try:
    pygame.mixer.music.load('ex021.mp3')
    pygame.mixer.music.play()
except pygame.error:
    print("Arquivo de áudio 'ex021.mp3' não encontrado.")

input("Aperte enter para sair...")
pygame.quit()'''

