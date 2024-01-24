v1 =float(input("INgrese primer voltaje: "))
v2 =float(input("INgrese segundo voltaje: "))
v3 =float(input("INgrese tercero voltaje: "))
v4 =float(input("INgrese cuarto voltaje: "))
v5 =float(input("INgrese quinto voltaje: "))




prom = (v1+v2+v3+v4+v5)/5

if prom > 220:
    print(f"Alto voltaje :| = {prom}")
else:
    print(f"Voltaje correcto :D = {prom}")


