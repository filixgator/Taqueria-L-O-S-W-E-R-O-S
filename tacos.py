import boto3
import json
from pprint import pprint

#sqs = boto3.client('sqs')

#response = sqs.receive_message(
#	QueueUrl='https://sqs.us-east-1.amazonaws.com/292274580527/cc406_team5',

#)

#recibidos = []

#for message in response["Messages"]:
#	recibidos.append(message['ReceiptHandle'])
#	print(message['Body'])

class sub_orden:
	def __init__(self,part_id,tipo,meat,quantity,ingredientes):
		self.part_id = part_id
		self.tipo = tipo
		self.meat = meat
		self.quantity = quantity
		self.ingredientes = ingredientes

class steps:
	def __init__(self,step,state,action,part_id,startTime,endTime):
		self.step = step
		self.state = state
		self.action = action
		self.part_id = part_id
		self.startTime =startTime
		self.endTime = endTime

class answer:
	def __init__(self,start_time):
		self.start_time = start_time
		self.end_date = None
		self.steps = None

class Pedido:
	def __init__(self,datetime,request_id,orden):
		self.datetime = datetime
		self.request_id = request_id
		self.orden = orden
		self.answer = None
	def __str__(self):
		return str(self.request_id)
class Struct:
	def __init__(self, **entries):
		self.__dict__.update(entries)

#class Taco:
#	def __init__(self):
#		self.tortilla = "maiz"
#		self.carne = ["adobada","asada","al pastor"]
#		self.salsa = "de la que pica"

def obj_dict(obj):
	return obj.__dict__

def json_2_Pedido(data):	#transfora a objeto Pedido
	#with open('ord.json','r') as data:
	#	data = json.load(data)
	#pprint(data)
	Pedido_pal_Prieto = Struct(**data)
	sub_pedidos = []
	sub_steps = []
	for i in Pedido_pal_Prieto.orden:
		sub_pedidos.append(Struct(**i))
	if Pedido_pal_Prieto.answer != None:
		for i in Pedido_pal_Prieto.answer:
			sub_steps.append(Struct(**i))
	Pedido_pal_Prieto.orden=sub_pedidos
	Pedido_pal_Prieto.answer=sub_steps
	#print(Pedido_pal_Prieto.orden[1].meat)
	return Pedido_pal_Prieto

#sqs = boto3.client('sqs')

#response = sqs.receive_message(
#	QueueUrl='https://sqs.us-east-1.amazonaws.com/292274580527/cc406_team5',

#)

#recibidos = []

#for message in response["Messages"]:
#	recibidos.append(message['ReceiptHandle'])
#	print(message['Body'])

print("Taqueria los weros - graficas")
ingredientes_uno = ["cebolla","cilantro","aguacate"]
ingredientes_dos = ["cebolla","limon","aguacate","frijoles"]

orden = [sub_orden("BB41","taco","asada",3,ingredientes_uno),sub_orden("BB42","mulita","adobada",1,ingredientes_dos)]

Pedido_pal_Wero = Pedido(2017,"AA32",orden)

pedido_json = json.dumps(Pedido_pal_Wero, default=obj_dict)
with open('ord.json','w') as out:
	out.write(pedido_json)
pedido_json = json.loads(pedido_json)
ped = json_2_Pedido(pedido_json)
print(ped.datetime)
