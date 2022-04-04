"""
Set: tipo de dato que contiene elementos sin orden especifico ni indexado
"""

personas = {"Primera persona", "Segunda persona", "Tercera persona"}
print(personas)
print(type(personas))

# agregar y quitar elementos del set
personas.add("Cuarta persona")
print(personas)
personas.remove("Primera persona")
print(personas)

