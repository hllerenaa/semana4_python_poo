# =============================================================================
#  PILAR 4 DE 4  -  POLIMORFISMO
#  Misma orden, distinto resultado segun el tipo de objeto.
#
#  IDEA CLAVE:
#  Le dices "habla" a un perro y ladra. Le dices "habla" a un gato y maulla.
#  MISMA orden ("habla"), distinto resultado.
#  En programacion: cada subclase define su propio metodo y cuando lo llamas
#  sobre un objeto, CADA UNO responde a su manera.
#
#  POR QUE ES UTIL:
#  Sin polimorfismo tendrias que llenar tu codigo de if/elif/else preguntando
#  el tipo. Con polimorfismo, llamas un metodo y cada clase sabe que hacer.
# =============================================================================


# -----------------------------------------------------------------------------
# EJEMPLO 1  -  El clasico de los animales
# -----------------------------------------------------------------------------

print("=== Polimorfismo basico: animales ===")

class Animal:
    """Clase base."""
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        """Cada hija va a SOBRESCRIBIR este metodo."""
        print(f"{self.nombre} hace un sonido generico")


class Perro(Animal):
    def hablar(self):
        print(f"{self.nombre}: Guau!")

class Gato(Animal):
    def hablar(self):
        print(f"{self.nombre}: Miau!")

class Vaca(Animal):
    def hablar(self):
        print(f"{self.nombre}: Muuu!")


# OBSERVACION: el truco del polimorfismo esta aqui.
# Mezclamos perros, gatos y vacas en UNA lista.
animales = [
    Perro("Rocky"),
    Gato("Luna"),
    Vaca("Margarita"),
    Perro("Toby"),
]

# OBSERVACION: misma llamada (a.hablar()), cada uno responde a SU manera.
# Sin polimorfismo tendrias que hacer if/elif para cada tipo.
for a in animales:
    a.hablar()


# -----------------------------------------------------------------------------
# EJEMPLO 2  -  Sin polimorfismo (la version FEA)
# -----------------------------------------------------------------------------

print("\n=== Sin polimorfismo: codigo lleno de IF ===")

# OBSERVACION: imagina que NO usaramos polimorfismo.
# Tendrias que hacer algo asi:

class PerroSimple:
    def __init__(self, nombre):
        self.nombre = nombre

class GatoSimple:
    def __init__(self, nombre):
        self.nombre = nombre

# Funcion suelta que tiene que preguntar el tipo:
def hacer_hablar(animal):
    if isinstance(animal, PerroSimple):
        print(f"{animal.nombre}: Guau!")
    elif isinstance(animal, GatoSimple):
        print(f"{animal.nombre}: Miau!")
    # OBSERVACION: si agregas Vaca, Cerdo, Pato... esta funcion crece SIN PARAR.

hacer_hablar(PerroSimple("Max"))
hacer_hablar(GatoSimple("Pelusa"))

# OBSERVACION DIDACTICA: comparalo con el ejemplo 1. Cual prefieres mantener?


# -----------------------------------------------------------------------------
# EJEMPLO 3  -  Polimorfismo en dispositivos de red (caso real)
# -----------------------------------------------------------------------------

print("\n=== Polimorfismo en una red ===")

class Dispositivo:
    """Clase base para todo dispositivo."""
    def __init__(self, ip):
        self.ip = ip

    def reportar(self):
        print(f"Dispositivo {self.ip}")


class Router(Dispositivo):
    def __init__(self, ip, num_rutas):
        super().__init__(ip)
        self.num_rutas = num_rutas

    def reportar(self):
        print(f"Router {self.ip}: {self.num_rutas} rutas configuradas")


class Switch(Dispositivo):
    def __init__(self, ip, num_vlans):
        super().__init__(ip)
        self.num_vlans = num_vlans

    def reportar(self):
        print(f"Switch {self.ip}: {self.num_vlans} VLANs activas")


class Firewall(Dispositivo):
    def __init__(self, ip, num_reglas):
        super().__init__(ip)
        self.num_reglas = num_reglas

    def reportar(self):
        print(f"Firewall {self.ip}: {self.num_reglas} reglas aplicadas")


class AccessPoint(Dispositivo):
    def __init__(self, ip, ssid):
        super().__init__(ip)
        self.ssid = ssid

    def reportar(self):
        print(f"AccessPoint {self.ip}: SSID '{self.ssid}'")


# OBSERVACION: la red es heterogenea (varios tipos mezclados).
red = [
    Router("10.0.0.1", num_rutas=8),
    Switch("10.0.0.2", num_vlans=5),
    Firewall("10.0.0.3", num_reglas=42),
    AccessPoint("10.0.0.4", ssid="ISTER-WiFi"),
    Switch("10.0.0.5", num_vlans=3),
    Router("10.0.0.6", num_rutas=12),
]

# OBSERVACION: UN solo bucle, sin if/elif. Cada objeto responde a SU manera.
print("Reporte de toda la red:")
for d in red:
    d.reportar()

# OBSERVACION DIDACTICA: si mañana agregas un tipo nuevo (ej: Servidor),
# solo defines su clase con su reportar(). El bucle de arriba NO cambia.


# -----------------------------------------------------------------------------
# EJEMPLO 4  -  Polimorfismo con figuras geometricas
# -----------------------------------------------------------------------------

print("\n=== Polimorfismo en figuras geometricas ===")

class Figura:
    def area(self):
        return 0     # se sobrescribira

    def descripcion(self):
        return f"Figura con area {self.area():.2f}"


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14159 * self.radio ** 2


class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto


class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2


figuras = [
    Circulo(5),
    Rectangulo(4, 6),
    Triangulo(3, 8),
    Circulo(2),
]

# OBSERVACION: misma llamada f.descripcion(), cada figura calcula su area.
for f in figuras:
    print(f.descripcion())

# OBSERVACION TECNICA: en Figura.descripcion(), self.area() llama al area()
# de la subclase concreta (Circulo, Rectangulo, etc.). Esto es DESPACHO
# DINAMICO: Python elige el metodo correcto en tiempo de ejecucion.


# -----------------------------------------------------------------------------
# EJEMPLO 5  -  Polimorfismo con notificaciones
# -----------------------------------------------------------------------------

print("\n=== Polimorfismo en notificaciones ===")

class Notificacion:
    def __init__(self, destinatario, mensaje):
        self.destinatario = destinatario
        self.mensaje = mensaje

    def enviar(self):
        raise NotImplementedError("Cada subclase debe implementar enviar()")


class NotificacionEmail(Notificacion):
    def enviar(self):
        print(f"  EMAIL a {self.destinatario}: {self.mensaje}")


class NotificacionSMS(Notificacion):
    def enviar(self):
        print(f"  SMS a {self.destinatario}: {self.mensaje[:50]}...")


class NotificacionPush(Notificacion):
    def enviar(self):
        print(f"  PUSH a {self.destinatario}: {self.mensaje}")


# Procesamos una cola de notificaciones de tipos mezclados.
cola = [
    NotificacionEmail("hector@ister.edu.ec", "Tu tarea fue calificada"),
    NotificacionSMS("0987654321", "Codigo de verificacion: 4521"),
    NotificacionPush("dispositivo-001", "Backup completado"),
    NotificacionEmail("maria@ister.edu.ec", "Nueva nota disponible"),
]

print("Procesando cola de notificaciones:")
for n in cola:
    n.enviar()


# =============================================================================
#  PARA PRACTICAR
# =============================================================================
# Crea una clase base Empleado con:
#   - __init__(self, nombre)
#   - calcular_salario(self): retorna 0 (se sobrescribira)
#
# Crea tres clases hijas:
#   - EmpleadoFijo: salario fijo de 1500
#   - EmpleadoPorHora: salario = horas_trabajadas * 15
#   - EmpleadoVentas: salario = base + comision (donde base=500 y
#     comision = ventas * 0.10)
#
# Crea una lista mixta de los 3 tipos y muestra el salario de cada uno
# con UN solo bucle (sin if/elif). Ese es el poder del polimorfismo.
# =============================================================================
