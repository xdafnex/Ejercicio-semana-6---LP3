# -*- coding: utf-8 -*-
"""
Created on Mon May  6 16:33:08 2024

@author: Dell
"""

import os

def crear_archivo(nombre, contenido):
    archivo = open(nombre,"wt")
    archivo.write(contenido)
    archivo.close()

def eliminar_archivo(nombre):
    os.remove(nombre)

def agregar_contenido_archivo(nombre, contenido):
    archivo = open(nombre,"at")
    archivo.write("\n" + contenido)
    archivo.close()

def leer_archivo(nombre):
    archivo = open(nombre,"rt",encoding='utf8')
    contenido = archivo.read()
    return contenido

