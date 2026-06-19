class Dispositivo:
    """Clase PADRE. Tiene lo comun a todos los dispositivos."""

    def __init__(self, ip, mac):
        self.ip = ip
        self.mac = mac
        self.activo = False

    def encender(self):
        self.activo = True
        print(f"{self.ip} encendido")

    def apagar(self):
        self.activo = False
        print(f"{self.ip} apagado")

    def reportar(self):
        estado = "ACTIVO" if self.activo else "INACTIVO"
        print(f"  {self.ip} / {self.mac} -> {estado}")

# OBSERVACION: Router HEREDA de Dispositivo.
# Recibe ip, mac, encender(), apagar() y reportar() GRATIS.
class Router(Dispositivo):
    """Router HEREDA todo de Dispositivo."""

    def __init__(self, ip, mac, num_rutas):
        # OBSERVACION: super() llama al __init__ del padre.
        super().__init__(ip, mac)
        # Y agregamos LO PROPIO del Router:
        self.num_rutas = num_rutas

    def mostrar_rutas(self):
        """Metodo propio del Router (no esta en Dispositivo)."""
        print(f"  Router {self.ip} tiene {self.num_rutas} rutas")


# OBSERVACION: Switch tambien hereda.
class Switch(Dispositivo):
    """Switch HEREDA de Dispositivo, agrega lo propio."""

    def __init__(self, ip, mac, num_vlans):
        super().__init__(ip, mac)
        self.num_vlans = num_vlans

    def mostrar_vlans(self):
        print(f"  Switch {self.ip} tiene {self.num_vlans} VLANs")