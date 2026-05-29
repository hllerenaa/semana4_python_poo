# =============================================================================
#  SEMANA 4  |  TIPO 3 DE 5  -  @property
#  Metodos que se USAN como atributos pero ejecutan codigo.
#
#  Asignatura:  Lenguaje de Programacion Python
#  Carrera:     Infraestructura de Redes y Ciberseguridad
#  Docente:     Ing. Hector Llerena, MSc
#  Periodo:     2026-1
#
#  QUE ES:     Decorador que convierte un metodo en algo que se ve como
#              atributo pero ejecuta logica de validacion o calculo.
#  CUANDO:     1) Validar datos al asignarse (con setter).
#              2) Calcular valores a partir de otros atributos.
#  COMO LLAMAR: objeto.atributo            (sin parentesis!)
#              objeto.atributo = valor    (dispara el setter)
#
#  Convencion de comentarios:
#    OBSERVACION            -> que hace el codigo
#    OBSERVACION DIDACTICA  -> pregunta para el estudiante
#    OBSERVACION TECNICA    -> detalle sutil de Python
# =============================================================================


# =============================================================================
#  EJERCICIO 01  -  @property con validacion: clave robusta
# =============================================================================

class UsuarioSeguro:
    """Usuario cuya clave debe cumplir reglas minimas de seguridad."""

    def __init__(self, nombre, clave):
        self.nombre = nombre
        self.clave = clave            # ATENCION: esta linea llama al setter!

    @property
    def clave(self):
        """Getter: devuelve la clave guardada (uso interno)."""
        return self._clave

    @clave.setter
    def clave(self, valor):
        """Setter: valida y guarda la clave."""
        if len(valor) < 8:
            raise ValueError("Clave demasiado corta (minimo 8)")
        if not any(c.isupper() for c in valor):
            raise ValueError("Falta una mayuscula")
        if not any(c.isdigit() for c in valor):
            raise ValueError("Falta un numero")
        self._clave = valor

print("=== Ejercicio 01: @property con validacion ===")
u = UsuarioSeguro("hector", "Pass2026")
print(f"Clave aceptada: {u.clave}")

# OBSERVACION: el usuario USA u.clave como si fuera un atributo, pero por
# detras se ejecuta el setter con su logica de validacion.
intentos_malos = ["123", "claveSinNumero", "PASSWORD1", "Pass2026"]
for intento in intentos_malos:
    try:
        u.clave = intento
        print(f"  Clave '{intento}' aceptada (longitud={len(intento)})")
    except ValueError as e:
        print(f"  Clave '{intento}' rechazada: {e}")

# OBSERVACION DIDACTICA: la sintaxis u.clave = '123' parece una asignacion
# normal, pero ejecuta codigo. Eso es lo que diferencia @property.
# OBSERVACION TECNICA: el atributo real se llama self._clave (con guion bajo).
# self.clave es el property que controla el acceso a self._clave.


# =============================================================================
#  EJERCICIO 02  -  @property con validacion: IP correcta
# =============================================================================

class HostRed:
    """Host de red con IP validada al asignarse."""

    def __init__(self, nombre, ip):
        self.nombre = nombre
        self.ip = ip                  # dispara el setter

    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, valor):
        # OBSERVACION: validacion completa antes de aceptar el valor.
        partes = valor.split(".")
        if len(partes) != 4:
            raise ValueError(f"IP debe tener 4 octetos: {valor}")
        for parte in partes:
            if not parte.isdigit():
                raise ValueError(f"Octeto no numerico: {parte}")
            if not 0 <= int(parte) <= 255:
                raise ValueError(f"Octeto fuera de rango: {parte}")
        self._ip = valor

print("\n=== Ejercicio 02: @property valida IP ===")
h = HostRed("router-core", "10.0.0.1")
print(f"Host creado con IP: {h.ip}")

# OBSERVACION: intentamos varias IPs malas, todas deben ser rechazadas.
ips_malas = ["192.168.1", "192.168.1.300", "a.b.c.d", "10.0.0.5"]
for ip_test in ips_malas:
    try:
        h.ip = ip_test
        print(f"  IP '{ip_test}' aceptada -> ahora h.ip = {h.ip}")
    except ValueError as e:
        print(f"  IP '{ip_test}' rechazada: {e}")

# OBSERVACION DIDACTICA: cuando se ejecuto la validacion al crear el objeto?
# OBSERVACION TECNICA: dentro de __init__, la linea "self.ip = ip" no asigna
# directamente: Python ve que existe el setter @ip.setter y lo invoca.


# =============================================================================
#  EJERCICIO 03  -  @property CALCULADO: URL desde host+puerto+https
# =============================================================================

class ServicioWeb:
    """Servicio web cuya URL se calcula a partir de sus atributos."""

    def __init__(self, host, puerto=80, https=False):
        self.host = host
        self.puerto = puerto
        self.https = https

    @property
    def url(self):
        """Calculado: NO se guarda, se construye al pedirlo."""
        esquema = "https" if self.https else "http"
        return f"{esquema}://{self.host}:{self.puerto}"

    @property
    def es_seguro(self):
        """Calculado: True si usa HTTPS en el puerto estandar."""
        return self.https and self.puerto == 443

print("\n=== Ejercicio 03: @property calculado ===")
s = ServicioWeb("ister.edu.ec", 443, https=True)
print(f"URL inicial:    {s.url}")
print(f"Es seguro?:     {s.es_seguro}")

# OBSERVACION: si cambio un atributo, el property reflejara automaticamente.
s.puerto = 8443
print(f"\nDespues de cambiar puerto a 8443:")
print(f"URL nueva:      {s.url}")
print(f"Es seguro?:     {s.es_seguro}")     # ya no, porque puerto != 443

s.https = False
s.puerto = 80
print(f"\nDespues de pasar a HTTP estandar:")
print(f"URL nueva:      {s.url}")
print(f"Es seguro?:     {s.es_seguro}")

# OBSERVACION DIDACTICA: cuantos atributos guarda el objeto realmente?
# OBSERVACION TECNICA: solo 3 (host, puerto, https). url y es_seguro NO se
# guardan: se calculan cada vez que se piden. Por eso no quedan "obsoletos".


# =============================================================================
#  EJERCICIO 04  -  @property CALCULADO: estadisticas de logs
# =============================================================================

class RegistroLogs:
    """Coleccion de logs con estadisticas calculadas dinamicamente."""

    def __init__(self):
        self.entradas = []          # lista de tuplas (nivel, mensaje)

    def agregar(self, nivel, mensaje):
        """Agrega una entrada al registro."""
        self.entradas.append((nivel.upper(), mensaje))

    @property
    def total(self):
        """Total de entradas registradas."""
        return len(self.entradas)

    @property
    def cantidad_errores(self):
        """Cantidad de logs nivel ERROR o CRITICAL."""
        return sum(1 for nivel, _ in self.entradas
                   if nivel in ("ERROR", "CRITICAL"))

    @property
    def porcentaje_critico(self):
        """Porcentaje de logs criticos sobre el total."""
        if self.total == 0:
            return 0.0
        return (self.cantidad_errores / self.total) * 100

    @property
    def tiene_alertas(self):
        """True si hay al menos un log critico."""
        return self.cantidad_errores > 0

print("\n=== Ejercicio 04: @property estadisticas ===")
reg = RegistroLogs()
reg.agregar("info",     "Sistema iniciado")
reg.agregar("info",     "Conexion BD OK")
reg.agregar("warning",  "Memoria al 75%")
reg.agregar("error",    "Fallo en autenticacion")
reg.agregar("critical", "Brecha detectada")

print(f"Total de entradas:    {reg.total}")
print(f"Cantidad de errores:  {reg.cantidad_errores}")
print(f"Porcentaje critico:   {reg.porcentaje_critico:.1f}%")
print(f"Tiene alertas?:       {reg.tiene_alertas}")

# OBSERVACION: agrego un log mas y todos los @property se recalculan solos.
reg.agregar("info", "Backup completado")
print(f"\nTras agregar 1 log info:")
print(f"Total:                {reg.total}")
print(f"Porcentaje critico:   {reg.porcentaje_critico:.1f}%")

# OBSERVACION DIDACTICA: por que el porcentaje cambia automaticamente sin
# que yo llame ningun metodo de actualizacion?
# OBSERVACION TECNICA: porque @property RE-EJECUTA el codigo cada vez que
# se accede. No es un valor cacheado: es un calculo en vivo.


# =============================================================================
#  ZONA INTERACTIVA  (descomentar en clase)
# =============================================================================
# DESCOMENTAR EN CLASE:
#
# nombre = input("Nombre del usuario: ")
# while True:
#     clave = input("Define una clave segura (8+ chars, mayus, num): ")
#     try:
#         u = UsuarioSeguro(nombre, clave)
#         print("Clave aceptada!")
#         break
#     except ValueError as e:
#         print(f"Rechazada: {e}. Intenta de nuevo.")
#
# OBSERVACION DIDACTICA: el bucle se sale solo cuando el setter NO lanza
# excepcion. Quien decide cuando la clave es valida?


# =============================================================================
#  FIN DEL ARCHIVO  -  03_property.py
# =============================================================================
