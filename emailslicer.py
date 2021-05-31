correo = input("Escribe tu correo: ").strip()

usuario = correo[:correo.index('@')]
dominio = correo[correo.index('@') + 1:]

print(f"Tu nombre de usuario es {usuario} y el dominio es {dominio}")