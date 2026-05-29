# =============================================================================
#  SEMANA 4  |  TIPO 2 DE 5  -  METODO NORMAL  (con self)
#  Funciones dentro de una clase que reciben self como primer parametro.
#
#  Asignatura:  Lenguaje de Programacion Python
#  Carrera:     Infraestructura de Redes y Ciberseguridad
#  Docente:     Ing. Hector Llerena, MSc
#  Periodo:     2026-1
#
#  QUE ES:     Funcion dentro de una clase cuyo primer parametro es self.
#              Por self accede a los atributos del objeto.
#  CUANDO:     Cuando la operacion DEPENDE de los datos del objeto.
#  COMO LLAMAR: objeto.metodo(argumentos)
#
#  Convencion de comentarios:
#    OBSERVACION            -> que hace el codigo
#    OBSERVACION DIDACTICA  -> pregunta para el estudiante
#    OBSERVACION TECNICA    -> detalle sutil de Python
# =============================================================================


# =============================================================================
#  EJERCICIO 01  -  clase Dispositivo con metodos basicos
# =============================================================================

class Dispositivo:
    """Modela un dispositivo de red con IP, MAC y estado."""

    def __init__(self, ip, mac):
        # OBSERVACION: __init__ tambien es un metodo normal (recibe self).
        # Es el constructor: se ejecuta al crear el objeto.
        self.ip = ip
        self.mac = mac
        self.activo = False

    def encender(self):
        """Marca el dispositivo como activo."""
        self.activo = True
        print(f"[{self.ip}] encendido")

    def apagar(self):
        """Marca el dispositivo como inactivo."""
        self.activo = False
        print(f"[{self.ip}] apagado")

    def reportar(self):
        """Imprime el estado actual del dispositivo."""
        estado = "ACTIVO" if self.activo else "INACTIVO"
        print(f"{self.ip} / {self.mac} -> {estado}")

# OBSERVACION: creo el objeto y opero sobre el con sus metodos.
print("=== Ejercicio 01: Dispositivo ===")
router = Dispositivo("10.0.0.1", "AA:BB:CC:01")
router.reportar()        # INACTIVO
router.encender()
router.reportar()        # ACTIVO
router.apagar()
router.reportar()        # INACTIVO

# OBSERVACION DIDACTICA: cuantas veces tuve que pasar la IP a los metodos?
# Compara con la version "funcion suelta" donde tendrias que pasar ip cada vez.
# OBSERVACION TECNICA: cuando llamo router.reportar(), Python lo traduce
# internamente a Dispositivo.reportar(router). Por eso self es el primer parametro.


# =============================================================================
#  EJERCICIO 02  -  clase Usuario con control de intentos de login
# =============================================================================

class Usuario:
    """Usuario con clave y control de intentos fallidos."""

    def __init__(self, nombre, clave):
        self.nombre = nombre
        self._clave = clave            # protegido (uso interno)
        self._intentos = 0
        self.bloqueado = False

    def autenticar(self, intento):
        """Compara el intento con la clave guardada."""
        if self.bloqueado:
            print(f"[{self.nombre}] cuenta bloqueada")
            return False
        if intento == self._clave:
            self._intentos = 0          # reset al exito
            print(f"[{self.nombre}] login exitoso")
            return True
        self._intentos += 1
        print(f"[{self.nombre}] intento fallido ({self._intentos}/3)")
        if self._intentos >= 3:
            self.bloqueado = True
            print(f"[{self.nombre}] cuenta bloqueada por 3 intentos fallidos")
        return False

    def desbloquear(self):
        """Resetea el contador y desbloquea la cuenta."""
        self._intentos = 0
        self.bloqueado = False
        print(f"[{self.nombre}] cuenta desbloqueada")

print("\n=== Ejercicio 02: Usuario con login ===")
hector = Usuario("hector", "Pass2026")
hector.autenticar("admin")        # fallido 1
hector.autenticar("12345")        # fallido 2
hector.autenticar("Pass2026")     # exito (resetea contador)
hector.autenticar("xxxx")         # fallido 1
hector.autenticar("yyyy")         # fallido 2
hector.autenticar("zzzz")         # fallido 3 -> bloqueado
hector.autenticar("Pass2026")     # ya esta bloqueado, ni siquiera intenta
hector.desbloquear()
hector.autenticar("Pass2026")     # ahora si

# OBSERVACION DIDACTICA: el contador _intentos esta en el OBJETO o fuera de el?
# OBSERVACION TECNICA: cada Usuario tiene su PROPIO _intentos. Si creo otra
# instancia Usuario("maria", ...), el contador de maria es independiente.


# =============================================================================
#  EJERCICIO 03  -  clase Conexion con duracion calculada
# =============================================================================

class Conexion:
    """Modela una conexion de red entre origen y destino."""

    def __init__(self, origen, destino, hora_inicio):
        self.origen = origen
        self.destino = destino
        self.hora_inicio = hora_inicio   # en segundos desde epoca
        self.hora_fin = None
        self.abierta = True

    def cerrar(self, hora_fin):
        """Marca la conexion como cerrada y guarda la hora."""
        self.hora_fin = hora_fin
        self.abierta = False
        print(f"Conexion {self.origen} -> {self.destino} cerrada")

    def duracion(self):
        """Retorna la duracion en segundos. 0 si sigue abierta."""
        if self.abierta or self.hora_fin is None:
            return 0
        return self.hora_fin - self.hora_inicio

    def resumen(self):
        """Imprime un resumen del estado de la conexion."""
        estado = "abierta" if self.abierta else f"cerrada ({self.duracion()}s)"
        print(f"{self.origen} -> {self.destino}  [{estado}]")

print("\n=== Ejercicio 03: Conexion con duracion ===")
c1 = Conexion("192.168.1.10", "8.8.8.8", hora_inicio=1700000000)
c1.resumen()                              # abierta
c1.cerrar(hora_fin=1700000045)
c1.resumen()                              # cerrada (45s)
print("Duracion:", c1.duracion(), "segundos")

# OBSERVACION DIDACTICA: el metodo duracion() funciona ANTES de cerrar?
# OBSERVACION TECNICA: el metodo trabaja con los atributos del objeto y
# devuelve diferente resultado segun el estado interno. Sin clase, tendrias
# que pasar todos los datos por parametro cada vez.


# =============================================================================
#  EJERCICIO 04  -  clase LogEntry con formato y prioridad
# =============================================================================

class LogEntry:
    """Una entrada de log con nivel, mensaje y fuente."""

    def __init__(self, nivel, mensaje, fuente):
        self.nivel = nivel.upper()       # INFO, WARN, ERROR, CRITICAL
        self.mensaje = mensaje
        self.fuente = fuente

    def formatear(self):
        """Retorna el log en formato estandar para archivo."""
        return f"[{self.nivel:8}] {self.fuente}: {self.mensaje}"

    def es_critico(self):
        """True si requiere atencion inmediata."""
        return self.nivel in ("ERROR", "CRITICAL")

    def notificar(self):
        """Muestra el log y avisa si es critico."""
        print(self.formatear())
        if self.es_critico():
            print(">>> ATENCION: requiere intervencion <<<")

print("\n=== Ejercicio 04: LogEntry ===")
log1 = LogEntry("info",     "Sistema iniciado",          "main.py")
log2 = LogEntry("warning",  "Memoria al 80%",            "monitor.py")
log3 = LogEntry("error",    "No se conecto a BD",        "db.py")
log4 = LogEntry("critical", "Brecha de seguridad",       "firewall")

log1.notificar()
log2.notificar()
log3.notificar()
log4.notificar()

# OBSERVACION DIDACTICA: por que es_critico() puede llamarse sin parametros?
# OBSERVACION TECNICA: porque ya tiene self.nivel guardado en el objeto.
# Si fuera funcion suelta, tendrias que llamar: es_critico(log.nivel).


# =============================================================================
#  ZONA INTERACTIVA  (descomentar en clase)
# =============================================================================
# DESCOMENTAR EN CLASE:
#
# nombre = input("Nombre de usuario: ")
# clave  = input("Define una clave: ")
# u = Usuario(nombre, clave)
# while not u.bloqueado:
#     intento = input(f"Ingresa la clave de {nombre} (q para salir): ")
#     if intento == "q":
#         break
#     u.autenticar(intento)
#
# OBSERVACION DIDACTICA: cuantos atributos del objeto se actualizan en cada
# llamada a autenticar()?


# =============================================================================
#  FIN DEL ARCHIVO  -  02_metodo_normal.py
# =============================================================================
