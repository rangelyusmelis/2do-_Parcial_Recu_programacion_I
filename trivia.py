from funciones_trivia import *
import pygame
import pygame.mixer as mixer
# inicializo pygame


pygame.init()
lista_elementos = []
parse_csv(lista_elementos, "preguntas.csv")
# creo la pantalla principal *
pantalla = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Trivia Mix")

# cargo la musica
mixer.music.load(
    "C:/Users/ryusm/OneDrive/Desktop/Programacion 08/2do-_Parcial_Recu_programacion_I/musica.mp3")
mixer.music.set_volume(0.100)
mixer.music.play()
# Cargo imagenes
trivia_mix = pygame.image.load(
    "C:/Users/ryusm/OneDrive/Desktop/Programacion 08/2do-_Parcial_Recu_programacion_I/trivia_mix.png")

# escalar la imagen
trivia_mix = pygame.transform.scale(trivia_mix, (100, cd100))

# colores

colo_de_fondo = (127, 130, 187,)
color_amarillo = (255, 249, 107)
# dibujar rectangulo para menu


coordenadas = (100, 200, 200, 50)
pygame.draw.rect(pantalla, color_amarillo, coordenadas)
# bucle principal del juego


# sonido = mixer.sound(ruta_al_audio)
# sonido.set_volume(0.4)
# sonido.play()

while True:

    # getionamos eventos (cierre de ventana)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()

    # actualizo el juego

    # dibujar en pantalla
    pantalla.fill(colo_de_fondo)
    pantalla.blit(trivia_mix, (150, 70))
    # actualizamos pantalla
    pygame.display.flip()

pygame.quit()
