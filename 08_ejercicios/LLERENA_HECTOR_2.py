# =============================================================================
#  SOLUCION DE REFERENCIA  -  Reto: Clase Router (suma de rutas)
#  Para uso del docente como referencia.
# =============================================================================


# ---- Version basica (lo minimo que se espera) ----

class Router:

    def __init__(self, ip, modelo):
        self.ip = ip
        self.modelo = modelo
        self.rutas_configuradas = 0

    def agregar_ruta(self, cantidad):
        self.rutas_configuradas += cantidad

    def reportar(self):
        print(f"IP: {self.ip}, Modelo: {self.modelo}, Rutas: {self.rutas_configuradas}")


# Pruebas
r = Router("192.168.1.1", "Cisco-2960")
r.agregar_ruta(2)
r.agregar_ruta(4)
r.agregar_ruta(1)
r.reportar()
# Salida esperada:
# IP: 192.168.1.1, Modelo: Cisco-2960, Rutas: 7


# =============================================================================
#  VERSION MEJORADA  (para los que terminan rapido - reto extra)
# =============================================================================
# Que pasa si alguien intenta agregar_ruta(-5)? Las rutas no pueden ser negativas.
# Que pasa si superamos un limite maximo de rutas?

print()
print("--- Version mejorada con validacion y limite ---")

class RouterMejorado:

    def __init__(self, ip, modelo, limite=10):
        self.ip = ip
        self.modelo = modelo
        self.rutas_configuradas = 0
        self.limite = limite

    def agregar_ruta(self, cantidad):
        # Validar cantidad valida
        if cantidad <= 0:
            print(f"Cantidad invalida: {cantidad}")
            return False

        # Validar limite
        nuevo_total = self.rutas_configuradas + cantidad
        if nuevo_total > self.limite:
            print(f"No se pueden agregar {cantidad} rutas. Limite: {self.limite}")
            return False

        # Si pasa las validaciones, agregamos
        self.rutas_configuradas = nuevo_total
        return True

    def reportar(self):
        print(f"IP: {self.ip}, Modelo: {self.modelo}, Rutas: {self.rutas_configuradas}/{self.limite}")


r2 = RouterMejorado("192.168.1.1", "Cisco-2960", limite=10)
r2.agregar_ruta(2)        # OK -> 2 rutas
r2.agregar_ruta(4)        # OK -> 6 rutas
r2.agregar_ruta(1)        # OK -> 7 rutas
r2.agregar_ruta(-3)       # Rechaza
r2.agregar_ruta(5)        # Rechaza (7+5=12 supera el limite de 10)
r2.agregar_ruta(3)        # OK -> 10 rutas
r2.reportar()
# Salida esperada:
# Cantidad invalida: -3
# No se pueden agregar 5 rutas. Limite: 10
# IP: 192.168.1.1, Modelo: Cisco-2960, Rutas: 10/10