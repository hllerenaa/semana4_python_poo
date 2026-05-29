# =============================================================================
#  SEMANA 4  |  TIPO 4 DE 5  -  @staticmethod
#  Funciones que viven DENTRO de una clase pero NO usan los datos del objeto.
#
#  Asignatura:  Lenguaje de Programacion Python
#  Carrera:     Infraestructura de Redes y Ciberseguridad
#  Docente:     Ing. Hector Llerena, MSc
#  Periodo:     2026-1
#
#  QUE ES:     Metodo decorado con @staticmethod que NO recibe self ni cls.
#              Funciona como funcion suelta pero vive dentro de la clase.
#  CUANDO:     Cuando una utilidad esta relacionada con la clase, pero NO
#              necesita acceder al objeto para funcionar.
#  COMO LLAMAR: Clase.metodo(argumentos)   (no requiere crear objeto)
#
#  Convencion de comentarios:
#    OBSERVACION            -> que hace el codigo
#    OBSERVACION DIDACTICA  -> pregunta para el estudiante
#    OBSERVACION TECNICA    -> detalle sutil de Python
# =============================================================================


# =============================================================================
#  EJERCICIO 01  -  HerramientasIP: utilidades agrupadas para IP
# =============================================================================

class HerramientasIP:
    """Utilidades estaticas relacionadas con direcciones IP."""

    @staticmethod
    def es_formato_valido(ip):
        """Verifica el formato basico IPv4."""
        partes = ip.split(".")
        if len(partes) != 4:
            return False
        for p in partes:
            if not p.isdigit() or not 0 <= int(p) <= 255:
                return False
        return True

    @staticmethod
    def es_privada(ip):
        """Verifica si esta en rangos RFC 1918."""
        # OBSERVACION: reutiliza la validacion sin crear objeto.
        if not HerramientasIP.es_formato_valido(ip):
            return False
        o1, o2, _, _ = map(int, ip.split("."))
        if o1 == 10:
            return True
        if o1 == 172 and 16 <= o2 <= 31:
            return True
        if o1 == 192 and o2 == 168:
            return True
        return False

    @staticmethod
    def es_loopback(ip):
        """Verifica si es loopback (127.0.0.0/8)."""
        if not HerramientasIP.es_formato_valido(ip):
            return False
        return ip.startswith("127.")

print("=== Ejercicio 01: HerramientasIP ===")
# OBSERVACION: las llamo SIN crear objeto. Solo Clase.metodo(...)
print("Formato valido 10.0.0.1:", HerramientasIP.es_formato_valido("10.0.0.1"))
print("Formato valido 999.0.0.1:", HerramientasIP.es_formato_valido("999.0.0.1"))
print("Es privada 10.0.0.5:    ", HerramientasIP.es_privada("10.0.0.5"))
print("Es privada 8.8.8.8:     ", HerramientasIP.es_privada("8.8.8.8"))
print("Es loopback 127.0.0.1:  ", HerramientasIP.es_loopback("127.0.0.1"))
print("Es loopback 10.0.0.1:   ", HerramientasIP.es_loopback("10.0.0.1"))

# OBSERVACION DIDACTICA: necesite crear un objeto HerramientasIP() para usar
# estas funciones? Cual es la ventaja de agruparlas en una clase?
# OBSERVACION TECNICA: el namespace ayuda. HerramientasIP.es_privada deja
# claro que es para IP. Si fuera funcion suelta es_privada(), podria chocar
# con otra (una "es_privada" para info personal, por ejemplo).


# =============================================================================
#  EJERCICIO 02  -  HerramientasPuerto: validaciones de puerto
# =============================================================================

class HerramientasPuerto:
    """Utilidades estaticas para puertos TCP/UDP."""

    PUERTOS_BIEN_CONOCIDOS = set(range(0, 1024))
    PUERTOS_REGISTRADOS    = set(range(1024, 49152))
    PUERTOS_DINAMICOS      = set(range(49152, 65536))

    @staticmethod
    def es_valido(puerto):
        """True si esta en rango 1-65535."""
        return 1 <= puerto <= 65535

    @staticmethod
    def es_bien_conocido(puerto):
        """True si esta en el rango 0-1023 (IANA system)."""
        return puerto in HerramientasPuerto.PUERTOS_BIEN_CONOCIDOS

    @staticmethod
    def categoria(puerto):
        """Devuelve el nombre de la categoria IANA."""
        if not HerramientasPuerto.es_valido(puerto):
            return "INVALIDO"
        if puerto in HerramientasPuerto.PUERTOS_BIEN_CONOCIDOS:
            return "BIEN_CONOCIDO"
        if puerto in HerramientasPuerto.PUERTOS_REGISTRADOS:
            return "REGISTRADO"
        return "DINAMICO"

print("\n=== Ejercicio 02: HerramientasPuerto ===")
for p in [22, 443, 3306, 8080, 49152, 65535, 70000]:
    categoria = HerramientasPuerto.categoria(p)
    print(f"Puerto {p:5}  ->  categoria: {categoria}")

# OBSERVACION DIDACTICA: por que defini PUERTOS_BIEN_CONOCIDOS fuera de los
# metodos pero dentro de la clase?
# OBSERVACION TECNICA: son atributos de CLASE (no de instancia). Se comparten
# entre todas las llamadas. No se recrean en cada invocacion -> eficiencia.


# =============================================================================
#  EJERCICIO 03  -  HerramientasPassword: evaluar fortaleza de claves
# =============================================================================

class HerramientasPassword:
    """Evaluadores de seguridad de contraseñas (sin estado)."""

    @staticmethod
    def tiene_mayuscula(clave):
        return any(c.isupper() for c in clave)

    @staticmethod
    def tiene_minuscula(clave):
        return any(c.islower() for c in clave)

    @staticmethod
    def tiene_numero(clave):
        return any(c.isdigit() for c in clave)

    @staticmethod
    def tiene_simbolo(clave):
        simbolos = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        return any(c in simbolos for c in clave)

    @staticmethod
    def evaluar_fortaleza(clave):
        """Retorna un puntaje 0-5 y un nombre de nivel."""
        # OBSERVACION: combina las otras utilidades estaticas en una sola.
        puntaje = 0
        if len(clave) >= 8:
            puntaje += 1
        if len(clave) >= 12:
            puntaje += 1
        if HerramientasPassword.tiene_mayuscula(clave):
            puntaje += 1
        if HerramientasPassword.tiene_numero(clave):
            puntaje += 1
        if HerramientasPassword.tiene_simbolo(clave):
            puntaje += 1
        niveles = ["MUY_DEBIL", "DEBIL", "MEDIA", "FUERTE", "MUY_FUERTE", "EXCELENTE"]
        return puntaje, niveles[puntaje]

print("\n=== Ejercicio 03: HerramientasPassword ===")
pruebas = ["123", "admin", "Admin123", "Admin@123", "P@ssw0rd_Largo!"]
for clave in pruebas:
    puntaje, nivel = HerramientasPassword.evaluar_fortaleza(clave)
    print(f"  '{clave:18}'  ->  {puntaje}/5  ({nivel})")

# OBSERVACION DIDACTICA: el metodo evaluar_fortaleza llama a otros @staticmethod
# de la misma clase. Como los referencia?
# OBSERVACION TECNICA: usa HerramientasPassword.tiene_mayuscula(clave) - el
# nombre completo de la clase. NO usa self porque @staticmethod NO recibe self.


# =============================================================================
#  EJERCICIO 04  -  HerramientasRed: utilidades generales mezcladas
# =============================================================================

class HerramientasRed:
    """Conjunto de utilidades genericas de red."""

    @staticmethod
    def cidr_a_mascara(cidr):
        """Convierte un prefijo CIDR (ej: 24) a mascara (ej: 255.255.255.0)."""
        if not 0 <= cidr <= 32:
            raise ValueError(f"CIDR fuera de rango: {cidr}")
        bits = "1" * cidr + "0" * (32 - cidr)
        octetos = [str(int(bits[i:i+8], 2)) for i in range(0, 32, 8)]
        return ".".join(octetos)

    @staticmethod
    def mac_normalizar(mac):
        """Normaliza una MAC: minusculas, separada por dos puntos."""
        limpia = mac.replace("-", "").replace(":", "").replace(".", "").lower()
        if len(limpia) != 12:
            raise ValueError(f"MAC con longitud invalida: {mac}")
        return ":".join(limpia[i:i+2] for i in range(0, 12, 2))

    @staticmethod
    def es_misma_subred(ip1, ip2, cidr):
        """Verifica si dos IPs estan en la misma subred."""
        # OBSERVACION: simplificacion: compara los primeros N bits.
        if not (HerramientasIP.es_formato_valido(ip1) and
                HerramientasIP.es_formato_valido(ip2)):
            return False
        o1 = ip1.split(".")
        o2 = ip2.split(".")
        octetos_completos = cidr // 8
        return o1[:octetos_completos] == o2[:octetos_completos]

print("\n=== Ejercicio 04: HerramientasRed ===")
print(f"CIDR /24 -> mascara:    {HerramientasRed.cidr_a_mascara(24)}")
print(f"CIDR /16 -> mascara:    {HerramientasRed.cidr_a_mascara(16)}")
print(f"CIDR /30 -> mascara:    {HerramientasRed.cidr_a_mascara(30)}")

print(f"\nMAC normalizada 'AA-BB-CC-11-22-33': {HerramientasRed.mac_normalizar('AA-BB-CC-11-22-33')}")
print(f"MAC normalizada 'aabb.cc11.2233':    {HerramientasRed.mac_normalizar('aabb.cc11.2233')}")

print(f"\n10.0.0.1 y 10.0.0.5 en /24:    {HerramientasRed.es_misma_subred('10.0.0.1', '10.0.0.5', 24)}")
print(f"10.0.0.1 y 10.0.1.5 en /24:    {HerramientasRed.es_misma_subred('10.0.0.1', '10.0.1.5', 24)}")
print(f"10.0.0.1 y 10.0.1.5 en /16:    {HerramientasRed.es_misma_subred('10.0.0.1', '10.0.1.5', 16)}")

# OBSERVACION DIDACTICA: HerramientasRed usa HerramientasIP. Esto es valido?
# OBSERVACION TECNICA: si. Las clases pueden referenciarse entre si. Como
# son @staticmethod, no hay objetos involucrados, solo lookup por nombre.


# =============================================================================
#  ZONA INTERACTIVA  (descomentar en clase)
# =============================================================================
# DESCOMENTAR EN CLASE:
#
# clave = input("Ingresa una clave para evaluar: ")
# puntaje, nivel = HerramientasPassword.evaluar_fortaleza(clave)
# print(f"Tu clave es: {nivel} ({puntaje}/5)")
#
# ip = input("Ingresa una IP para categorizar: ")
# if HerramientasIP.es_formato_valido(ip):
#     if HerramientasIP.es_privada(ip):
#         print(f"{ip} es PRIVADA (RFC 1918)")
#     elif HerramientasIP.es_loopback(ip):
#         print(f"{ip} es LOOPBACK")
#     else:
#         print(f"{ip} es PUBLICA")
#
# OBSERVACION DIDACTICA: cuantos objetos cree para hacer todas estas operaciones?


# =============================================================================
#  FIN DEL ARCHIVO  -  04_staticmethod.py
# =============================================================================
