import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


plt.figure(1, figsize=(18, 5))
#Datos de prueba
diccTacos = {'Mulitas':35,'Quesadillas':43,'Tacos':41,'Tortas':13,'Tostadas':39, 'PMulitas':35,'PQuesadillas':43,'PTacos':41,'PTortas':13,'PTostadas':39}
diccIngredientes = {"CEBOLLA" : [500,400,350,300], "CILANTRO" : [500,450,400], "SALSA" : [500,480,430], "GUACAMOLE" : [500,470,420], "QUESO" : [500,300,250], "FRIJOLES" : [500,450,300]}
diccTiempo = {"CEBOLLA" : 500, "CILANTRO" : 500}


def graficar(diccTacos,diccIngredientes):
	names = ['Mul','Ques','Tacos','Tortas','Tost']
	values = [diccTacos['Mulitas'],diccTacos['Quesadillas'],diccTacos['Tacos'],diccTacos['Tortas'], diccTacos['Tostadas']]
	valuesP = [diccTacos['PMulitas'],diccTacos['PQuesadillas'],diccTacos['PTacos'],diccTacos['PTortas'], diccTacos['PTostadas']]

	#Cantidad de tacos
	plt.subplot(231)
	plt.bar(names, values)

	#Tiempo por orden
	plt.subplot(232)
	plt.plot(names, values)

	#Promedio por orden
	plt.subplot(233)
	plt.bar(names, valuesP)

	#Ingredientes
	plt.subplot(234)
	plt.plot(diccIngredientes["CEBOLLA"],label="CEB")
	plt.plot(diccIngredientes["CILANTRO"],label="CIL")
	plt.plot(diccIngredientes["SALSA"],label="SAL")
	plt.plot(diccIngredientes["GUACAMOLE"],label="GUA")
	plt.plot(diccIngredientes["QUESO"],label="QUE")
	plt.plot(diccIngredientes["FRIJOLES"],label="FRI")

	#Tabla tamanio ordenes
	n_rows = diccTiempo.keys()
	cell_text = [n_rows]
	plt.subplot(235)
	plt.axis('off')
	plt.table(cellText=cell_text)

	plt.suptitle('Taqueria los WERS')
	plt.show()

graficar(diccTacos,diccIngredientes)
#print(len(diccTiempo))

