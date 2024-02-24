# Ejemplo de modus ponens en Python

# Premisas
p = True  # Si está lloviendo
q = True  # Entonces el suelo está mojado

# Regla: Si está lloviendo, entonces el suelo está mojado
def modus_ponens(p, q):
    if p:
        print("Está lloviendo, por lo tanto el suelo está mojado.")
    else:
        print("No se puede determinar si el suelo está mojado.")

# Aplicar modus ponens
modus_ponens(p, q)
