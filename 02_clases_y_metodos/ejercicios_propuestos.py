# =============================================================================
#  EJERCICIOS PROPUESTOS  -  CLASES Y METODOS NORMALES (con self)
#  Resuelve cada ejercicio por tu cuenta. La solucion no esta aqui.
#
#  COMO TRABAJAR ESTE ARCHIVO:
#  1. Lee primero teoria_y_ejemplos.py de esta misma carpeta.
#  2. Resuelve UN ejercicio a la vez.
#  3. Ejecuta y verifica con las pruebas.
# =============================================================================


# -----------------------------------------------------------------------------
# EJERCICIO 1  -  Clase ImpresoraRed
# -----------------------------------------------------------------------------
# Crea una clase ImpresoraRed con los siguientes atributos y metodos:
#
# ATRIBUTOS (en __init__):
#   - ip: direccion IP de la impresora
#   - modelo: modelo (ej: 'HP-LaserJet')
#   - paginas_impresas: contador (empieza en 0)
#   - tinta: nivel de tinta de 0 a 100 (empieza en 100)
#
# METODOS:
#   - imprimir(self, cantidad): suma 'cantidad' a paginas_impresas
#                                y resta 5 a tinta por cada hoja
#   - reportar(self): imprime estado con ip, modelo, paginas y tinta
#   - necesita_recarga(self): True si tinta < 20, False en caso contrario
#
# PRUEBAS QUE DEBES PASAR:
#   imp = ImpresoraRed('10.0.0.50', 'HP-LaserJet')
#   imp.imprimir(3)
#   imp.reportar()                    # paginas=3, tinta=85
#   imp.imprimir(15)
#   print(imp.necesita_recarga())     # True (tinta=10)

# TU CODIGO AQUI


# -----------------------------------------------------------------------------
# EJERCICIO 2  -  Clase CuentaBancaria
# -----------------------------------------------------------------------------
# Crea una clase CuentaBancaria con:
#
# ATRIBUTOS:
#   - titular: nombre
#   - saldo: dinero disponible (empieza en 0)
#   - historial: lista de movimientos (empieza vacia)
#
# METODOS:
#   - depositar(self, monto): suma monto al saldo y agrega un movimiento
#                              al historial: ('deposito', monto)
#   - retirar(self, monto): si hay saldo suficiente, resta y agrega
#                            ('retiro', monto). Si no, imprime "Saldo insuficiente".
#   - mostrar_estado(self): imprime titular, saldo actual y cantidad de movimientos
#   - ultimo_movimiento(self): retorna el ultimo movimiento del historial
#                              o None si no hay movimientos
#
# PRUEBAS QUE DEBES PASAR:
#   c = CuentaBancaria('Hector')
#   c.depositar(500)
#   c.retirar(200)
#   c.retirar(1000)                   # Saldo insuficiente
#   c.mostrar_estado()                # saldo=300, 2 movimientos
#   print(c.ultimo_movimiento())      # ('retiro', 200)

# TU CODIGO AQUI


# -----------------------------------------------------------------------------
# EJERCICIO 3  -  Clase ContadorVisitas
# -----------------------------------------------------------------------------
# Crea una clase ContadorVisitas para llevar registro de visitas a un sitio web.
#
# ATRIBUTOS:
#   - url: la URL del sitio
#   - visitas: contador (empieza en 0)
#   - visitantes_unicos: un set vacio (para guardar IPs sin repetir)
#
# METODOS:
#   - registrar_visita(self, ip): suma 1 a visitas y agrega la ip al set
#   - resumen(self): imprime "{url}: {visitas} visitas, {N} unicos"
#   - visitas_promedio_por_unico(self): retorna visitas / cantidad de unicos
#                                        (cuidado con division por cero)
#
# PRUEBAS QUE DEBES PASAR:
#   c = ContadorVisitas('http://ister.edu.ec')
#   c.registrar_visita('10.0.0.1')
#   c.registrar_visita('10.0.0.2')
#   c.registrar_visita('10.0.0.1')    # mismo visitante
#   c.resumen()                        # 3 visitas, 2 unicos
#   print(c.visitas_promedio_por_unico())  # 1.5

# TU CODIGO AQUI


# -----------------------------------------------------------------------------
# EJERCICIO 4  -  Clase TareaPendiente (mini gestor de tareas)
# -----------------------------------------------------------------------------
# Crea una clase TareaPendiente con:
#
# ATRIBUTOS:
#   - descripcion: texto de la tarea
#   - prioridad: 'alta', 'media' o 'baja'
#   - completada: bool (empieza en False)
#
# METODOS:
#   - completar(self): marca completada=True e imprime "Tarea completada"
#   - es_urgente(self): True si prioridad='alta' Y no esta completada
#   - mostrar(self): imprime [X] si completada o [ ] si no, mas la descripcion
#                    y la prioridad. Ej: "[X] Cambiar firewall - alta"
#
# PRUEBAS QUE DEBES PASAR:
#   t = TareaPendiente('Actualizar OS', 'alta')
#   t.mostrar()                # [ ] Actualizar OS - alta
#   print(t.es_urgente())      # True
#   t.completar()              # Tarea completada
#   t.mostrar()                # [X] Actualizar OS - alta
#   print(t.es_urgente())      # False

# TU CODIGO AQUI


# =============================================================================
#  RETO FINAL (extra)
#  Combina los ejercicios anteriores en un programa principal que:
#  1. Crea una lista de 5 TareaPendiente con distintas prioridades
#  2. Las recorre y muestra solo las urgentes
#  3. Marca como completadas las que tengan 'firewall' en su descripcion
# =============================================================================
