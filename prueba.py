import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


plt.figure(1, figsize=(18, 5))
#Datos de prueba
diccTacos = {'Mulitas':35,'Quesadillas':43,'Tacos':41,'Tortas':13,'Tostadas':39}
diccIngredientes = {"CEBOLLA" : [500,400,350,300], "CILANTRO" : [500,450,400], "SALSA" : 500, "GUACAMOLE" : 500, "QUESO" : 500, "FRIJOLES" : 500}
diccTiempo = {"CEBOLLA" : 500, "CILANTRO" : 500}


def graficar(diccTacos,diccIngredientes):
	names = ['Mul','Ques','Tacos','Tortas','Tost']
	values = [diccTacos['Mulitas'],diccTacos['Quesadillas'],diccTacos['Tacos'],diccTacos['Tortas'], diccTacos['Tostadas']]

	#Cantidad de tacos
	plt.subplot(231)
	plt.bar(names, values)

	#Tiempo por orden
	plt.subplot(232)
	plt.plot(names, values)

	#Promedio por orden
	plt.subplot(233)
	plt.scatter(names, values)

	#Ingredientes
	plt.subplot(234)
	for i in diccIngredientes.keys():
		plt.plot(diccIngredientes[i],label=i)


	#Tabla tamanio ordenes
	plt.subplot(235)
#	plt.table(names, values)


	plt.suptitle('Taqueria los WERS')
	plt.show()

graficar(diccTacos,diccIngredientes)
