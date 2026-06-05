class Empleado:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property
    def edad(self):
        return self._edad

    @property
    def fecha_nacimiento(self):
        """Getter: fecha_nacimiento"""
        from datetime import datetime
        


emp = Empleado("", "", 15)
print(emp.edad)