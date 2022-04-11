# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 10:03:29 2022

@author: aleia
"""

alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
            "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


def cambioTexto(texto, k, rot):
    output = []
    for i in range(len(texto)):
        indice = alfabeto.index(texto[i])
        output.append(alfabeto[(indice + rot*k)%26])
    return output


def main():
    
    c = int(input("¿Cifrar (0) o descifrar (1)? "))
    if not( c== 0 or c==1):
        print("Proceso no válido")
    else:
        entrada = input("Ingrese el mensaje: ").replace(" ", "").upper()
        k = int(input("Ingrese número de permutaciones k: "))
        if c == 0: rot = 1
        else: rot = -1
        print(cambioTexto(entrada, k, rot))

if __name__=="__main__":
    main()
        
