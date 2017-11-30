import matplotlib.pyplot as plt
import time

#plt.figure(1, figsize=(18, 5))
#Datos de prueba
#diccTacos = {'MULITA':35,'QUESADILLA':43,'TACO':41,'TORTA':13,'TOSTADA':39, 'PMULITAS':35,'PQUESADILLAS':43,'PTACOS':41,'PTORTAS':13,'PTOSTADAS':39}
#diccIngredientes = {"CEBOLLA" : [500,400,350,300], "CILANTRO" : [500,450,400], "SALSA" : [500,480,430], "GUACAMOLE" : [500,470,420], "QUESO" : [500,300,250], "FRIJOLES" : [500,450,300]}
#diccOrdenes = {"121_253" : 5, "257_426" : 2}

def CREA():
	P = plt.figure(1, figsize=(18, 5))
#	print("P")
	P.show()
	plt.ion()
	return P

def graficar(P,diccTacos,diccIngredientes,diccOrdenes):
#	mng = plt.get_current_fig_manager()
#	mng.frame.Maximize(True)
	P.clear()
	names = ['Mul','Ques','Tacos','Tortas','Tost']
	values = [diccTacos['MULITA'],diccTacos['QUESADILLA'],diccTacos['TACO'],diccTacos['TORTA'], diccTacos['TOSTADA']]
	valuesP = [diccTacos['PMULITAS'],diccTacos['PQUESADILLAS'],diccTacos['PTACOS'],diccTacos['PTORTAS'], diccTacos['PTOSTADAS']]
	#Cantidad de tacos
	C = P.add_subplot(321)
	C.bar(names, values)

	#Tiempo por orden
	T = P.add_subplot(322)
	T.plot(diccTacos['TMULITA'],label='MUL')
	T.plot(diccTacos['TQUESADILLA'],label='QUES')
	T.plot(diccTacos['TTACO'],label='TACO')
	T.plot(diccTacos['TTORTA'],label='TORTA')
	T.plot(diccTacos['TTOSTADA'],label='TOST')

	#Promedio por orden
	Prom = P.add_subplot(323)
	Prom.bar(names,valuesP)

	#Ingredientes
	I = P.add_subplot(325)
	I.plot(diccIngredientes["CEBOLLA"],label="CEB")
	I.plot(diccIngredientes["CILANTRO"],label="CIL")
	I.plot(diccIngredientes["SALSA"],label="SAL")
	I.plot(diccIngredientes["GUACAMOLE"],label="GUA")
	I.plot(diccIngredientes["QUESO"],label="QUE")
	I.plot(diccIngredientes["FRIJOLES"],label="FRI")

	#Tabla tamanio ordenes
	cols = ['ID_orden','Size']
	rows = []
	cell_text = []
	if len(diccOrdenes.keys()) > 1:
		for i in diccOrdenes.keys():
			cell_text.append([i,diccOrdenes[i]])
		Tab = P.add_subplot(326)
		Tab.axis('off')
		Tab.table(cellText=cell_text,
			colLabels=cols,
			loc='center')

	P.suptitle('Taqueria  L O S   W E R O S')
	P.canvas.draw()
	plt.pause(2)
	return P

#graficar(diccTacos,diccIngredientes,diccOrdenes)
#print(len(diccTiempo))
#PP = CREA()
#while True:
#	PP = graficar(PP,diccTacos,diccIngredientes,diccOrdenes)
#PP = graficar(PP,diccTacos,diccIngredientes,diccOrdenes)
