# listas multidimensionales

contactos = [
    ["Gabriela Lorentzen", "Guayaquil", 31, "gabriela.lorentzen@gmail.com"],
    ["Tino Reyna", "Guayaquil", 37, "tinoreyna1984@gmail.com"],
    ["Juan Ramirez", "Quito", 30, "jramirez@gmail.com"]
]

for contacto in contactos:
    print(f"Item {contactos.index(contacto)+1}:")
    for elemento in contacto:
        print(elemento)


