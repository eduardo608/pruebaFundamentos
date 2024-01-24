base = float(input("Digite la base del triangulo equilatero: "))
alt = float(input("Digite la altura del triangulo equilatero: "))

area = (base * alt)/2

if area > 1000:
    print(f"Datos no validos: {area}")
else:
    print(f"El area es: {area}")