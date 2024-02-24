# Ejemplo de modus tollens en Python

# Premisas
p = False  # Si está lloviendo
q = False  # Entonces el suelo está mojado

# Regla: Si está lloviendo, entonces el suelo está mojado
def modus_tollens(p, q):
    if not q:
        print("El suelo no está mojado, por lo tanto no está lloviendo.")
    else:
        print("No se puede determinar si está lloviendo.")

# Aplicar modus tollens
modus_tollens(p, q)
