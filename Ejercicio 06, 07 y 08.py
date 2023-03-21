#clase
class Persona:
    def __init__(self, nombre=None, edad=None, dni=None):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni    

#setter and getters 

#nombre
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if not isinstance (nuevo_nombre, str):
            raise TypeError ("Dato incorrecto")
        self._nombre = nuevo_nombre
#edad
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad < 0:
            raise ValueError("La edad debe ser mayor a 0")
        self._edad = nueva_edad

#dni
    @property
    def dni(self):
        return self._dni
    
    @dni.setter
    def dni(self, nuevo_dni):
        if not isinstance (nuevo_dni, int):
            raise TypeError ("Dato incorrecto")
        self._dni = nuevo_dni
  

def mostrar(persona):
    print(f"Nombre: {persona.nombre}, Edad: {persona.edad}, DNI: {persona.dni}")
    
def es_mayor_de_edad(Persona):
    if Persona.edad >17:
        return True
    else:
        return False

    
lorena = Persona("Lorena", 34, 34283916)
carlos = Persona("Carlos", 13, 11021931)

mostrar(lorena)
print(es_mayor_de_edad(lorena))
mostrar(carlos)
print(es_mayor_de_edad(carlos))


#EJERCICIO 7
class Cuenta:
    def __init__(self, titular, cantidad=0):
        self.titular = titular
        self.cantidad = cantidad

    def get_titular(self):
        return self.titular

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def mostrar_cuenta(self):
        print("Titular:", self.titular.nombre)
        print("Cantidad:", self.cantidad)

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad

    def retirar(self, cantidad):
        if cantidad > 0:
            self.cantidad -= cantidad

    def __str__(self):
        return f"Titular: {self.titular.nombre}, Cantidad: {self.cantidad}"

#EJERCICIO 8

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    def get_bonificacion(self):
        return self.bonificacion

    def set_bonificacion(self, bonificacion):
        self.bonificacion = bonificacion

    def es_titular_valido(self):
        if self.Persona.edad >= 18 and self.Persona.edad < 25:
            return True
        else:
            return False

    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)

    def mostrar(self):
        print("Cuenta Joven")
        print("Titular:", self.titular.nombre)
        print("Cantidad:", self.cantidad)
        print("Bonificación:", self.bonificacion)