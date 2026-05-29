# =============================================================================
#  TAREA PEA1  -  Sistema de inventario de dispositivos de red
#
#  Estudiante:  ___________________________
#  Fecha:       __ / __ / 2026
#  Asignatura:  Lenguaje de Programacion Python
#  Proposito:   Aplicar los 5 tipos de funciones vistos en clase
#
#  COMO USAR ESTE ARCHIVO:
#  Este es un ESQUELETO. Donde dice TODO, debes completar el codigo.
#  Lee primero el archivo enunciado.md para ver los requisitos completos.
#
#  RENOMBRA este archivo a: apellido_nombre_PEA1.py antes de entregar.
# =============================================================================


# ---------------------------------------------------------------
# TIPO 1: FUNCION SUELTA  (fuera de cualquier clase)
# ---------------------------------------------------------------
def imprimir_banner():
    # TODO: imprimir 3 lineas decorativas con el titulo del sistema
    # Ejemplo:
    #   =================================================
    #       SISTEMA DE INVENTARIO DE DISPOSITIVOS
    #   =================================================
    pass


# ---------------------------------------------------------------
# CLASE PRINCIPAL
# ---------------------------------------------------------------
class Dispositivo:

    def __init__(self, ip, modelo, ubicacion):
        # TODO: asignar self.modelo = modelo
        # TODO: asignar self.ubicacion = ubicacion
        # TODO: usar self.ip = ip  (llama al setter automaticamente)
        pass

    # TIPO 3: @property (con validacion)
    @property
    def ip(self):
        # TODO: devolver self._ip
        pass

    @ip.setter
    def ip(self, valor):
        # TODO: validar que valor tiene 4 octetos 0-255
        # PISTA: usa valor.split('.') y verifica len(partes) == 4
        # PISTA: para cada parte, verifica isdigit() y rango 0-255
        # TODO: si es invalida, lanzar ValueError('IP invalida: ' + valor)
        # TODO: si es valida, asignar self._ip = valor
        pass

    # TIPO 2: METODO NORMAL  (con self)
    def reportar(self):
        # TODO: imprimir self.ip, self.modelo, self.ubicacion en formato bonito
        # Ejemplo de salida:
        #   Dispositivo: 10.0.0.1
        #     Modelo:    Cisco-2960
        #     Ubicacion: DC-A
        pass

    # TIPO 4: @staticmethod  (sin self, sin cls)
    @staticmethod
    def es_ip_privada(ip):
        # TODO: True si ip empieza con '10.'
        # TODO: True si ip empieza con '192.168.'
        # TODO: True si ip empieza con '172.' y segundo octeto 16-31
        # TODO: False en cualquier otro caso
        pass

    # TIPO 5: @classmethod  (constructor alternativo)
    @classmethod
    def desde_csv(cls, linea):
        # TODO: dividir linea por coma con linea.split(',')
        # TODO: limpiar cada parte con .strip()
        # TODO: devolver cls(ip, modelo, ubicacion)
        pass


# ---------------------------------------------------------------
# PROGRAMA PRINCIPAL  (pruebas)
# ---------------------------------------------------------------
if __name__ == "__main__":
    imprimir_banner()

    # TODO: crear dispositivo manualmente
    # d1 = Dispositivo('10.0.0.1', 'Cisco-2960', 'DC-A')

    # TODO: crear dispositivo desde CSV
    # d2 = Dispositivo.desde_csv('192.168.1.1, MikroTik, Oficina')

    # TODO: reportar ambos
    # d1.reportar()
    # d2.reportar()

    # TODO: probar Dispositivo.es_ip_privada()
    # print('10.0.0.5 es privada?', Dispositivo.es_ip_privada('10.0.0.5'))
    # print('8.8.8.8 es privada?', Dispositivo.es_ip_privada('8.8.8.8'))

    # TODO: probar IP invalida con try/except
    # try:
    #     d3 = Dispositivo('999.0.0.1', 'X', 'Y')
    # except ValueError as e:
    #     print('Error capturado:', e)
