# =============================================================================
#  SEMANA 4  |  TIPO 1 DE 5  -  FUNCION SUELTA
#  Funciones que viven en el archivo, fuera de cualquier clase.
#
#  Asignatura:  Lenguaje de Programacion Python
#  Carrera:     Infraestructura de Redes y Ciberseguridad
#  Docente:     Ing. Hector Llerena, MSc
#  Periodo:     2026-1
#
#  QUE ES:     Bloque de codigo con nombre que recibe parametros y devuelve
#              un resultado. Vive fuera de cualquier clase.
#  CUANDO:     Cuando solo necesitas procesar datos sin guardar estado.
#  COMO LLAMAR: nombre_funcion(argumentos)
#
#  Convencion de comentarios:
#    OBSERVACION            -> que hace el codigo
#    OBSERVACION DIDACTICA  -> pregunta para el estudiante
#    OBSERVACION TECNICA    -> detalle sutil de Python
# =============================================================================


# =============================================================================
#  EJERCICIO 01  -  validar_ip
#  Valida que una direccion sea una IPv4 correcta.
# =============================================================================

def validar_ip(direccion):
    """Retorna True si la direccion es una IPv4 valida."""
    # OBSERVACION: dividimos por punto y verificamos 4 octetos.
    partes = direccion.split(".")
    if len(partes) != 4:
        return False
    for parte in partes:
        if not parte.isdigit():
            return False
        if not 0 <= int(parte) <= 255:
            return False
    return True

# OBSERVACION: pruebas con datos validos y no validos.
print("=== Ejercicio 01: validar_ip ===")
print(validar_ip("192.168.1.10"))      # True
print(validar_ip("10.0.0.1"))           # True
print(validar_ip("192.168.300.1"))      # False - octeto > 255
print(validar_ip("192.168.1"))          # False - faltan octetos
print(validar_ip("a.b.c.d"))            # False - no son numeros

# OBSERVACION DIDACTICA: que pasa si pasas un entero en lugar de string?
# Pruebalo: validar_ip(192168110)  -> dara AttributeError
# OBSERVACION TECNICA: una funcion suelta no tiene control sobre el tipo de
# entrada. En contextos profesionales se valida el tipo o se usa type hints.


# =============================================================================
#  EJERCICIO 02  -  es_puerto_valido
#  Verifica si un numero esta en el rango valido de puertos TCP/UDP.
# =============================================================================

def es_puerto_valido(puerto):
    """Retorna True si el puerto esta en rango 1-65535."""
    return 1 <= puerto <= 65535

print("\n=== Ejercicio 02: es_puerto_valido ===")
print(es_puerto_valido(443))            # True
print(es_puerto_valido(22))             # True
print(es_puerto_valido(70000))          # False - excede maximo
print(es_puerto_valido(0))              # False - 0 no es valido
print(es_puerto_valido(-1))             # False - negativo

# OBSERVACION DIDACTICA: por que el puerto 0 no es valido?
# OBSERVACION TECNICA: en TCP/UDP el puerto 0 es reservado para "asignacion
# automatica" del sistema operativo. Por convencion no se usa.


# =============================================================================
#  EJERCICIO 03  -  nombre_servicio
#  Mapea un numero de puerto bien conocido a su nombre de servicio.
# =============================================================================

def nombre_servicio(puerto):
    """Devuelve el nombre del servicio para un puerto bien conocido."""
    # OBSERVACION: tabla de puertos comunes (IANA).
    servicios = {
        20:   "FTP-DATA",
        21:   "FTP",
        22:   "SSH",
        23:   "Telnet",
        25:   "SMTP",
        53:   "DNS",
        80:   "HTTP",
        110:  "POP3",
        143:  "IMAP",
        443:  "HTTPS",
        465:  "SMTPS",
        993:  "IMAPS",
        995:  "POP3S",
        3306: "MySQL",
        3389: "RDP",
        5432: "PostgreSQL",
        8080: "HTTP-Proxy",
    }
    return servicios.get(puerto, "Desconocido")

print("\n=== Ejercicio 03: nombre_servicio ===")
print(nombre_servicio(22))              # SSH
print(nombre_servicio(443))             # HTTPS
print(nombre_servicio(3306))            # MySQL
print(nombre_servicio(9999))            # Desconocido
print(nombre_servicio(80))              # HTTP

# OBSERVACION DIDACTICA: por que usamos .get(puerto, 'Desconocido') en lugar
# de servicios[puerto]?
# OBSERVACION TECNICA: servicios[puerto] lanzaria KeyError si el puerto no
# existe. .get() es seguro: si no existe la clave, devuelve el valor por
# defecto sin error.


# =============================================================================
#  EJERCICIO 04  -  construir_url  (con valores por defecto)
#  Arma una URL a partir de host, puerto, esquema y ruta.
# =============================================================================

def construir_url(host, puerto=80, https=False, ruta="/"):
    """Construye una URL en formato esquema://host:puerto/ruta."""
    esquema = "https" if https else "http"
    return f"{esquema}://{host}:{puerto}{ruta}"

print("\n=== Ejercicio 04: construir_url ===")
print(construir_url("ister.edu.ec"))                       # http://ister.edu.ec:80/
print(construir_url("ister.edu.ec", 443, https=True))      # https://ister.edu.ec:443/
print(construir_url("api.local", 8080, ruta="/v1/users"))  # http://api.local:8080/v1/users
print(construir_url("test.local", https=True, puerto=8443))# por NOMBRE en cualquier orden

# OBSERVACION DIDACTICA: que pasa si llamo construir_url() sin argumentos?
# OBSERVACION TECNICA: dara TypeError porque host es OBLIGATORIO (no tiene
# valor por defecto). Los parametros con default deben ir despues de los
# obligatorios en la firma de la funcion.


# =============================================================================
#  ZONA INTERACTIVA  (descomentar en clase)
# =============================================================================
# DESCOMENTAR EN CLASE:
#
# ip = input("Ingrese una IP a validar: ")
# if validar_ip(ip):
#     puerto = int(input("Ingrese el puerto: "))
#     if es_puerto_valido(puerto):
#         servicio = nombre_servicio(puerto)
#         url = construir_url(ip, puerto, https=(puerto == 443))
#         print(f"Servicio: {servicio}")
#         print(f"URL:      {url}")
#     else:
#         print("Puerto invalido")
# else:
#     print("IP invalida")
#
# OBSERVACION DIDACTICA: cuantas funciones suelta participan en esta validacion?


# =============================================================================
#  FIN DEL ARCHIVO  -  01_funcion_suelta.py
# =============================================================================
