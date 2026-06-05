class Dispositivo:
    def __init__(self, ip, mac):
        self.ip = ip
        self.mac = mac

    def reportar(self):
        print(f"IP: {self.ip}, MAC: {self.mac}")

    def es_valida(self):
        if "abcdefghijklmnop" in self.ip:
            return False
        else:
            return True

llamada_dispositivo = Dispositivo("10.0.0.1", "AA:BB:CC:DD:EE:FF")
llamada_dispositivo.reportar()
es_valida_ = llamada_dispositivo.es_valida()
print(es_valida_)


"""
RETO: Clase Router

Atributos (en __init__):
  - ip
  - modelo
  - rutas_configuradas (empieza en 0)

Metodos:
  - agregar_ruta(cantidad)  ->  suma cantidad a rutas_configuradas
  - reportar()              ->  imprime ip, modelo, rutas_configuradas

Pruebas al final:
  - Crear un router 192.168.1.1, Cisco-2960
  - agregar 2 rutas
  - agregar 4 rutas
  - agregar 1 ruta
  - llamar reportar()

Salida esperada:
  IP: 192.168.1.1, Modelo: Cisco-2960, Rutas: 7

"""