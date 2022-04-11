# -*- coding: utf-8 -*-
"""
Taller 1 - Criptografía 2022-1 Maria Alejandra Arias Frontanilla
Playfair

"""

alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I/J", "K", "L", "M", "N",
            "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


def changeIfIorJ(a):
    if a == "I" or a == "J":
        a = "I/J"
    return a

def anotarClave(clave):
    for i in range(len(clave)):
        if changeIfIorJ(clave[i]) not in celdas:
            celdas.append(changeIfIorJ(clave[i]))
                
def rellenarAlfabeto():  
    for i in range(len(alfabeto)):
        if alfabeto[i] not in celdas:
            celdas.append(alfabeto[i])
            
def calcularFilaColumna(letra):
    indice = celdas.index(letra)
    fila = indice//5
    columna = indice%5
    return fila, columna

def calcularLetra(fila, columna):
    return celdas[5*fila+columna]
            
def cambioParDeLetras(a, b, i):
    fa, ca = calcularFilaColumna(a)
    fb, cb = calcularFilaColumna(b)   
    
    if(fa == fb):
        newA = calcularLetra(fa, (ca+i)%5)
        newB = calcularLetra(fb, (cb+i)%5)
    elif(ca == cb):
        newA = calcularLetra((fa+i)%5, ca)
        newB = calcularLetra((fb+i)%5, cb)
    else:
        newA = calcularLetra(fa, cb)
        newB = calcularLetra(fb, ca)
    return newA, newB              
                      

def modificarTexto(entrada, tecnica):
    i = 0
    while(i < len(entrada)):
        
        oldA = changeIfIorJ(entrada[i])
        
        if(i == len(entrada)-1 or changeIfIorJ(entrada[i]) == 
           changeIfIorJ(entrada[i+1])):#última letra o letras repetidas
            oldB = "X" #Padding: X
            i+=1
        else:
            oldB = changeIfIorJ(entrada[i+1])
            i+=2
             
        output.append(cambioParDeLetras(oldA, oldB, tecnica))
            
      
def mostrarOutput(tecnica):
    tipo= "cifrado"
    if tecnica == -1:
        tipo = "descifrado"
    print("El mensaje " + tipo + " es: ")
    print(output)
        

celdas = [] #En esta lista están los elementos de la matriz
output = [] #En esta lista la salida después del cifrado o descifrado


def main():
    c = int(input("¿Cifrar (0) o descifrar (1)? "))
    if not( c== 0 or c==1):
        print("Proceso no válido")
    else:
        entrada = input("Ingrese el mensaje: ").replace(" ", "").upper()
        clave = input("Ingrese la clave: ").replace(" ", "").upper()
        anotarClave(clave)
        rellenarAlfabeto()
        if(c == 0): tecnica = 1
        if(c == 1): tecnica = -1
        modificarTexto(entrada, tecnica)
        mostrarOutput(tecnica)
        print("Padding usado: X")
if __name__=="__main__":
    main()
