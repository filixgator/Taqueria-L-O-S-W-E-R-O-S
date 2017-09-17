class taco:

    def __init__(self, pedido, cantidad, cebolla, cilantro, guacamole, salsa, siguiente = None,anterior = None):

        assert type(pedido) is String
        assert type(cantidad) is int
        assert type(cebolla) is boolean
        assert type(cilantro) is boolean
        assert type(guacamole) is boolean
        assert type(salsa) is boolean
        self.pedido = pedido
        self.tiempoDeEjecucion=tiempoDeEjecucion
        self.tiempoTotal = self.tiempoTotal
        self.cantidad = cantidad
        self.aguacate = aguacate
        self.salsa=salsa
        self.Siguiente = siguiente
        self.Anterior = anterior



class orden:

    def __init__(self, Mesero, Taquero, Tortillera):
        assert type(Mesero) is int
        assert type(Taquero) is int
        assert type(Tortillera) is int
        self.Ultimo = None

        def appendTaco(self, taco):
            assert type(taco) is taco
            if self.Ultimo is None:
                self.Ultimo = taco
                self.Ultimo.Siguiente = self.Ultimo
                self.Ultimo.Anterior = self.Ultimo
            else:
                puntoTemp = self.Ultimo
                self.Ultimo = taco
                puntoPrimero = puntoTemp.Siguiente
                puntoTemp.Siguiente = self.Ultimo
                self.Ultimo.Anterior = puntoTemp
                self.Ultimo.Siguiente = puntoPrimero
                puntoPrimero.Anterior = self.Ultimo
