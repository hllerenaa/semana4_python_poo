# Solucion de referencia (NO se entrega al estudiante - solo para validacion del docente)
def imprimir_banner():
    print("================================================")
    print("    SISTEMA DE INVENTARIO DE DISPOSITIVOS       ")
    print("================================================")

class Dispositivo:
    def __init__(self, ip, modelo, ubicacion):
        self.modelo = modelo
        self.ubicacion = ubicacion
        self.ip = ip

    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, valor):
        partes = valor.split(".")
        if len(partes) != 4:
            raise ValueError("IP invalida: " + valor)
        for p in partes:
            if not p.isdigit() or not 0 <= int(p) <= 255:
                raise ValueError("IP invalida: " + valor)
        self._ip = valor

    def reportar(self):
        print()
        print(f"Dispositivo: {self.ip}")
        print(f"  Modelo:    {self.modelo}")
        print(f"  Ubicacion: {self.ubicacion}")

    @staticmethod
    def es_ip_privada(ip):
        if ip.startswith("10."):
            return True
        if ip.startswith("192.168."):
            return True
        partes = ip.split(".")
        if partes[0] == "172" and 16 <= int(partes[1]) <= 31:
            return True
        return False

    @classmethod
    def desde_csv(cls, linea):
        ip, modelo, ubicacion = linea.split(",")
        return cls(ip.strip(), modelo.strip(), ubicacion.strip())


if __name__ == "__main__":
    imprimir_banner()

    d1 = Dispositivo("10.0.0.1", "Cisco-2960", "DC-A")
    d2 = Dispositivo.desde_csv("192.168.1.1, MikroTik, Oficina")

    d1.reportar()
    d2.reportar()

    print()
    print(f"10.0.0.5  es privada?  {Dispositivo.es_ip_privada('10.0.0.5')}")
    print(f"8.8.8.8   es privada?  {Dispositivo.es_ip_privada('8.8.8.8')}")

    print()
    try:
        d3 = Dispositivo("999.0.0.1", "X", "Y")
    except ValueError as e:
        print(f"Error capturado: {e}")
