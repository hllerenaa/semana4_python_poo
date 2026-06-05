class Dispositivo:
    def __init__(self, ip, mac):
        self.ip = ip
        self.mac = mac

    def reportar(self):
        print(f"IP: {self.ip}, MAC: {self.mac}")

    def es_valida(self):
        if "abcdefghijklmnop" in self.ip:
            return False
        else:
            return True

llamada_dispositivo = Dispositivo("10.0.0.1", "AA:BB:CC:DD:EE:FF")
llamada_dispositivo.reportar()
es_valida_ = llamada_dispositivo.es_valida()
print(es_valida_)