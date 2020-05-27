# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 10:28:40 2019

@author: (╯°□°)╯︵ ┻━┻
"""

import ArreglarCSV as ac #Importa el codigo ArreglarCSV y le asigna el nombre ac
import FiabilidadCronbach as fc #Importa el codigo FiabilidadCronbach y le asigna el nombre fc
import Kr20  as kr #Importa el codigo ArreglarCSV y le asigna el nombre ac


class Main: # Inicio clase Main

    def __init__(self): #Clase Init
        self.alfaCronbach = 0 #Se instancia alfaCronbach

    def seleccion(self, numero): #Funcion  selección, se envía parámetro numero

        if numero == 1:    #Inicio de sentencia condicional if
            ac.ArreglarCSV() #Si es 1 el objeto ac inicia la función ArreglarCSV
                                #importado previamente
        elif numero == 2:  #Opcion 2 del codicional
            fc.FiablidadCronbach().resultado()#Si es 2 el objeto fc inicia la función resultado()
                                                #importado de la clase Fiabilidad Cronbach
        elif numero == 3: #Opcion 3 del condicional
            kr.Kr20().resultado() #Si es 3 el objeto kr inicia la funcion resultado()
                                                #importado de la clase Kr20
        #Fin funcion selección

    if __name__ == "__main__": #Condicional iniciado
        opcion = 0

        while opcion >= 0: #Mientras la opción sea 0 o mayor permanece en el ciclo
            Main()
            print('\n\n\n Para crear CSV escriba 1')
            print('Para calcular alfa de crombach escriba 2')
            print('para calcular kr20 escriba 3')
            print('Para salir ponga 0')
            opcion = int(input('selecciona una opción\n')) #Recibe la opcion ingresada como entero
            opcion = int(opcion)
            Main().seleccion(opcion) #Inicia funcion seleccion
            if (opcion == 0):
                opcion = -1 #Sale del ciclo while