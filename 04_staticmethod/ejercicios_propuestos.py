# =============================================================================
#  EJERCICIOS PROPUESTOS  -  @staticmethod
#  Resuelve cada ejercicio por tu cuenta. La solucion no esta aqui.
#
#  RECUERDA:
#  - @staticmethod NO recibe self ni cls
#  - Se llama: Clase.metodo(...) sin crear objeto
#  - Es como una funcion suelta, pero agrupada dentro de una clase
# =============================================================================


# -----------------------------------------------------------------------------
# EJERCICIO 1  -  Calculadora con metodos estaticos
# -----------------------------------------------------------------------------
# Crea una clase Calculadora con 4 @staticmethod:
#   - sumar(a, b)
#   - restar(a, b)
#   - multiplicar(a, b)
#   - dividir(a, b): si b es 0, retorna None
#
# Importante: la clase NO necesita __init__ porque nunca creas un objeto.
# Llamas todo como Calculadora.sumar(2, 3).
#
# PRUEBAS QUE DEBES PASAR:
#   print(Calculadora.sumar(2, 3))         # 5
#   print(Calculadora.multiplicar(4, 5))   # 20
#   print(Calculadora.dividir(10, 2))      # 5.0
#   print(Calculadora.dividir(10, 0))      # None

# TU CODIGO AQUI


# -----------------------------------------------------------------------------
# EJERCICIO 2  -  Validadores de seguridad
# -----------------------------------------------------------------------------
# Crea una clase Validador con 3 @staticmethod:
#
#   - es_email_valido(email): True si tiene exactamente UN '@' y al menos un '.'
#                             despues del @. Ejemplo: 'a@b.com' True, 'sin-arroba' False.
#
#   - es_telefono_ecuador(numero): True si empieza con '09' y tiene
#                                   exactamente 10 digitos. Ej: '0987654321' True.
#
#   - es_cedula_valida(cedula): True si tiene exactamente 10 digitos numericos.
#
# PRUEBAS QUE DEBES PASAR:
#   print(Validador.es_email_valido('test@gmail.com'))      # True
#   print(Validador.es_email_valido('sin-arroba'))          # False
#   print(Validador.es_telefono_ecuador('0987654321'))      # True
#   print(Validador.es_telefono_ecuador('123'))             # False
#   print(Validador.es_cedula_valida('1712345678'))         # True
#   print(Validador.es_cedula_valida('abc1234567'))         # False

# TU CODIGO AQUI


# -----------------------------------------------------------------------------
# EJERCICIO 3  -  Conversor de unidades de red
# -----------------------------------------------------------------------------
# Crea una clase ConversorRed con @staticmethod:
#
#   - bytes_a_kb(bytes): divide entre 1024
#   - bytes_a_mb(bytes): divide entre 1024 * 1024
#   - bytes_a_gb(bytes): divide entre 1024^3
#   - mb_a_bytes(mb): multiplica por 1024 * 1024
#
# PRUEBAS QUE DEBES PASAR:
#   print(ConversorRed.bytes_a_kb(1024))           # 1.0
#   print(ConversorRed.bytes_a_mb(1048576))        # 1.0
#   print(ConversorRed.bytes_a_gb(1073741824))     # 1.0
#   print(ConversorRed.mb_a_bytes(5))              # 5242880

# TU CODIGO AQUI


# -----------------------------------------------------------------------------
# EJERCICIO 4  -  Generador de identificadores
# -----------------------------------------------------------------------------
# Crea una clase GeneradorID con 3 @staticmethod:
#
#   - id_dispositivo(prefijo, numero): retorna 'PREFIJO-00numero'
#                                       Ejemplo: ('RTR', 5) -> 'RTR-005'
#                                       Usa zfill(3) para rellenar con ceros.
#
#   - id_usuario(nombre, apellido): retorna iniciales en minusculas + numero
#                                    aleatorio entre 100-999.
#                                    Ejemplo: ('Hector', 'Llerena') -> 'hl742'
#                                    PISTA: import random; random.randint(100, 999)
#
#   - id_sesion(): retorna 8 caracteres alfanumericos aleatorios.
#                  PISTA: string.ascii_letters + string.digits
#
# PRUEBAS QUE DEBES PASAR:
#   print(GeneradorID.id_dispositivo('SW', 7))      # SW-007
#   print(GeneradorID.id_dispositivo('FW', 142))    # FW-142
#   print(GeneradorID.id_usuario('Maria', 'Lopez')) # ml<algun-numero>
#   print(GeneradorID.id_sesion())                  # 8 caracteres random

# TU CODIGO AQUI


# =============================================================================
#  RETO FINAL (extra)
#  Crea una clase Hash con @staticmethod md5_de(texto) que retorne el hash MD5
#  de un texto en formato hexadecimal.
#  PISTA: import hashlib; hashlib.md5(texto.encode()).hexdigest()
# =============================================================================
