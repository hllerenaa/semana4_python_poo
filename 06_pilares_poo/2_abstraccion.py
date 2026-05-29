# =============================================================================
#  PILAR 2 DE 4  -  ABSTRACCION
#  Mostrar solo lo IMPORTANTE; los detalles internos quedan ocultos.
#
#  IDEA CLAVE:
#  Cuando manejas un auto, solo usas el volante, los pedales y la palanca.
#  No te importa COMO funciona el motor. Eso es abstraccion.
#  En programacion, una clase ofrece metodos publicos faciles de usar,
#  y los detalles internos quedan en metodos privados (con _).
# =============================================================================


# -----------------------------------------------------------------------------
# EJEMPLO 1  -  Escaner de puertos: complejo por dentro, simple por fuera
# -----------------------------------------------------------------------------

class EscanerPuertos:
    """Escanea puertos de un host. Detalles ocultos al usuario."""

    def __init__(self, host):
        self.host = host
        # OBSERVACION: lista de puertos comunes (oculto al usuario).
        self._puertos_comunes = [22, 23, 80, 443, 3306, 3389]
        self._timeout = 2

    # OBSERVACION: metodo PRIVADO (empieza con _). Detalle interno.
    def _intentar_conectar(self, puerto):
        """Detalle interno: simula intentar conectar a un puerto."""
        # En produccion aqui iria socket.connect_ex(...)
        # Simulamos: el 22 y el 443 estan abiertos.
        return puerto in (22, 443)

    # OBSERVACION: metodo PRIVADO. Otro detalle interno.
    def _formatear_resultado(self, puerto, abierto):
        """Detalle interno: como mostrar cada resultado."""
        estado = "ABIERTO " if abierto else "cerrado"
        return f"  Puerto {puerto:5} - {estado}"

    # OBSERVACION: este es el UNICO metodo que el usuario necesita conocer.
    def escanear(self):
        """Metodo publico SIMPLE. El usuario solo llama esto."""
        print(f"Escaneando {self.host}...")
        abiertos = []
        for puerto in self._puertos_comunes:
            if self._intentar_conectar(puerto):
                abiertos.append(puerto)
                print(self._formatear_resultado(puerto, True))
            else:
                print(self._formatear_resultado(puerto, False))
        return abiertos


print("=== Escaner de puertos (abstraccion) ===")
escaner = EscanerPuertos("10.0.0.1")
# OBSERVACION: el usuario solo llama escanear(). No necesita saber nada mas.
resultado = escaner.escanear()
print(f"\nPuertos abiertos: {resultado}")

# OBSERVACION DIDACTICA: el usuario NO sabe (ni necesita saber):
#   - como se intenta conectar
#   - cuales son los puertos comunes
#   - como se formatea la salida
# Solo sabe: "llamo escanear() y obtengo los puertos abiertos".


# -----------------------------------------------------------------------------
# EJEMPLO 2  -  Cafetera con abstraccion (analogia simple)
# -----------------------------------------------------------------------------

class Cafetera:
    """Una cafetera: presionas un boton y sale el cafe.
    Lo de adentro queda oculto."""

    def __init__(self):
        self._agua_ml = 1000
        self._cafe_gramos = 200

    # PRIVADOS (lo interno)
    def _calentar_agua(self):
        print("  (interno) Calentando agua...")
        self._agua_ml -= 200

    def _moler_cafe(self):
        print("  (interno) Moliendo cafe...")
        self._cafe_gramos -= 20

    def _filtrar(self):
        print("  (interno) Filtrando...")

    def _servir(self):
        print("  (interno) Sirviendo en la taza")

    # PUBLICO (lo que usa el usuario)
    def preparar_cafe(self):
        """UN boton. Por dentro hace 4 cosas."""
        print("Preparando tu cafe...")
        self._calentar_agua()
        self._moler_cafe()
        self._filtrar()
        self._servir()
        print("Listo! Disfruta")


print("\n=== Cafetera (analogia de abstraccion) ===")
cafetera = Cafetera()
cafetera.preparar_cafe()

# OBSERVACION DIDACTICA: el usuario solo llamo UN metodo (preparar_cafe).
# La cafetera hizo 4 cosas por dentro. Esa es la abstraccion.


# -----------------------------------------------------------------------------
# EJEMPLO 3  -  Notificador con abstraccion (oculta el medio)
# -----------------------------------------------------------------------------

class Notificador:
    """Envia notificaciones. El usuario no sabe POR DONDE se envian."""

    def __init__(self, destinatario):
        self.destinatario = destinatario

    def _enviar_email(self, mensaje):
        print(f"  [Email a {self.destinatario}]: {mensaje}")

    def _enviar_sms(self, mensaje):
        print(f"  [SMS a {self.destinatario}]: {mensaje}")

    def _enviar_push(self, mensaje):
        print(f"  [Push a {self.destinatario}]: {mensaje}")

    def notificar(self, mensaje, urgencia="normal"):
        """Metodo publico: el usuario solo llama esto."""
        # OBSERVACION: por dentro decide el medio segun la urgencia.
        if urgencia == "alta":
            self._enviar_sms(mensaje)
            self._enviar_push(mensaje)
        elif urgencia == "media":
            self._enviar_email(mensaje)
            self._enviar_push(mensaje)
        else:
            self._enviar_email(mensaje)


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
