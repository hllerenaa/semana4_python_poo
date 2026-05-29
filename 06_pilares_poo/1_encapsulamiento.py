# =============================================================================
#  PILAR 1 DE 4  -  ENCAPSULAMIENTO
#  Esconder los datos importantes dentro del objeto.
#  Solo se cambian con permiso (a traves de metodos controlados).
#
#  IDEA CLAVE:
#  Imagina una caja fuerte. Los datos importantes estan dentro y nadie los
#  toca directamente. Hay que pasar por un control (validacion) para
#  modificarlos. En Python esto se hace con:
#    - Atributos privados (con __ adelante)
#    - @property + @setter para controlar el acceso
# =============================================================================


# -----------------------------------------------------------------------------
# EJEMPLO 1  -  SIN encapsulamiento  (lo que pasa cuando no proteges)
# -----------------------------------------------------------------------------

class CuentaSinProteccion:
    """Esta clase NO usa encapsulamiento. Cualquiera puede romperla."""

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

# OBSERVACION: cualquiera puede cambiar el saldo sin control.
print("=== Sin encapsulamiento ===")
cuenta = CuentaSinProteccion("Hector", 500)
cuenta.saldo = -10000          # esto es legal y es un PROBLEMA
print(f"Saldo: {cuenta.saldo}") # -10000 (un saldo negativo absurdo)

# OBSERVACION DIDACTICA: en la vida real, un saldo bancario nunca puede ser
# tan negativo. Hay que poner limites.


# -----------------------------------------------------------------------------
# EJEMPLO 2  -  CON encapsulamiento  (la version protegida)
# -----------------------------------------------------------------------------

class CuentaProtegida:
    """Esta clase SI usa encapsulamiento."""

    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        # OBSERVACION: __saldo es PRIVADO (doble guion bajo).
        # Nadie deberia tocarlo desde afuera.
        self.__saldo = saldo_inicial

    @property
    def saldo(self):
        """Getter: cualquiera puede LEER el saldo."""
        return self.__saldo

    @saldo.setter
    def saldo(self, nuevo_valor):
        """Setter: SOLO permite cambiar si el valor es valido."""
        # OBSERVACION: aqui esta el control.
        if nuevo_valor < 0:
            raise ValueError("El saldo no puede ser negativo")
        self.__saldo = nuevo_valor

    def depositar(self, monto):
        """Metodo controlado para SUMAR al saldo."""
        if monto <= 0:
            raise ValueError("Monto invalido")
        self.__saldo += monto

    def retirar(self, monto):
        """Metodo controlado para RESTAR del saldo."""
        if monto > self.__saldo:
            raise ValueError("Saldo insuficiente")
        self.__saldo -= monto


print("\n=== Con encapsulamiento ===")
cuenta = CuentaProtegida("Hector", 500)
cuenta.depositar(200)
print(f"Despues de depositar 200: {cuenta.saldo}")  # 700

cuenta.retirar(300)
print(f"Despues de retirar 300:   {cuenta.saldo}")  # 400

# OBSERVACION: ahora intentos invalidos lanzan errores.
print("\nIntentos invalidos:")
try:
    cuenta.saldo = -50
except ValueError as e:
    print(f"  Bloqueado: {e}")

try:
    cuenta.retirar(10000)
except ValueError as e:
    print(f"  Bloqueado: {e}")

try:
    cuenta.depositar(-100)
except ValueError as e:
    print(f"  Bloqueado: {e}")


# -----------------------------------------------------------------------------
# EJEMPLO 3  -  Encapsulamiento aplicado a seguridad de red
# -----------------------------------------------------------------------------

class ServidorWeb:
    """Servidor con clave de admin protegida."""

    def __init__(self, host, clave_admin):
        self.host = host
        self.__clave = clave_admin       # privada
        self.__intentos_fallidos = 0     # privada

    @property
    def clave_visible(self):
        """Solo muestra los primeros 2 caracteres + asteriscos."""
        # OBSERVACION: ni el getter expone la clave completa.
        if not self.__clave:
            return ""
        return self.__clave[:2] + "*" * (len(self.__clave) - 2)

    def autenticar(self, intento):
        """Unica forma de comparar con la clave guardada."""
        if intento == self.__clave:
            self.__intentos_fallidos = 0
            return True
        self.__intentos_fallidos += 1
        return False

    def esta_bloqueado(self):
        """True si hubo 3 intentos fallidos."""
        return self.__intentos_fallidos >= 3


print("\n=== Encapsulamiento en seguridad ===")
servidor = ServidorWeb("ister.edu.ec", "Pass2026!")
print(f"Clave visible: {servidor.clave_visible}")  # Pa******

print(servidor.autenticar("admin"))     # False
print(servidor.autenticar("Pass2026!")) # True
print(f"Bloqueado?: {servidor.esta_bloqueado()}")  # False

# OBSERVACION DIDACTICA: si alguien quiere imprimir la clave directamente,
# no podra. Solo puede usar los metodos que YO defini.


# =============================================================================
#  PARA PRACTICAR
# =============================================================================
# Crea una clase Termostato que tenga:
#   - temperatura: atributo privado
#   - @property que permita leer la temperatura
#   - @setter que valide que la temperatura este entre -50 y 100 grados
#   - Si esta fuera de rango, lanzar ValueError
# =============================================================================
