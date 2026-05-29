# =============================================================================
#  EJERCICIOS PROPUESTOS  -  @property
#  Resuelve cada ejercicio por tu cuenta. La solucion no esta aqui.
#
#  COMO TRABAJAR ESTE ARCHIVO:
#  1. Lee primero teoria_y_ejemplos.py de esta misma carpeta.
#  2. Recuerda: hay DOS tipos de @property:
#     - Con validacion (getter + setter)
#     - Calculado (solo getter)
# =============================================================================


# -----------------------------------------------------------------------------
# EJERCICIO 1  -  @property con VALIDACION (Producto y precio)
# -----------------------------------------------------------------------------
# Crea una clase Producto con:
#   - nombre: texto libre
#   - precio: NO puede ser negativo
#
# REQUISITOS:
# Usa @property + @precio.setter para validar que el precio sea >= 0.
# Si alguien intenta poner un precio negativo, lanza ValueError.
#
# PRUEBAS QUE DEBES PASAR:
#   p = Producto('Switch', 250)
#   print(p.precio)                # 250
#   p.precio = 300
#   print(p.precio)                # 300
#   p.precio = -50                 # debe lanzar ValueError

# TU CODIGO AQUI


# -----------------------------------------------------------------------------
# EJERCICIO 2  -  @property con VALIDACION (Persona y edad)
# -----------------------------------------------------------------------------
# Crea una clase Persona con:
#   - nombre: texto libre
#   - edad: numero entre 0 y 150
#
# Si la edad esta fuera de rango, lanza ValueError.
#
# PRUEBAS QUE DEBES PASAR:
#   p = Persona('Hector', 35)
#   print(p.edad)        # 35
#   p.edad = 40
#   print(p.edad)        # 40
#   p.edad = -5          # ValueError
#   p.edad = 200         # ValueError

# TU CODIGO AQUI


# -----------------------------------------------------------------------------
# EJERCICIO 3  -  @property CALCULADO (Rectangulo)
# -----------------------------------------------------------------------------
# Crea una clase Rectangulo con:
#   - ancho: numero
#   - alto: numero
#
# Y dos PROPERTIES CALCULADOS (sin setter, solo se calculan):
#   - area: ancho * alto
#   - perimetro: 2 * (ancho + alto)
#   - es_cuadrado: True si ancho == alto
#
# PRUEBAS QUE DEBES PASAR:
#   r = Rectangulo(4, 5)
#   print(r.area)              # 20
#   print(r.perimetro)         # 18
#   print(r.es_cuadrado)       # False
#   r.alto = 4
#   print(r.area)              # 16 (se actualiza solo!)
#   print(r.es_cuadrado)       # True

# TU CODIGO AQUI


# -----------------------------------------------------------------------------
# EJERCICIO 4  -  @property CALCULADO (Estadisticas de notas)
# -----------------------------------------------------------------------------
# Crea una clase Estudiante con:
#   - nombre: texto
#   - notas: lista de numeros (empieza vacia)
#
# METODO:
#   - agregar_nota(self, nota): agrega una nota a la lista
#
# PROPERTIES CALCULADOS:
#   - promedio: suma de notas / cantidad. 0 si no hay notas.
#   - aprobado: True si promedio >= 7
#   - nota_mas_alta: maximo de la lista. 0 si no hay notas.
#   - nota_mas_baja: minimo de la lista. 0 si no hay notas.
#
# PRUEBAS QUE DEBES PASAR:
#   e = Estudiante('Maria')
#   e.agregar_nota(8)
#   e.agregar_nota(6)
#   e.agregar_nota(9)
#   print(e.promedio)          # 7.666...
#   print(e.aprobado)          # True
#   print(e.nota_mas_alta)     # 9
#   print(e.nota_mas_baja)     # 6
#
#   e.agregar_nota(2)          # baja el promedio
#   print(e.promedio)          # 6.25
#   print(e.aprobado)          # False (se actualiza solo!)

# TU CODIGO AQUI


# =============================================================================
#  RETO FINAL (extra)
#  Crea una clase Termometro con un atributo grados_celsius y propiedades
#  CALCULADAS para:
#     - grados_fahrenheit (formula: celsius * 9/5 + 32)
#     - grados_kelvin (formula: celsius + 273.15)
#     - estado: 'congelado' si <= 0, 'normal' si 1-30, 'caliente' si > 30
# =============================================================================
