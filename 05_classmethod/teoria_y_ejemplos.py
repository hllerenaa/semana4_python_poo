# =============================================================================
#  SEMANA 4  |  TIPO 5 DE 5  -  @classmethod
#  Metodos que reciben la CLASE (cls) en lugar del objeto (self).
#  Su uso principal: constructores alternativos.
#
#  Asignatura:  Lenguaje de Programacion Python
#  Carrera:     Infraestructura de Redes y Ciberseguridad
#  Docente:     Ing. Hector Llerena, MSc
#  Periodo:     2026-1
#
#  QUE ES:     Metodo decorado con @classmethod cuyo primer parametro es cls
#              (la clase misma). Permite crear objetos desde otras fuentes.
#  CUANDO:     Cuando necesitas MAS DE UNA forma de construir el objeto.
#              __init__ ofrece una sola; @classmethod ofrece alternativas.
#  COMO LLAMAR: Clase.metodo(argumentos)
#
#  Convencion de comentarios:
#    OBSERVACION            -> que hace el codigo
#    OBSERVACION DIDACTICA  -> pregunta para el estudiante
#    OBSERVACION TECNICA    -> detalle sutil de Python
# =============================================================================

import json


# =============================================================================
#  EJERCICIO 01  -  Equipo: constructor alternativo desde CSV
# =============================================================================

class Equipo:
    """Equipo de red creable desde varias fuentes de datos."""

    def __init__(self, ip, modelo, ubicacion):
        # OBSERVACION: constructor estandar. Recibe los datos por separado.
        self.ip = ip
        self.modelo = modelo
        self.ubicacion = ubicacion

    @classmethod
    def desde_csv(cls, linea):
        """Crea un Equipo desde una linea CSV: 'ip,modelo,ubicacion'."""
        # OBSERVACION: cls es la clase. cls(...) equivale a Equipo(...).
        partes = linea.split(",")
        if len(partes) != 3:
            raise ValueError(f"CSV invalido: {linea}")
        ip, modelo, ubicacion = (p.strip() for p in partes)
        return cls(ip, modelo, ubicacion)

    def __repr__(self):
        return f"Equipo({self.ip}, {self.modelo}, {self.ubicacion})"

print("=== Ejercicio 01: desde_csv ===")
# OBSERVACION: dos formas de crear el mismo tipo de objeto.
e1 = Equipo("10.0.0.1", "Cisco-2960", "DC-A")
e2 = Equipo.desde_csv(" 10.0.0.2 , HP-Aruba , DC-B ")
print(e1)
print(e2)

# OBSERVACION DIDACTICA: por que usar Equipo.desde_csv en lugar de hacer el
# split antes y llamar Equipo() con los pedazos?
# OBSERVACION TECNICA: encapsula la logica del parsing en la clase. Si
# mañana el formato CSV cambia, modificas en UN solo lugar. El codigo que
# usa la clase no se entera.


# =============================================================================
#  EJERCICIO 02  -  Equipo: multiples constructores alternativos
# =============================================================================

class EquipoCompleto:
    """Equipo con CUATRO formas de crearse."""

    def __init__(self, ip, modelo, ubicacion):
        self.ip = ip
        self.modelo = modelo
        self.ubicacion = ubicacion

    @classmethod
    def desde_csv(cls, linea):
        """Crea desde linea CSV."""
        ip, modelo, ubicacion = (p.strip() for p in linea.split(","))
        return cls(ip, modelo, ubicacion)

    @classmethod
    def desde_dict(cls, datos):
        """Crea desde un diccionario."""
        return cls(datos["ip"], datos["modelo"], datos["ubicacion"])

    @classmethod
    def desde_json(cls, json_str):
        """Crea desde un string JSON."""
        # OBSERVACION: reutiliza desde_dict pasando el dict parseado.
        return cls.desde_dict(json.loads(json_str))

    @classmethod
    def por_defecto(cls):
        """Crea un equipo con valores estandar (util para tests)."""
        return cls("0.0.0.0", "Generic", "Sin asignar")

    def __repr__(self):
        return f"Equipo({self.ip}, {self.modelo}, @ {self.ubicacion})"

print("\n=== Ejercicio 02: multiples constructores ===")

# OBSERVACION: cuatro formas de crear el MISMO tipo de objeto.
e1 = EquipoCompleto("10.0.0.1", "Cisco", "DC-A")
e2 = EquipoCompleto.desde_csv("10.0.0.2, HP, DC-B")
e3 = EquipoCompleto.desde_dict({"ip": "10.0.0.3", "modelo": "MikroTik", "ubicacion": "DC-C"})
e4 = EquipoCompleto.desde_json('{"ip": "10.0.0.4", "modelo": "TP-Link", "ubicacion": "DC-D"}')
e5 = EquipoCompleto.por_defecto()

for equipo in [e1, e2, e3, e4, e5]:
    print(f"  {equipo}")

# OBSERVACION DIDACTICA: cuantos __init__ tiene la clase? Por que podemos
# tener 5 formas de crear el objeto con UN solo __init__?
# OBSERVACION TECNICA: __init__ es uno solo. Los @classmethod son PARSERS
# que terminan llamando a __init__ con los datos ya procesados.


# =============================================================================
#  EJERCICIO 03  -  Contador de instancias con @classmethod
# =============================================================================

class Dispositivo:
    """Lleva la cuenta de cuantas instancias se han creado."""

    # Atributo de clase: compartido entre TODOS los objetos.
    _total_creados = 0

    def __init__(self, ip):
        self.ip = ip
        self.id = Dispositivo._siguiente_id()

    @classmethod
    def _siguiente_id(cls):
        """Incrementa y retorna el siguiente ID. Util para asignar IDs unicos."""
        cls._total_creados += 1
        return cls._total_creados

    @classmethod
    def cantidad_creada(cls):
        """Retorna cuantos dispositivos se han creado."""
        return cls._total_creados

    @classmethod
    def resetear_contador(cls):
        """Reinicia el contador (util en tests)."""
        cls._total_creados = 0

    def __repr__(self):
        return f"Dispositivo #{self.id}: {self.ip}"

print("\n=== Ejercicio 03: contador con @classmethod ===")
print(f"Inicial: {Dispositivo.cantidad_creada()}")

d1 = Dispositivo("10.0.0.1")
d2 = Dispositivo("10.0.0.2")
d3 = Dispositivo("10.0.0.3")

print(d1)
print(d2)
print(d3)
print(f"Total creados: {Dispositivo.cantidad_creada()}")

Dispositivo.resetear_contador()
print(f"Tras reset:    {Dispositivo.cantidad_creada()}")

d4 = Dispositivo("10.0.0.99")
print(d4)
print(f"Total creados: {Dispositivo.cantidad_creada()}")

# OBSERVACION DIDACTICA: que diferencia hay entre el atributo self.id y
# el atributo cls._total_creados?
# OBSERVACION TECNICA: self.id pertenece a CADA objeto (cada uno tiene el
# suyo). cls._total_creados pertenece a la CLASE: hay UNO solo compartido.


# =============================================================================
#  EJERCICIO 04  -  @classmethod + herencia: factory polimorfico
# =============================================================================

class DispositivoBase:
    """Clase base con factory metodo polimorfico."""

    def __init__(self, ip):
        self.ip = ip

    @classmethod
    def desde_string(cls, texto):
        """Crea un objeto desde un string. SE ADAPTA a la subclase."""
        # OBSERVACION: cls(texto.strip()) crea una instancia de la clase
        # CORRECTA. Si lo llaman desde Router, hace Router(...). Si lo
        # llaman desde Switch, hace Switch(...).
        return cls(texto.strip())

    def reportar(self):
        print(f"Dispositivo {self.ip}")


class Router(DispositivoBase):
    """Hereda de DispositivoBase. desde_string viene gratis."""
    def reportar(self):
        print(f"Router {self.ip}  (con tabla de rutas)")


class Switch(DispositivoBase):
    """Hereda de DispositivoBase. desde_string viene gratis."""
    def reportar(self):
        print(f"Switch {self.ip}  (con VLANs configuradas)")


print("\n=== Ejercicio 04: @classmethod polimorfico ===")
# OBSERVACION: la MISMA llamada desde_string produce objetos de tipos distintos.
d = DispositivoBase.desde_string("  10.0.0.1  ")    # crea DispositivoBase
r = Router.desde_string("  10.0.0.2  ")              # crea Router (no DispositivoBase!)
s = Switch.desde_string("  10.0.0.3  ")              # crea Switch (no DispositivoBase!)

d.reportar()
r.reportar()
s.reportar()

print(f"\nTipo de d: {type(d).__name__}")
print(f"Tipo de r: {type(r).__name__}")
print(f"Tipo de s: {type(s).__name__}")

# OBSERVACION DIDACTICA: si en desde_string hubiera puesto 'return DispositivoBase(...)'
# en lugar de 'return cls(...)', que pasaria al llamar Router.desde_string()?
# OBSERVACION TECNICA: crearia un DispositivoBase, NO un Router. Por eso
# @classmethod recibe cls: para crear instancias de la clase CORRECTA segun
# desde donde se llamo. Esa es la magia que hace el factory polimorfico.


# =============================================================================
#  ZONA INTERACTIVA  (descomentar en clase)
# =============================================================================
# DESCOMENTAR EN CLASE:
#
# print("\nFormas de crear un Equipo:")
# print("1. Manual    (ip, modelo, ubicacion)")
# print("2. Desde CSV (ip,modelo,ubicacion)")
# print("3. Por defecto")
# opcion = input("Elige (1/2/3): ")
#
# if opcion == "1":
#     ip = input("IP: ")
#     modelo = input("Modelo: ")
#     ubicacion = input("Ubicacion: ")
#     e = EquipoCompleto(ip, modelo, ubicacion)
# elif opcion == "2":
#     linea = input("Linea CSV: ")
#     e = EquipoCompleto.desde_csv(linea)
# else:
#     e = EquipoCompleto.por_defecto()
#
# print(f"Equipo creado: {e}")
#
# OBSERVACION DIDACTICA: en los 3 casos el resultado es UN objeto Equipo.
# Cual de los 3 caminos prefieres? Por que?


# =============================================================================
#  FIN DEL ARCHIVO  -  05_classmethod.py
# =============================================================================
