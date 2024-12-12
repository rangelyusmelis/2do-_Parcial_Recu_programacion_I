import os
import random
import json
from datetime import datetime
from Constantes import *


def crear_diccionario_item(lista_valores: list) -> dict:
    item_cuestionario = {}
    item_cuestionario["pregunta"] = lista_valores[0]
    item_cuestionario["opcion 1"] = lista_valores[1]
    item_cuestionario["opcion 2"] = lista_valores[2]
    item_cuestionario["opcion 3"] = lista_valores[3]
    item_cuestionario["opcion 4"] = lista_valores[4]
    item_cuestionario["respuesta correcta"] = int(lista_valores[5])
    return item_cuestionario


def leer_csv_preguntas(nombre_archivo: str, lista_preguntas: list) -> bool:
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r", encoding="utf-8", errors="ignore") as archivo:
            archivo.readline()
            for linea in archivo:
                linea_aux = linea.replace("\n", "")
                lista_valores = linea_aux.split(",")
                item_cuestionario_aux = crear_diccionario_item(lista_valores)
                lista_preguntas.append(item_cuestionario_aux)
                retorno = True
    else:
        retorno = False
        print("no se pudo leer el archivo")
    return retorno


def limpiar_consola():
    input(" presione una tecla para continuar)")
    os.system("cls")


def pedir_numero(mensaje: str, mensaje_error: str, min: int, max: int) -> int:
    while True:
        numero = input(mensaje)
        if numero.isdigit():
            numero = int(numero)
            if numero <= max and numero >= min:
                return numero
            else:
                print(f"error el numero deberia de estar entre {min} y {max}")
        else:
            print(mensaje_error)


def ejecutar_menu():
    print("PREGUNTADOS\n 1- Jugar \n 2- Fin de la Partida \n 3- top 10 partidas")
    return pedir_numero("ingrese el numero de la opcion deseada ", "error en el numero ingresado", 1, 3)


def mostrar_pregunta(pregunta_juego: dict) -> None:
    print(f"Pregunta: {pregunta_juego["pregunta"]}")
    print(f"1: {pregunta_juego["opcion 1"]}")
    print(f"2: {pregunta_juego["opcion 2"]}")
    print(f"3: {pregunta_juego["opcion 3"]}")
    print(f"4: {pregunta_juego["opcion 4"]}")


def mezclar_lista(lista_preguntas: list) -> None:
    random.shuffle(lista_preguntas)


def jugar_preguntados_por_consola(datos_juego: dict, lista_preguntas) -> None:
    contador_respuestas_correctas = 0
    indice = 0
    while datos_juego["vidas"] != 0:

        if contador_respuestas_correctas == 5:
            modificar_vidas(datos_juego, 1)
            contador_respuestas_correctas = 0

        print(f"PUNTUACION ACTUAL: {datos_juego['puntuacion']}")
        print(f"VIDAS RESTANTES: {datos_juego["vidas"]}")

        if indice == len(lista_preguntas):
            indice = 0
            mezclar_lista[lista_preguntas]

        pregunta_actual = lista_preguntas[indice]
        mostrar_pregunta(pregunta_actual)
        respuesta = pedir_numero(
            "su respuesta: ", "reingrese la respuesta: (entre 1 y 4)", 1, 4)
        if verificar_respuesta(datos_juego, pregunta_actual, respuesta):
            print("RESPUESTA CORRECTA")
            contador_respuestas_correctas += 1
        else:
            print("RESPUESTA INCORRECTA")
            contador_respuestas_correctas = 0
        indice += 1

        limpiar_consola()


def verificar_respuesta(datos_juego: dict, pregunta_actual: dict, respuesta: int) -> bool:
    if respuesta == pregunta_actual["respuesta correcta"]:
        datos_juego['puntuacion'] += PUNTUACION_ACIERTO
        retorno = True
    else:
        datos_juego["vidas"] -= 1
        datos_juego['puntuacion'] -= PUNTUACION_ERROR
        print(f"la respuesta correcta es la {
              pregunta_actual["respuesta correcta"]}")
        retorno = False
    return retorno


def reiniciar_estadisticas(datos_juego: dict):
    datos_juego["puntuacion"] = 0
    datos_juego["vidas"] = CANTIDAD_VIDAS


def modificar_vidas(datos_juego: dict, vida_nueva: int):
    datos_juego["vidas"] += vida_nueva


def guardar_puntuacion_lista(lista_rankings: list, diccionario_jugador: dict) -> bool:
    diccionario_auxiliar = {}
    diccionario_auxiliar["nombre"] = diccionario_jugador["nombre"]
    diccionario_auxiliar["puntuacion"] = diccionario_jugador["puntuacion"]
    fecha_actual = (datetime.now()).strftime("%d/%m/%y")
    diccionario_auxiliar["fecha"] = fecha_actual
    lista_rankings.append(diccionario_auxiliar)


def generar_json(nombre_archivo: str, lista: list) -> bool:
    if type(lista) == list and len(lista) > 0:
        with open(nombre_archivo, "w") as archivo:
            json.dump(lista, archivo, indent=4)
            retorno = True
    else:
        retorno = False
    return retorno


def ordenar_puntaciones(lista_rankings: list, criterio: str):
    for i in range(len(lista_rankings)-1):
        for j in range(i+1, len(lista_rankings)):
            if (lista_rankings[i][criterio] < lista_rankings[j][criterio]):
                auxiliar = lista_rankings[i]
                lista_rankings[i] = lista_rankings[j]
                lista_rankings[j] = auxiliar


def mostrar_rankings(lista_rankings: list) -> bool:
    if len(lista_rankings) > 0:
        print(f"Nombre          Puntuacion          Fecha")
        for ranking in lista_rankings:
            print(f"{ranking["nombre"]}          {
                  ranking["puntuacion"]}           {ranking["fecha"]}")
        return True
    else:
        return False
