import time
import random
import threading
import json
import boto3
from copy import copy
from time import time as t
from threading import BoundedSemaphore
from pprint import pprint
from Queue import Queue
from datetime import datetime as date
#CLASES
class Taquero(threading.Thread):
	def __init__(self,ID):
		threading.Thread.__init__(self)
		self.request = None
		self.request_id = None
		self.sub_orden_id = None
		self.answer_steps = None
		self.ID = "T{0}".format(ID)
		self.Hold = None
		self.counter = 0
	def run(self):
		print(self.ID)
		while True:
			## ELIGE ENTRE ORDEN DE QUEUE O DE ORDEN DE HOLD
			if self.Hold == None:
				try:	self.Hold = Queues[self.ID].get(False)
				except:	self.Hold = None
			if self.request == None:
				try:	self.request = Queues[self.ID].get()
				except:	self.request = None
			if self.Hold == None and self.request == None:	continue
			elif self.Hold != None and self.request != None:
				if self.Hold[2] >= self.request[2] and self.counter < CONTADOR:
					self.request_id = self.request[0]
					self.sub_orden_id = self.request[1]
					self.request = None
					self.counter += 1
				else:
					self.request_id = self.Hold[0]
					self.sub_orden_id = self.Hold[1]
					self.Hold = None
					self.counter = 0
			elif self.request == None:
				self.request_id = self.Hold[0]
				self.sub_orden_id = self.Hold[1]
				self.Hold = None
			elif self.Hold == None:
				self.request_id = self.request[0]
				self.sub_orden_id = self.request[1]
				self.request = None
			## OBTENER SUB_ORDEN DE LA BARRA
			if self.request_id != None:
				for SUB in Barra[self.request_id].orden:
					if SUB.part_id == self.sub_orden_id:
						## PREPARA SUB_ORDEN
						self.answer_steps = Prepara_Tacos(SUB,self)
				Barra[self.request_id].answer.steps.append(self.answer_steps)
				time.sleep(1)
			continue

class Mesero(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.sub_ordenes_total = 0
		self.answers_total = 0
	def run(self):
		while True:	## REVISAR SI ALGUIEN EL BARRA YA TIENE ORDEN COMPLETA
			ID_EN_BARRA = Barra.keys()
			for id in ID_EN_BARRA:
				if len(Barra[id].orden) == len(Barra[id].answer.steps):
					## GENERAR RESPUESTA
					A = answer(Barra[id].datetime)
					A.end_date = str(date.now())
					A.steps = []
					for R in Barra[id].answer.steps:
						for r in R:
							A.steps.append(r)
					Barra[id].answer = A
#					A_SQS = json.dumps(Barra[id], default=obj_dict)
					A_SQS = json.dumps(A, default=obj_dict)
					## RESPONDER A SQS
                                        reply_SQS(A_SQS,id)
					RESULTS.append(Barra[id])
#					JSON_RESULTS.append(A_SQS)
			for i in RESULTS:
				## QUITAR CLIENTE DE BARRA
				if i.request_id in ID_EN_BARRA:
					print("\t CLIENTE DESPACHADO: {0}".format(Barra[i.request_id]))
					del Barra[i.request_id]
					## DELETE DE SQS
					delete_SQS(i.request_id)

class sub_orden(object):
	def __init__(self,part_id,tipo,meat,quantity,ingredients):
		self.part_id = part_id
		self.tipe = tipo
		self.meat = meat
		self.quantity = quantity
		self.ingredients = ingredients

class steps:
	def __init__(self,step,state,action,part_id,startTime):
		self.step = step
		self.state = state
		self.action = action
		self.part_id = part_id
		self.startTime = startTime
		self.endTime = None

class answer:
	def __init__(self,start_time):
		self.start_time = start_time
		self.end_date = None
		self.steps = []

class pedido(object):
	def __init__(self,datetime,request_id,orden):
		self.datetime = datetime
		self.request_id = str(request_id)
		self.orden = orden
		self.answer = None
	def __init__(self):
		self.datetime = None
                self.request_id = None
                self.orden = None
                self.answer = None
	def __str__(self):
		return str("ID Pedido: {0} \t Sub-ordenes: {1}".format(
				self.request_id,
				len(self.orden)))

## FUNCIONES
def obj_dict(obj):
	return obj.__dict__

def json_2_Pedido(data):	## TRANSFORMA SQS A OBJETO PEDIDO
	sub_ordenes = []
	J = json.loads(data)	## CONVERTIR STRING A JSON
	P = pedido()
	P.datetime,P.request_id = J['datetime'],J['request_id']
	for D in J['orden']:	#'orden' ES UNA LISTA DE SUBORDENES
		SUB = sub_orden(D['part_id'],D['type'],D['meat'],D['quantity'],D['ingredients'])
		sub_ordenes.append(SUB)
	P.orden = sub_ordenes
	P.answer = answer(J['datetime'])
	return P		## RETURN OBJETO PEDIDO

## CREA TORTILLAS O CUALQUIER INGREDIENTE
def crea_ingrediente(dicc, ingrediente):
	time.sleep(SLEEP_TIME)
	dicc[ingrediente] = 500
	return

def Prepara_Tacos(sub_orden, Taquero):
	steps_orden = [steps(1, "running", "working on order", sub_orden.part_id, str(date.now().time()))]
	num_steps = 2
	for taco in range(sub_orden.quantity):
		if Tortillas[Taquero.ID] > 1:
			Tortillas[Taquero.ID] -= 1
		else:
			## WAIT FOR TORTILLAS
			st = steps(num_steps, "suspend", "waiting for tortillas", sub_orden.part_id, str(date.now().time()))
			num_steps += 1
			crea_ingrediente(Tortillas,Taquero.ID)
			st.endTime = str(date.now())
			steps_orden.append(st)
			## RESUME ORDEN
			st = steps(num_steps, "running", "working on order", sub_orden.part_id, str(date.now().time()))
                        num_steps += 1
                        st.endTime = str(date.now())
                        steps_orden.append(st)

		for i in sub_orden.ingredients:
			sema.acquire()
			if ingredients[i.upper()] > 1:
				ingredients[i.upper()] -= 1
				sema.release()
			else:
				## WAIT FOR INGREDIENT
				st = steps(num_steps, "suspend", "waiting for {0}".format(i.upper()), sub_orden.part_id, str(date.now().time()))
				crea_ingrediente(ingredients,i.upper())
                                sema.release()
				st.endTime = str(date.now().time())
				steps_orden.append(st)
				num_steps += 1

				st = steps(num_steps, "running", "working on order", sub_orden.part_id, str(date.now().time()))
                                num_steps += 1
                                st.endTime = str(date.now().time())
                                steps_orden.append(st)

	st = steps(num_steps,"FINISHED", "SUB_ORDEN COMPLETED", sub_orden.part_id, steps_orden[0].startTime)
	st.endTime = str(date.now().time())
	steps_orden.append(st)
	steps_orden[0].endTime = str(date.now().time())
	return steps_orden

def pull_SQS():
	## READ FROM SQS
	response = sqs.receive_message(QueueUrl='https://sqs.us-east-1.amazonaws.com/292274580527/cc406_team5')
	for message in response["Messages"]:
#		recibidos.append(message['ReceiptHandle'])
		Orden_SQS = message['Body']
		Orden_SQS = json_2_Pedido(Orden_SQS)
		recibidos[Orden_SQS.request_id] = message['ReceiptHandle']
	return Orden_SQS

def reply_SQS(ANSWER,ID):
	reply = sqs.send_message(QueueUrl='https://sqs.us-east-1.amazonaws.com/292274580527/cc406_response5',MessageBody=ANSWER)
	print("\t \t RESPONDER SQS: {0}".format(ID))

def delete_SQS(ID):
	RECEIPT = recibidos[ID]
	delete = sqs.delete_message(QueueUrl='https://sqs.us-east-1.amazonaws.com/292274580527/cc406_team5',ReceiptHandle=RECEIPT)
	print("\t DELETE: {0}".format(ID))

def asignarQ(ID_PED, ID_SUB, SUB_SIZE):
	while True:		## ASIGNAR QUEUE DE ESPERA
		for l in range(1, len(Queues)+1):
			if Queues["T{0}".format(l)].qsize() < Q_Size:
				## SI NO HAY ESPACIO EN QUEUES, VOLVER A REVISAR
				print("ACOMODANDO {0} \t EN QUEUE  T{1} \t CON TAMANO DE {2}".format(ID_SUB, l,Queues["T{0}".format(l)].qsize()))
				Queues["T{0}".format(l)].put([ID_PED, ID_SUB, SUB_SIZE])
				return
	return



def main():
	print("==== M A I N ====")
	Todas_las_Ordenes = []
	Todas_pero_json = []
#	while not SQS_List.empty():
	for i in range(100):
		## PULL DE SQS
		pedido_Actual = pull_SQS()
		while True:
			if len(Barra.keys())< B_Size:
				Barra[str(pedido_Actual.request_id)] = pedido_Actual
				break
			else:	continue
		for sub in pedido_Actual.orden:
		## ASIGNAR QUEUE A CADA SUB_ORDEN DEL PEDIDO
			asignarQ(pedido_Actual.request_id, sub.part_id, sub.quantity)
		continue

	time.sleep(120)
	## IMPRIMIR ORDENES COMPLETAS
	print("\n \t IMPRIME RESULTS")
	num = 1
	for element in RESULTS:
		print('{3} - Pedido: {0} \t Start Date: {1} \t End Date: {2}'.format(element.request_id, element.answer.start_time, element.answer.end_date, num))
		num += 1
		for step in element.answer.steps:
			print('\t PART ID: {0} \t STATE: {1} \t ACTION: {2}'.format(step.part_id, step.state, step.action))


## VARIABLES
sqs = boto3.client('sqs')
sema = BoundedSemaphore()
SLEEP_TIME = 5
recibidos = {}
Q_Size = 10
B_Size = 20
CONTADOR = 5
Queues = {"T1" : Queue(Q_Size), "T2" : Queue(Q_Size), "T3" : Queue(Q_Size)}
Tortillas =   {"T1" : 500, "T2" : 500, "T3" : 500}
ingredients =   {"CEBOLLA" : 500, "CILANTRO" : 500, "SALSA" : 500, "GUACAMOLE" : 500, "QUESO" : 500, "FRIJOLES" : 500}
Taquero_1 = Taquero(1)
Taquero_2 = Taquero(2)
Taquero_3 = Taquero(3)
Taquero_1.start()
Taquero_2.start()
Taquero_3.start()
Barra = {}
RESULTS = []
JSON_RESULTS = []
MESERO = Mesero()
MESERO.start()
## MAIN
main()

