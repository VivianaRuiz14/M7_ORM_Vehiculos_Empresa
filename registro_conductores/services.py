from registro_conductores.models import Conductor

def crear_conductor(nombre, apellido, fecha_nacimiento):
    c = Conductor(nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento)
    c.save()