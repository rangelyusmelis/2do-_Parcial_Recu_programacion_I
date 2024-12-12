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

