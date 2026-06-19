from abstraccion import EscanerPuertos, Cafetera, Notificador

print("=== Escaner de puertos (abstraccion) ===")
escaner = EscanerPuertos("10.0.0.1")
# OBSERVACION: el usuario solo llama escanear(). No necesita saber nada mas.
resultado = escaner.escanear()
print(f"\nPuertos abiertos: {resultado}")


print("\n=== Cafetera (analogia de abstraccion) ===")
cafetera = Cafetera()
cafetera.preparar_cafe()

# OBSERVACION DIDACTICA: el usuario solo llamo UN metodo (preparar_cafe).
# La cafetera hizo 4 cosas por dentro. Esa es la abstraccion.


# -----------------------------------------------------------------------------
# EJEMPLO 3  -  Notificador con abstraccion (oculta el medio)
# -----------------------------------------------------------------------------

print("\n=== Notificador (multiples canales ocultos) ===")
n = Notificador("hector@ister.edu.ec")
n.notificar("Tarea entregada", urgencia="normal")     # solo email
n.notificar("Backup completado", urgencia="media")     # email + push
n.notificar("Brecha detectada!", urgencia="alta")      # sms + push

# OBSERVACION DIDACTICA: si mañana cambias TODA la logica interna
# (por ejemplo agregar WhatsApp), el codigo que llama notify() sigue igual.


# =============================================================================
#  PARA PRACTICAR
# =============================================================================
# Crea una clase ReproductorMP3 con:
#   - Metodos privados: _cargar_archivo(), _decodificar(), _enviar_a_altavoz()
#   - Metodo publico: reproducir(cancion) que llama a los 3 privados en orden
# La idea es que el usuario solo llame reproducir('cancion.mp3') y todo lo
# demas pase por dentro.
# =============================================================================
