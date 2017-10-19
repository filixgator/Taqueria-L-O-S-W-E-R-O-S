from tkinter import*

class sub_orden:
        def __init__(self,part_id,type,meat,quantity,ingredients):
                self.part_id = part_id
                self.type = type
                self.meat = meat
                self.quantity = quantity
                self.ingredients = ingredients

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

            
#VARIABLES
listaPedidos = []
totalTacos = 0
cantidadAsada=0
cantidadAdobada = 0
cantidadCabeza=0
cantidadTripa = 0
cantidadLengua = 0
cantidadSuadero = 0
cantidadVeggie = 0
n=8

    


#CREACION DE PEDIDOS
pedido1 = Pedido(91017,15,sub_orden(20,"taco","asada",3,("aguacate","cebolla")))
listaPedidos.append(pedido1)

pedido2 = Pedido(91017,15,sub_orden(20,"taco","asada",2,("aguacate","cebolla")))
listaPedidos.append(pedido2)

pedido3 = Pedido(91017,15,sub_orden(20,"taco","adobada",42,("aguacate","cebolla")))
listaPedidos.append(pedido3)

pedido4 = Pedido(91017,15,sub_orden(20,"taco","lengua",13,("aguacate","cebolla")))
listaPedidos.append(pedido4)

pedido5 = Pedido(91017,15,sub_orden(20,"taco","veggie",16,("aguacate","cebolla")))
listaPedidos.append(pedido5)

pedido6 = Pedido(91017,15,sub_orden(20,"taco","suadero",8,("aguacate","cebolla")))
listaPedidos.append(pedido6)

pedido7 = Pedido(91017,15,sub_orden(20,"taco","tripa",21,("aguacate","cebolla")))
listaPedidos.append(pedido7)

pedido8 = Pedido(91017,15,sub_orden(20,"taco","cabeza",26,("aguacate","cebolla")))
listaPedidos.append(pedido8)



for pedido in listaPedidos:
    if pedido.orden.meat == "asada":
        cantidadAsada = cantidadAsada+(pedido.orden.quantity)
    elif pedido.orden.meat == "adobada":
        cantidadAdobada = cantidadAdobada+(pedido.orden.quantity)
    elif pedido.orden.meat == "cabeza":
        cantidadCabeza = cantidadCabeza+(pedido.orden.quantity)
    elif pedido.orden.meat == "tripa":
        cantidadTripa = cantidadTripa+(pedido.orden.quantity)
    elif pedido.orden.meat == "lengua":
        cantidadLengua = cantidadLengua+(pedido.orden.quantity)
    elif pedido.orden.meat == "suadero":
        cantidadSuadero = cantidadSuadero+(pedido.orden.quantity)
    elif pedido.orden.meat == "veggie":
        cantidadVeggie = cantidadVeggie+(pedido.orden.quantity)

totalTacos = cantidadAsada+cantidadAdobada+cantidadCabeza+cantidadTripa+cantidadLengua+cantidadSuadero+cantidadVeggie


       
        
print(len(listaPedidos))
print("tacos asada",cantidadAsada)
print("tacos adobada",cantidadAdobada)
print(totalTacos)





def graficar(cantidadAsada,cantidadAdobada,cantidadCabeza,cantidadTripa,cantidadLengua,cantidadSuadero, cantidadVeggie):
    root = Tk()
    canvas = Canvas(root, width=1000,height = 800, bg = 'white')
    canvas.pack()

    #GRAFICA 1
    canvas.create_line(60,10,60,300)
    canvas.create_line(60,300,350,300)
    
    canvas.create_line(101,305,101,295)
    canvas.create_line(142,305,142,295)
    canvas.create_line(183,305,183,295)
    canvas.create_line(224,305,224,295)
    canvas.create_line(265,305,265,295)
    canvas.create_line(306,305,306,295)
    canvas.create_line(347,305,347,295)

    canvas.create_line(55,10,65,10)
    canvas.create_line(55,39,65,39)
    canvas.create_line(55,68,65,68)
    canvas.create_line(55,97,65,97)
    canvas.create_line(55,126,65,126)
    canvas.create_line(55,155,65,155)
    canvas.create_line(55,184,65,184)
    canvas.create_line(55,213,65,213)
    canvas.create_line(55,242,65,242)
    canvas.create_line(55,271,65,271)
    
    canvas.create_rectangle(60,300-(cantidadAsada*5.8),101,300,fill = "red")
    canvas.create_rectangle(101,300-(cantidadAdobada*5.8),142,300,fill = "blue")
    canvas.create_rectangle(142,300-(cantidadCabeza*5.8),183,300,fill = "red")
    canvas.create_rectangle(183,300-(cantidadTripa*5.8),224,300,fill = "blue")
    canvas.create_rectangle(224,300-(cantidadLengua*5.8),265,300,fill = "red")
    canvas.create_rectangle(265,300-(cantidadSuadero*5.8),306,300,fill = "blue")
    canvas.create_rectangle(306,300-(cantidadVeggie*5.8),347,300,fill = "red")

    canvas.create_text(200,350,fill="darkblue",font="Times 12 italic bold",text="CANTIDAD DE TACOS PEDIDOS")
    
    canvas.create_text(80,315,fill="darkblue",font="Times 8 italic bold",text="Asada")
    canvas.create_text(120,330,fill="darkblue",font="Times 8 italic bold",text="Adobada")
    canvas.create_text(160,315,fill="darkblue",font="Times 8 italic bold",text="Cabeza")
    canvas.create_text(200,330,fill="darkblue",font="Times 8 italic bold",text="Tripa")
    canvas.create_text(240,315,fill="darkblue",font="Times 8 italic bold",text="Lengua")
    canvas.create_text(280,330,fill="darkblue",font="Times 8 italic bold",text="Suadero")
    canvas.create_text(320,315,fill="darkblue",font="Times 8 italic bold",text="Veggie")

    canvas.create_text(45,271,fill="darkblue",font="Times 8 italic bold",text="5")
    canvas.create_text(45,242,fill="darkblue",font="Times 8 italic bold",text="10")
    canvas.create_text(45,213,fill="darkblue",font="Times 8 italic bold",text="15")
    canvas.create_text(45,184,fill="darkblue",font="Times 8 italic bold",text="20")
    canvas.create_text(45,155,fill="darkblue",font="Times 8 italic bold",text="25")
    canvas.create_text(45,126,fill="darkblue",font="Times 8 italic bold",text="30")
    canvas.create_text(45,97,fill="darkblue",font="Times 8 italic bold",text="35")
    canvas.create_text(45,68,fill="darkblue",font="Times 8 italic bold",text="40")
    canvas.create_text(45,39,fill="darkblue",font="Times 8 italic bold",text="45")
    canvas.create_text(45,10,fill="darkblue",font="Times 8 italic bold",text="50")

    #GRAFICA 2
    canvas.create_line(550,10,550,300)
    canvas.create_line(550,300,840,300)

    canvas.create_line(591,305,591,295)
    canvas.create_line(632,305,632,295)
    canvas.create_line(673,305,673,295)
    canvas.create_line(714,305,714,295)
    canvas.create_line(755,305,755,295)
    canvas.create_line(796,305,796,295)
    canvas.create_line(837,305,837,295)

    canvas.create_line(545,10,555,10)
    canvas.create_line(545,39,555,39)
    canvas.create_line(545,68,555,68)
    canvas.create_line(545,97,555,97)
    canvas.create_line(545,126,555,126)
    canvas.create_line(545,155,555,155)
    canvas.create_line(545,184,555,184)
    canvas.create_line(545,213,555,213)
    canvas.create_line(545,242,555,242)
    canvas.create_line(545,271,555,271)

    canvas.create_text(700,350,fill="darkblue",font="Times 12 italic bold",text="PROMEDIO DE TACOS PEDIDOS")
    
    canvas.create_text(568,315,fill="darkblue",font="Times 8 italic bold",text="Asada")
    canvas.create_text(613,330,fill="darkblue",font="Times 8 italic bold",text="Adobada")
    canvas.create_text(658,315,fill="darkblue",font="Times 8 italic bold",text="Cabeza")
    canvas.create_text(695,330,fill="darkblue",font="Times 8 italic bold",text="Tripa")
    canvas.create_text(740,315,fill="darkblue",font="Times 8 italic bold",text="Lengua")
    canvas.create_text(780,330,fill="darkblue",font="Times 8 italic bold",text="Suadero")
    canvas.create_text(820,315,fill="darkblue",font="Times 8 italic bold",text="Veggie")

    canvas.create_text(535,271,fill="darkblue",font="Times 8 italic bold",text="10")
    canvas.create_text(535,242,fill="darkblue",font="Times 8 italic bold",text="20")
    canvas.create_text(535,213,fill="darkblue",font="Times 8 italic bold",text="30")
    canvas.create_text(535,184,fill="darkblue",font="Times 8 italic bold",text="40")
    canvas.create_text(535,155,fill="darkblue",font="Times 8 italic bold",text="50")
    canvas.create_text(535,126,fill="darkblue",font="Times 8 italic bold",text="60")
    canvas.create_text(535,97,fill="darkblue",font="Times 8 italic bold",text="70")
    canvas.create_text(535,68,fill="darkblue",font="Times 8 italic bold",text="80")
    canvas.create_text(535,39,fill="darkblue",font="Times 8 italic bold",text="90")
    canvas.create_text(535,10,fill="darkblue",font="Times 8 italic bold",text="100")

    print("promedio Asada",(cantidadAsada/totalTacos)*100)
    print("promedio Adobada",(cantidadAdobada/totalTacos)*100)
    print("promedio Cabeza",(cantidadCabeza/totalTacos)*100)
    print("promedio Tripa",(cantidadTripa/totalTacos)*100)
    print("promedio Lengua",(cantidadLengua/totalTacos)*100)
    print("promedio Suadero",(cantidadSuadero/totalTacos)*100)
    print("promedio Veggie",(cantidadVeggie/totalTacos)*100)
    

    canvas.create_rectangle(550,300-(((cantidadAsada/totalTacos)*100)*2.9),591,300,fill = "red")
    canvas.create_rectangle(591,300-(((cantidadAdobada/totalTacos)*100)*2.9),632,300,fill = "blue")
    canvas.create_rectangle(632,300-(((cantidadCabeza/totalTacos)*100)*2.9),673,300,fill = "red")
    canvas.create_rectangle(673,300-(((cantidadTripa/totalTacos)*100)*2.9),714,300,fill = "blue")
    canvas.create_rectangle(714,300-(((cantidadLengua/totalTacos)*100)*2.9),755,300,fill = "red")
    canvas.create_rectangle(755,300-(((cantidadSuadero/totalTacos)*100)*2.9),796,300,fill = "blue")
    canvas.create_rectangle(796,300-(((cantidadVeggie/totalTacos)*100)*2.9),837,300,fill = "red")

    #TABLA
    canvas.create_rectangle(100,400,580,400+30*n)
    for i in range(n-1):
	canvas.create_line(100,430+30*i,580,430+30*i)
    for j in range(2):
	canvas.create_line(260+160*j,400,260+160*j,400+30*n)
    canvas.create_text(180,415,fill="darkblue",font="Times 8 italic bold",text="Tipo de taco")
    canvas.create_text(180,445,fill="darkblue",font="Times 8 italic bold",text="Asada")
    canvas.create_text(180,475,fill="darkblue",font="Times 8 italic bold",text="Adobada")
    canvas.create_text(180,505,fill="darkblue",font="Times 8 italic bold",text="Cabeza")
    canvas.create_text(180,535,fill="darkblue",font="Times 8 italic bold",text="Tripa")
    canvas.create_text(180,565,fill="darkblue",font="Times 8 italic bold",text="Lengua")
    canvas.create_text(180,595,fill="darkblue",font="Times 8 italic bold",text="Suadero")
    canvas.create_text(180,625,fill="darkblue",font="Times 8 italic bold",text="Veggie")
    canvas.create_text(340,415,fill="darkblue",font="Times 8 italic bold",text="Cantidad")
    canvas.create_text(340,445,fill="darkblue",font="Times 8 italic bold",text=cantidadAsada)
    canvas.create_text(340,475,fill="darkblue",font="Times 8 italic bold",text=cantidadAdobada)
    canvas.create_text(340,505,fill="darkblue",font="Times 8 italic bold",text=cantidadCabeza)
    canvas.create_text(340,535,fill="darkblue",font="Times 8 italic bold",text=cantidadTripa)
    canvas.create_text(340,565,fill="darkblue",font="Times 8 italic bold",text=cantidadLengua)
    canvas.create_text(340,595,fill="darkblue",font="Times 8 italic bold",text=cantidadSuadero)
    canvas.create_text(340,625,fill="darkblue",font="Times 8 italic bold",text=cantidadVeggie)
    canvas.create_text(500,415,fill="darkblue",font="Times 8 italic bold",text="Promedio")
    canvas.create_text(500,445,fill="darkblue",font="Times 8 italic bold",text=(cantidadAsada/totalTacos)*100)
    canvas.create_text(500,475,fill="darkblue",font="Times 8 italic bold",text=(cantidadAdobada/totalTacos)*100)
    canvas.create_text(500,505,fill="darkblue",font="Times 8 italic bold",text=(cantidadCabeza/totalTacos)*100)
    canvas.create_text(500,535,fill="darkblue",font="Times 8 italic bold",text=(cantidadTripa/totalTacos)*100)
    canvas.create_text(500,565,fill="darkblue",font="Times 8 italic bold",text=(cantidadLengua/totalTacos)*100)
    canvas.create_text(500,595,fill="darkblue",font="Times 8 italic bold",text=(cantidadSuadero/totalTacos)*100)
    canvas.create_text(500,625,fill="darkblue",font="Times 8 italic bold",text=(cantidadVeggie/totalTacos)*100
        
graficar(cantidadAsada,cantidadAdobada,cantidadCabeza,cantidadTripa,cantidadLengua,cantidadSuadero, cantidadVeggie)




