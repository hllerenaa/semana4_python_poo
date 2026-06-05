import transaction


class ImpresoraRed:
    def __init__(self, ip_, modelo_):
        self.ip = ip_
        self.modelo = modelo_
        self.paginas_impresoras = 0
        self.limite_impresion = 5

    def imprimir(self, paginas):
        try:
            if paginas > 0:
                self.paginas_impresoras += paginas
                if self.paginas_impresoras > self.limite_impresion:
                    raise NameError(f"Limite de impresion alcanzado, por favor recargue papel ({self.paginas_impresoras}/{self.limite_impresion})")
            else:
                raise NameError("Cantidad no valida")
            return True
        except Exception as e:
            return False

    def imprimir_basic(self, paginas):
        if paginas > 0:
            self.paginas_impresoras += paginas
            if self.paginas_impresoras > self.limite_impresion:
                print(f"Limite de impresion alcanzado, por favor recargue papel ({self.paginas_impresoras}/{self.limite_impresion})")
                return False
            else:
                return True
        else:
            print("Cantidad no valida")
            return False

    def reportar(self):
        print(f"Modelo: {self.modelo}, IP: {self.ip}, Paginas impresas: {self.paginas_impresoras}")


imp = ImpresoraRed("10.0.0.1", "Epson")
imp.imprimir(2)
imp.imprimir(3)
imp.imprimir(1)
imp.reportar()