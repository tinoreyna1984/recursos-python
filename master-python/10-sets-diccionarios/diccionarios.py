'''
Diccionarios: son los arrays asociativos. Esto es, usan indices alfanumericos,
a modo de claves (keys). Similares a los objetos JSON
'''

persona = {
    'nombre' : 'Tino',
    'apellido' : 'Reyna',
    'edad' : 37
}

print(persona)
print(type(persona))
print(persona['apellido'])
print(persona['edad'])

# diccionarios dentro de listas

contactos = [
    {
        'nombre' : 'Tino',
        'apellido' : 'Reyna',
        'edad' : 37
    },
    {
        'nombre' : 'Gabriela',
        'apellido' : 'Lorentzen',
        'edad' : 31
    },
    {
        'nombre' : 'Jose',
        'apellido' : 'Cuadros',
        'edad' : 20
    },
    {
        'nombre' : 'Alberto',
        'apellido' : 'Perez',
        'edad' : 25
    }
]

print(contactos)
print(contactos[1])
print(contactos[1]['edad'])
contactos.append({
    'nombre' : 'Juan',
    'apellido' : 'Ramirez',
    'edad' : 25
})
print(contactos)

for contacto in contactos:
    print(f"Nombre: {contacto['nombre']}")
    print(f"Apellido: {contacto['apellido']}")
    print(f"Edad: {str(contacto['edad'])}")

