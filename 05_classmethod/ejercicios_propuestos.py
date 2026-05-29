# =============================================================================
#  EJERCICIOS PROPUESTOS  -  @classmethod
#  Resuelve cada ejercicio por tu cuenta. La solucion no esta aqui.
#
#  RECUERDA:
#  - @classmethod recibe cls como primer parametro (no self)
#  - Se usa principalmente para CONSTRUCTORES ALTERNATIVOS
#  - Dentro del metodo, usa cls(...) para crear instancias
# =============================================================================


# -----------------------------------------------------------------------------
# EJERCICIO 1  -  Libro con constructor desde CSV
# -----------------------------------------------------------------------------
# Crea una clase Libro con:
#
# ATRIBUTOS:
#   - titulo
#   - autor
#   - año
#
# CONSTRUCTORES (3 formas de crear un Libro):
#   - __init__(self, titulo, autor, año): el normal
#   - desde_csv(cls, linea): recibe 'titulo,autor,año' y crea un Libro
#   - desde_dict(cls, datos): recibe un dict con keys 'titulo', 'autor', 'año'
#
# METODO:
#   - __repr__(self): retorna 'Libro: titulo (año) - autor'
#
# PRUEBAS QUE DEBES PASAR:
#   l1 = Libro('Python Avanzado', 'Guido', 2020)
#   l2 = Libro.desde_csv('1984, Orwell, 1949')
#   l3 = Libro.desde_dict({'titulo': 'Dune', 'autor': 'Herbert', 'año': 1965})
#   print(l1)   # Libro: Python Avanzado (2020) - Guido
#   print(l2)   # Libro: 1984 (1949) - Orwell
#   print(l3)   # Libro: Dune (1965) - Herbert

# TU CODIGO AQUI


# -----------------------------------------------------------------------------
# EJERCICIO 2  -  Contador de empleados
# -----------------------------------------------------------------------------
# Crea una clase Empleado que cuente cuantos se han creado.
#
# ATRIBUTOS DE CLASE (no de instancia):
#   - _contador: empieza en 0 (lleva la cuenta TOTAL de empleados)
#
# ATRIBUTOS DE INSTANCIA (__init__):
#   - nombre
#   - id: se asigna automaticamente usando el contador
#
# METODOS:
#   - __init__(self, nombre): asigna nombre, incrementa contador, asigna id
#
# @classmethod:
#   - cuantos_hay(cls): retorna el contador actual
#   - resetear(cls): pone el contador en 0 (util para tests)
#
# PRUEBAS QUE DEBES PASAR:
#   e1 = Empleado('Hector')
#   e2 = Empleado('Maria')
#   e3 = Empleado('Carlos')
#   print(e1.id)                  # 1
#   print(e2.id)                  # 2
#   print(e3.id)                  # 3
#   print(Empleado.cuantos_hay()) # 3
#   Empleado.resetear()
#   print(Empleado.cuantos_hay()) # 0

# TU CODIGO AQUI


# -----------------------------------------------------------------------------
# EJERCICIO 3  -  Fecha desde texto
# -----------------------------------------------------------------------------
# Crea una clase Fecha con:
#
# ATRIBUTOS:
#   - dia, mes, año
#
# CONSTRUCTORES:
#   - __init__(self, dia, mes, año): el normal
#   - desde_texto(cls, texto): parsea 'dd/mm/aaaa' y crea Fecha
#   - hoy(cls): retorna la fecha actual usando datetime
#
# METODO:
#   - __repr__(self): 'dd/mm/aaaa'
#
# PRUEBAS:
#   f1 = Fecha(15, 5, 2026)
#   f2 = Fecha.desde_texto('20/12/2024')
#   f3 = Fecha.hoy()
#   print(f1)   # 15/5/2026
#   print(f2)   # 20/12/2024
#   print(f3)   # fecha de hoy
#
# PISTA para hoy():
#   from datetime import date
#   d = date.today()
#   return cls(d.day, d.month, d.year)

# TU CODIGO AQUI


# -----------------------------------------------------------------------------
# EJERCICIO 4  -  Pizza con constructores predefinidos
# -----------------------------------------------------------------------------
# Crea una clase Pizza con:
#
# ATRIBUTOS:
#   - tamaño: 'pequeña', 'mediana', 'grande'
#   - ingredientes: lista de ingredientes
#
# CONSTRUCTORES PREDEFINIDOS (con @classmethod):
#   - margarita(cls, tamaño='mediana'): ingredientes = ['queso', 'tomate', 'albahaca']
#   - hawaiana(cls, tamaño='mediana'): ['queso', 'jamon', 'piña']
#   - cuatro_quesos(cls, tamaño='mediana'): ['mozzarella', 'parmesano', 'gorgonzola', 'cheddar']
#
# METODO:
#   - __repr__(self): 'Pizza tamaño con: ing1, ing2, ing3'
#
# PRUEBAS:
#   p1 = Pizza.margarita()
#   p2 = Pizza.hawaiana('grande')
#   p3 = Pizza.cuatro_quesos('pequeña')
#   print(p1)   # Pizza mediana con: queso, tomate, albahaca
#   print(p2)   # Pizza grande con: queso, jamon, piña

# TU CODIGO AQUI


# =============================================================================
#  RETO FINAL (extra)
#  Crea una clase Color con @classmethod para colores predefinidos:
#  Color.rojo(), Color.verde(), Color.azul(), Color.desde_hex('#FF5733')
#  Cada uno retorna un Color con sus valores RGB asignados.
# =============================================================================
