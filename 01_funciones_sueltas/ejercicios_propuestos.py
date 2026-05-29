# =============================================================================
#  EJERCICIOS PROPUESTOS  -  FUNCIONES SUELTAS
#  Resuelve cada ejercicio por tu cuenta. La solucion no esta aqui.
#
#  Asignatura:  Lenguaje de Programacion Python
#  Carrera:     Infraestructura de Redes y Ciberseguridad
#  Periodo:     2026-1
#
#  COMO TRABAJAR ESTE ARCHIVO:
#  1. Lee primero teoria_y_ejemplos.py de esta misma carpeta.
#  2. Resuelve UN ejercicio a la vez. No saltes.
#  3. Ejecuta tu codigo y verifica que la salida coincida con lo esperado.
#  4. Si te atascas, vuelve al archivo de teoria y busca un ejemplo parecido.
# =============================================================================


# -----------------------------------------------------------------------------
# EJERCICIO 1  -  validar_mac
# -----------------------------------------------------------------------------
# Define una funcion validar_mac(mac) que retorne True si la direccion MAC
# tiene formato correcto.
#
# Una MAC valida tiene 6 grupos de 2 caracteres hexadecimales separados por
# dos puntos. Ejemplo: 'AA:BB:CC:11:22:33'
#
# REGLAS:
#   - 6 partes separadas por ':'
#   - Cada parte tiene exactamente 2 caracteres
#   - Cada caracter es un digito (0-9) o letra A-F (mayuscula)
#
# PRUEBAS QUE DEBES PASAR:
#   validar_mac('AA:BB:CC:11:22:33')  ->  True
#   validar_mac('AA:BB:CC:11:22')     ->  False  (solo 5 partes)
#   validar_mac('AA:BB:CC:11:22:ZZ')  ->  False  (Z no es hexadecimal)
#   validar_mac('AA-BB-CC-11-22-33')  ->  False  (separa con - no con :)

# TU CODIGO AQUI


# Pruebas (descomentar cuando termines):
# print(validar_mac('AA:BB:CC:11:22:33'))
# print(validar_mac('AA:BB:CC:11:22'))
# print(validar_mac('AA:BB:CC:11:22:ZZ'))


# -----------------------------------------------------------------------------
# EJERCICIO 2  -  contar_dispositivos_activos
# -----------------------------------------------------------------------------
# Define una funcion contar_dispositivos_activos(lista) que reciba una lista
# de tuplas (nombre, estado) y retorne CUANTOS dispositivos tienen estado
# 'activo'.
#
# PRUEBAS QUE DEBES PASAR:
#   red = [
#       ('router-1', 'activo'),
#       ('switch-1', 'inactivo'),
#       ('firewall', 'activo'),
#       ('ap-3',     'activo'),
#   ]
#   contar_dispositivos_activos(red)  ->  3

# TU CODIGO AQUI


# -----------------------------------------------------------------------------
# EJERCICIO 3  -  generar_password_aleatoria
# -----------------------------------------------------------------------------
# Define una funcion generar_password_aleatoria(longitud=12) que retorne
# una contraseña aleatoria de la longitud indicada. Debe contener:
#   - Mayusculas
#   - Minusculas
#   - Numeros
#
# PISTA: usa el modulo random y la funcion random.choice().
#   import random
#   alfabeto = 'ABC...abc...123'
#   resultado = ''.join(random.choice(alfabeto) for _ in range(longitud))
#
# PRUEBAS QUE DEBES PASAR:
#   generar_password_aleatoria()      -> 12 caracteres
#   generar_password_aleatoria(20)    -> 20 caracteres
#   generar_password_aleatoria(8)     -> 8 caracteres

# TU CODIGO AQUI
# import random


# -----------------------------------------------------------------------------
# EJERCICIO 4  -  filtrar_logs_por_nivel
# -----------------------------------------------------------------------------
# Define una funcion filtrar_logs_por_nivel(logs, nivel) que reciba:
#   - logs: una lista de tuplas (nivel, mensaje)
#   - nivel: el nivel a filtrar (ej: 'ERROR')
# Y retorne una NUEVA lista solo con los logs de ese nivel.
#
# PRUEBAS QUE DEBES PASAR:
#   logs = [
#       ('INFO',  'Sistema iniciado'),
#       ('ERROR', 'Fallo BD'),
#       ('WARN',  'Memoria alta'),
#       ('ERROR', 'Login fallido'),
#   ]
#   filtrar_logs_por_nivel(logs, 'ERROR')  ->  [('ERROR', 'Fallo BD'), ('ERROR', 'Login fallido')]
#   filtrar_logs_por_nivel(logs, 'INFO')   ->  [('INFO',  'Sistema iniciado')]

# TU CODIGO AQUI


# =============================================================================
#  RETO FINAL (extra)
#  Combina las funciones anteriores: lee un archivo CSV con dispositivos,
#  filtra los activos, genera un reporte con conteo. Si lo logras, comparte
#  tu solucion con el docente.
# =============================================================================
