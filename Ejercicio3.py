v1 =float(input("Ingrese primer voltaje: "))
v2 =float(input("Ingrese segundo voltaje: "))
v3 =float(input("Ingrese tercero voltaje: "))

prom = (v1+v2+v3/3)

if prom < 115:
    print(f"Voltaje correcto: {prom}")
elif prom > 115 and prom < 220:
    print(f"Alto voltaje : {prom}")
elif prom > 220:
    print(f"PELIGGRRO: {prom}")