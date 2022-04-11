# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 06:14:02 2022

@author: maaar
"""

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
            "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


def changeLetters(a, b, technic):
    index_a = letters.index(a)
    index_b = letters.index(b)
    newMessage.append(letters[(index_a + (technic*index_b))%26])

def changeMessage(key, t, message, technic):
    i =0
    j = 0
    while i<len(message):
        changeLetters(message[i], key[j], technic)
        j+=1
        i+=1
        if i % t == 0: newMessage.append(" ")
        if j == len(key): j = 0
        
def showNewMessage(technic):
    method= "cifrado"
    if technic == -1:
        method = "descifrado"
    print("El mensaje " + method + " es: ")
    for i in range(len(newMessage)):
        print(newMessage[i], end = '')
  

newMessage = []
def main():    
    c = int(input("¿Cifrar (0) o descifrar (1)? "))
    if not( c== 0 or c==1):
        print("Proceso no válido")
    else:
        
        key = input("Ingrese la clave: ").replace("", "").upper()
        t = int(input("Ingrese el parámetro t (número de letras a agrupar): "))
        entrada = input("Ingrese el mensaje: ").replace(" ", "").upper()
        
        if c == 0: technic = 1
        else: technic = -1
        changeMessage(key, t, entrada, technic)
        showNewMessage(technic)

if __name__=="__main__":
    main()
        