# =============================================================================
#  PILAR 3 DE 4  -  HERENCIA
#  Una clase HEREDA todo lo de otra. Como un hijo que hereda de su padre.
#
#  IDEA CLAVE:
#  Si tienes 10 tipos de dispositivos y todos tienen IP, MAC, encender() y
#  apagar(), no escribas eso 10 veces. Hazlo UNA vez en una clase padre
#  (Dispositivo). Las 10 clases hijas (Router, Switch, etc.) lo reciben gratis.
#
#  SINTAXIS:
#    class Hija(Padre):    <-- entre parentesis pones la clase padre
#        ...
#
#    super().__init__(...) <-- llama al __init__ del padre
# =============================================================================


# -----------------------------------------------------------------------------
# EJEMPLO 1  -  SIN herencia  (lo que pasa cuando no la usas)
# -----------------------------------------------------------------------------

print("=== SIN herencia: codigo repetido ===")

class RouterSinHerencia:
    def __init__(self, ip, mac):
        self.ip = ip
        self.mac = mac
        self.activo = False
    def encender(self):
        self.activo = True
    def apagar(self):
        self.activo = False

class SwitchSinHerencia:
    def __init__(self, ip, mac):
        self.ip = ip                  # REPETIDO
        self.mac = mac                # REPETIDO
        self.activo = False           # REPETIDO
    def encender(self):               # REPETIDO
        self.activo = True
    def apagar(self):                 # REPETIDO
        self.activo = False

# OBSERVACION: copie pegue casi todo. Si mañana cambio encender(), tengo
# que cambiarlo en TODAS las clases.


# -----------------------------------------------------------------------------
# EJEMPLO 2  -  CON herencia  (la version limpia)
# -----------------------------------------------------------------------------

print("\n=== CON herencia: codigo limpio ===")

class Dispositivo:
    """Clase PADRE. Tiene lo comun a todos los dispositivos."""

    def __init__(self, ip, mac):
        self.ip = ip
        self.mac = mac
        self.activo = False

    def encender(self):
        self.activo = True
        print(f"{self.ip} encendido")

    def apagar(self):
        self.activo = False
        print(f"{self.ip} apagado")

    def reportar(self):
        estado = "ACTIVO" if self.activo else "INACTIVO"
        print(f"  {self.ip} / {self.mac} -> {estado}")


# OBSERVACION: Router HEREDA de Dispositivo.
# Recibe ip, mac, encender(), apagar() y reportar() GRATIS.
class Router(Dispositivo):
    """Router HEREDA todo de Dispositivo."""

    def __init__(self, ip, mac, num_rutas):
        # OBSERVACION: super() llama al __init__ del padre.
        super().__init__(ip, mac)
        # Y agregamos LO PROPIO del Router:
        self.num_rutas = num_rutas

    def mostrar_rutas(self):
        """Metodo propio del Router (no esta en Dispositivo)."""
        print(f"  Router {self.ip} tiene {self.num_rutas} rutas")


# OBSERVACION: Switch tambien hereda.
class Switch(Dispositivo):
    """Switch HEREDA de Dispositivo, agrega lo propio."""

    def __init__(self, ip, mac, num_vlans):
        super().__init__(ip, mac)
        self.num_vlans = num_vlans

    def mostrar_vlans(self):
        print(f"  Switch {self.ip} tiene {self.num_vlans} VLANs")


# Usamos las clases hijas
r = Router("10.0.0.1", "AA:BB:01", num_rutas=8)
s = Switch("10.0.0.2", "AA:BB:02", num_vlans=5)

# OBSERVACION: r.encender() funciona aunque NO esta definido en Router.
# Funciona porque LO HEREDA de Dispositivo.
r.encender()
r.reportar()
r.mostrar_rutas()

s.encender()
s.reportar()
s.mostrar_vlans()


# -----------------------------------------------------------------------------
# EJEMPLO 3  -  Tres niveles de herencia (cadena)
# -----------------------------------------------------------------------------

print("\n=== Cadena de herencia: 3 niveles ===")

class Vehiculo:
    """Nivel 1: cualquier vehiculo."""
    def __init__(self, marca):
        self.marca = marca

    def encender(self):
        print(f"{self.marca}: vroom!")


class Auto(Vehiculo):
    """Nivel 2: un auto ES UN vehiculo."""
    def __init__(self, marca, modelo):
        super().__init__(marca)
        self.modelo = modelo

    def cerrar_puertas(self):
        print(f"{self.marca} {self.modelo}: puertas cerradas")


class AutoElectrico(Auto):
    """Nivel 3: un auto electrico ES UN auto (que ES UN vehiculo)."""
    def __init__(self, marca, modelo, bateria_kwh):
        super().__init__(marca, modelo)
        self.bateria_kwh = bateria_kwh

    def cargar(self):
        print(f"{self.marca} {self.modelo}: cargando bateria ({self.bateria_kwh} kWh)")


# OBSERVACION: el AutoElectrico tiene TODO de las 3 clases.
tesla = AutoElectrico("Tesla", "Model 3", 75)
tesla.encender()         # heredado de Vehiculo
tesla.cerrar_puertas()   # heredado de Auto
tesla.cargar()           # propio de AutoElectrico


# -----------------------------------------------------------------------------
# EJEMPLO 4  -  Sobrescribir (overriding) un metodo del padre
# -----------------------------------------------------------------------------

print("\n=== Sobrescribir metodos del padre ===")

class Animal:
    def hacer_sonido(self):
        print("Sonido generico")

class Perro(Animal):
    # OBSERVACION: Perro REEMPLAZA el metodo del padre con uno propio.
    def hacer_sonido(self):
        print("Guau guau!")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau!")

a = Animal()
p = Perro()
g = Gato()
a.hacer_sonido()   # Sonido generico
p.hacer_sonido()   # Guau guau! (reemplazo el del padre)
g.hacer_sonido()   # Miau!

# OBSERVACION DIDACTICA: cuando una hija define un metodo con el MISMO NOMBRE
# que el padre, el de la hija "gana". Esto se llama sobrescritura y es la
# base del POLIMORFISMO (que veremos en el siguiente archivo).


# =============================================================================
#  PARA PRACTICAR
# =============================================================================
# Crea una clase base Empleado con:
#   - __init__(self, nombre, salario_base)
#   - calcular_salario(self): retorna salario_base
#
# Crea dos clases hijas:
#   - EmpleadoVentas(Empleado): tiene comision; calcular_salario incluye comision
#   - EmpleadoGerente(Empleado): tiene bono; calcular_salario suma el bono
#
# Crea uno de cada y muestra el salario de cada uno.
# =============================================================================
