from funciones_trivia import *
from Constantes import *

flag_jugar = False
flag_json = False
lista_elementos = []
lista_rankings = [{"nombre": "Juan", "puntuacion": 600, "fecha": "25/06/2024"},
                  {"nombre": "Maria", "puntuacion": 100,"fecha": "25/07/2024"},
                  {"nombre": "Julio", "puntuacion": 500,"fecha": "25/08/2024"}
                  ]

leer_csv_preguntas(
    "C:/Users/ryusm/OneDrive/Desktop/Programacion 08/2do-_Parcial_Recu_programacion_I/preguntas.csv", lista_elementos)
while (True):
    datos_juego = {"puntuacion": 0, "vidas": CANTIDAD_VIDAS, "nombre": ""}
    opcion = ejecutar_menu()
    if opcion == 1:

        print(f"VIDAS RESTANTES {datos_juego["vidas"]}")

        mezclar_lista(lista_elementos)

        jugar_preguntados_por_consola(datos_juego, lista_elementos)

        print(f"JUEGO TERMINADO\n PUNTUACION FINAL {datos_juego['puntuacion']}"
              )
        flag_jugar = True

    if opcion == 2:
        if flag_jugar == True:
            datos_juego["nombre"] = input("ingrese el nombre del jugador")

            print(f"JUGADOR {datos_juego["nombre"]}")

            guardar_puntuacion_lista(lista_rankings, datos_juego)
            ordenar_puntaciones(lista_rankings, "puntuacion")
            generar_json("partidas.json", lista_rankings)

            flag_json = True
        else:
            print("primero deberas jugar")

    if opcion == 3:
        if flag_json == True:
            mostrar_rankings(lista_rankings[0:10])

        else:
            print(" primero deberas jugar y cdar fin a la partida")
            pass
    reiniciar_estadisticas(datos_juego)

# import pygame
# import pygame.mixer as mixer
# inicializo pygame


# pygame.init()


# # creo la pantalla principal *
# pantalla = pygame.display.set_mode((400, 600))
# pygame.display.set_caption("Trivia Mix")

# # cargo la musica
# mixer.music.load(
#     "C:/Users/ryusm/OneDrive/Desktop/Programacion 08/2do-_Parcial_Recu_programacion_I/musica.mp3")
# mixer.music.set_volume(0.100)
# mixer.music.play()

# # Cargo imagenes
# trivia_mix = pygame.image.load(
#     "C:/Users/ryusm/OneDrive/Desktop/Programacion 08/2do-_Parcial_Recu_programacion_I/trivia_mix.png")

# # escalar la imagen
# trivia_mix = pygame.transform.scale(trivia_mix, (100, 100))

# # colores

# colo_de_fondo = (127, 130, 187,)
# color_amarillo = (255, 249, 107)
# colo_negro = (0, 0, 0)
# # dibujar rectangulo para menu


# coordenadas = (100, 200, 200, 50)
# pygame.draw.rect(pantalla, color_amarillo, coordenadas)
# # bucle principal del juego

# # Texto
# fuente = pygame.font.SysFont("Arial", 25)
# texto = fuente.render(f" {lista_elementos}", False, colo_negro)

# # sonido = mixer.sound(ruta_al_audio)
# # sonido.set_volume(0.4)
# # sonido.play()

# while True:

#     # getionamos eventos (cierre de ventana)
#     for evento in pygame.event.get():
#         if evento.type == pygame.QUIT:
#             pygame.quit()
#             quit()

#     # actualizo el juego

#     # dibujar en pantalla
#     pantalla.fill(colo_de_fondo)
#     pantalla.blit(trivia_mix, (150, 70))
#     # actualizamos pantalla
#     pygame.display.flip()

# pygame.quit()
