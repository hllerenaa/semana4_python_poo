# Tarea PEA1 - Sistema de inventario de dispositivos de red

> **Vale:** 5 puntos (Parcial 1)
> **Entrega:** 31/05/2026 - 23:55 (Moodle)
> **Formato:** archivo unico `apellido_nombre_PEA1.py`
> **Modalidad:** Individual

---

## 1. Objetivo

Aplicar los 5 tipos de funciones/metodos vistos en clase y al menos 2 pilares de la POO en un programa real que gestiona dispositivos de red.

## 2. Contexto

Eres administrador de red. Necesitas un sistema simple para llevar el inventario de routers, switches y otros equipos. Tu sistema debe permitir:

- Agregar dispositivos manualmente o desde CSV
- Validar que la IP tenga formato correcto
- Detectar si la IP es publica o privada
- Mostrar un reporte de cada equipo

## 3. Lo que debes incluir (OBLIGATORIO los 5 tipos)

| Tipo | Nombre sugerido | Que debe hacer |
|---|---|---|
| 1. Funcion suelta | `imprimir_banner()` | Imprime titulo decorativo. Fuera de la clase. |
| 2. Metodo normal | `reportar(self)` | Imprime IP, modelo y ubicacion |
| 3. @property con setter | `ip` con `@ip.setter` | Valida que la IP tenga formato correcto. Lanza ValueError si no |
| 4. @staticmethod | `es_ip_privada(ip)` | True si esta en rango privado RFC 1918 (10.x, 172.16-31.x, 192.168.x) |
| 5. @classmethod | `desde_csv(cls, linea)` | Crea un Dispositivo desde texto 'ip,modelo,ubicacion' |

## 4. Programa principal

Despues de la clase, agrega:

```python
if __name__ == "__main__":
    imprimir_banner()
    d1 = Dispositivo('10.0.0.1', 'Cisco-2960', 'DC-A')
    d2 = Dispositivo.desde_csv('192.168.1.1, MikroTik, Oficina')
    d1.reportar()
    d2.reportar()
    print(Dispositivo.es_ip_privada('10.0.0.5'))   # True
    print(Dispositivo.es_ip_privada('8.8.8.8'))    # False
    try:
        d3 = Dispositivo('999.0.0.1', 'X', 'Y')
    except ValueError as e:
        print('Error capturado:', e)
```

## 5. Salida esperada

```
=================================================
    SISTEMA DE INVENTARIO DE DISPOSITIVOS
=================================================

Dispositivo: 10.0.0.1
  Modelo:    Cisco-2960
  Ubicacion: DC-A

Dispositivo: 192.168.1.1
  Modelo:    MikroTik
  Ubicacion: Oficina

10.0.0.5  es privada?  True
8.8.8.8   es privada?  False

Error capturado: IP invalida: 999.0.0.1
```

## 6. Como empezar

1. **Lee** el archivo `esqueleto.py`. Tiene la estructura lista con `TODO:` indicando que completar.
2. **Renombra** el archivo a `apellido_nombre_PEA1.py` (ej: `llerena_hector_PEA1.py`).
3. **Completa** cada TODO en orden.
4. **Ejecuta** tu archivo en cada paso para verificar que funciona.
5. **Sube** a Moodle antes del 31/05/2026 a las 23:55.

## 7. Rubrica (5 puntos)

| Criterio | Puntaje |
|---|---|
| Funcion suelta `imprimir_banner()` | 0.5 pts |
| Metodo normal `reportar(self)` | 0.75 pts |
| @property con setter (validacion de IP) | 1.5 pts |
| @staticmethod `es_ip_privada(ip)` | 1.0 pt |
| @classmethod `desde_csv(cls, linea)` | 1.0 pt |
| Programa principal completo + estilo | 0.25 pts |
| **TOTAL** | **5.0 pts** |

## 8. Penalizaciones

- Entrega tardia: -1.0 pt por dia (maximo 2 dias tarde)
- Copia: nota 0 para ambos
- Uso de IA sin declarar: nota 0
- Codigo que no ejecuta por errores de sintaxis: maximo 2 pts

## 9. Pistas

Si te atascas, revisa estos archivos del proyecto:

- `03_property/teoria_y_ejemplos.py` para la validacion de IP
- `04_staticmethod/teoria_y_ejemplos.py` para `es_ip_privada`
- `05_classmethod/teoria_y_ejemplos.py` para `desde_csv`
- `06_pilares_poo/1_encapsulamiento.py` para entender por que protegemos `_ip`

---

**Ing. Hector Llerena, MSc** - Lenguaje de Programacion Python - ISTER 2026-1
