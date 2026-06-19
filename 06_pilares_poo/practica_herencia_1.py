from herencia_dispositivos import Router, Switch

# Usamos las clases hijas
r = Router("10.0.0.1", "AA:BB:01", num_rutas=8)
s = Switch("10.0.0.2", "AA:BB:02", num_vlans=5)

r.encender()
r.reportar()
r.mostrar_rutas()
s.encender()
s.reportar()
s.mostrar_vlans()
