from encapsulamiento import CuentaSinProteccion, CuentaProtegida, ServidorWeb

# OBSERVACION: cualquiera puede cambiar el saldo sin control.
print("=== Sin encapsulamiento ===")
cuenta1 = CuentaSinProteccion("Hector", 500)
cuenta1.saldo = -10000          # esto es legal y es un PROBLEMA
print(f"Saldo: {cuenta1.saldo}") # -10000 (un saldo negativo absurdo)


cuenta = CuentaProtegida("Hector", 500)

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