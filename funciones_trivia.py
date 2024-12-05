import os
import json

#PARSER -> Conversion 
#Pasar del archivo CSV a una lista de diccionarios (todos str)
#La cabecera del csv se van a convertir en las claves de mi diccionario

def obtener_claves(archivo,separador:str) -> list:
    primer_linea = archivo.readline()
    primer_linea = primer_linea.replace("\n","")
    lista_claves = primer_linea.split(separador)
    
    return lista_claves

def obtener_valores(linea,separador:str) -> list:
    linea_aux = linea.replace("\n","")
    lista_valores = linea_aux.split(separador)
    return lista_valores

def crear_diccionario(lista_claves:list,lista_valores:list) -> dict:
    diccionario_aux = {} #Alumno/Usuario/Heroe/Etc
    for i in range(len(lista_claves)):
        diccionario_aux[lista_claves[i]] = lista_valores[i]
        
    return diccionario_aux

#Siempre va a generar una lista de sólo strings, hay que convertir los numericos en otra función propia
def parse_csv(lista_elementos,nombre_archivo:str) -> bool: 
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo,"r") as archivo:
            lista_claves = obtener_claves(archivo,",")
            for linea in archivo:
                lista_valores = obtener_valores(linea,",")
                diccionario_aux = crear_diccionario(lista_claves,lista_valores) #Alumno/Usuario/Heroe/Etc
                lista_elementos.append(diccionario_aux)        
        return True
    else:
        return False
        
