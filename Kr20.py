# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 15:30:25 2019
@author: (╯°□°)╯︵ ┻━┻
"""
import pandas as pd #Se importa la libreria PANDAS
import numpy as np #Se importa la librerias NUMPY


class Kr20: #Crear clase Kr20
    def __init__(self): #Inicio funcion init

        self.EFelicdad = pd.read_csv('DFnumericoInvertido.csv') #Se lee el datasetDFnumericoInvertido.csv

        self.seleccion = self.EFelicdad.iloc[:, 29:42] #Usa números enteros para leer y escribir datos
                                                        # en el DataFrame por medio de pandas"""
        self.seleccion['total'] = self.seleccion.sum(axis=1) #Agrega Total al 1er index
                                                               #del ndarray (array NumPy)
        self.result = self.kr20(self.seleccion) #Método result en kr20 selección
        self.rCorrItemTest = self.corrItemTest(self.seleccion)
        self.rIndiceHCorregido = self.indicecorrelaT(self.seleccion)
        self.siseQuitaElemento = self.siSequitaElemento(self.seleccion)

    def kr20(self, seleccion): #Inicio funcion kr20 con paso de parámetro selección
        p = seleccion.drop(['total'], axis=1).mean(axis=0) #Especifica la etiqueta total
                                                                #del indice 1 y calcula la media
        q = 1 - p
        pq = p * q
        k = len(seleccion.T) - 1

        sumatoria_pq = pq.sum() #Halla sumatoria adel resultado pq = p*Q
        varT = seleccion['total'].var(ddof=0)
        result = (k / (k - 1)) * (1 - (sumatoria_pq / varT)) #Valor resultado
        return result

    def siSequitaElemento(self, seleccion): #Inicio funcion siSequitaElemento con paso de parámetro selección
        vector = [] #Crea un vector vacio

        for x in seleccion.drop(['total'], axis=1).columns: #Recorre y suelta(borra) total en indice 1
            seleccionBorrar = seleccion.drop([x], axis=1).copy()
            p = seleccionBorrar.drop(['total'], axis=1).mean(axis=0)
            q = 1 - p
            pq = p * q
            k = len(seleccionBorrar.T) - 1 #borrado
            sumatoria_pq = pq.sum()

            varT = seleccionBorrar['total'].var(ddof=0)
            result = (k / (k - 1)) * (1 - (sumatoria_pq / varT)) #Nuevo valor Resultado

            vector.append(result) #Agrega Resultado al vector
        return vector #Regresa vector con elemento quitado

    def resultado(self): #Inicio método Resultado
        self.tabla = pd.DataFrame([self.siseQuitaElemento, #Se construye el dataframe
                                   self.rCorrItemTest,
                                   self.rIndiceHCorregido],
                                  index=['kr20 sin el item', #Lista los datos
                                         'Indice homogeneidad',
                                         'Indice homogeneidad c'],
                                  columns=[x + 1 for x in range(len(self.siseQuitaElemento))]).T
        print(self.tabla)#Imprime tabla

        print('      el indice de kr20 es: ', self.result) #Según el condicional imprime un resultado
        if self.result < 0.70:
            print("      Los datos no son consistentes")
        if self.result > 0.70 and self.result < 0.80:
            print("      la fiablidad es aceptable")
        if self.result > 0.80 and self.result < 0.99:
            print("      la fiablidad es buena")
        if self.result == 1:
            print("      la fiablidad es exelente")

    def corrItemTest(self, matriz1): #Inicio método CorrItemTest pasando parámetro matriz1
        salida = [] #Se crea vector vacío salida
        for x in matriz1.drop(['total'], axis=1): #Condicional para soltar elementos en indice 1
            b = matriz1['total']
            a = matriz1[x]
            c = np.corrcoef(a, b)[0, 1]
            salida.append(c) #Se agrega a salida el valor de c
        return salida

    def indicecorrelaT(self, matriz1):#Inicio método indicecorrelaT pasando parámetro matriz1
        salida = [] #Se crea vector vacío salida
        for x in matriz1.drop(['total'], axis=1):#Condicional para soltar elementos en  indice 1
            b = matriz1['total']
            a = matriz1[x]
            c = np.corrcoef(a, b - a)[0, 1]
            salida.append(c) #Se agrega a salida el valor de c
        return salida

    """vector=[]
    for i in seleccion.drop(['total'], axis =1):
        vector.append( seleccion[i][seleccion[i]==1].value_counts()/len(seleccion))
    p=pd.DataFrame(vector).T
    resul2t=(k/(k-1))*((varT-sumatoria_pq)/varT)
    """