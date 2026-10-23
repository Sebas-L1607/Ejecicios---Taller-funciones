def area (base,altura):
    resultado = base * altura / 2
    return resultado

base1 = int(input("Digite la base del triangulo #1: "))
altura1 = int(input("Digite la altura del triangulo #1: "))
base2 = int(input("Digite la base del triangulo #2: "))
altura2 = int(input("Digite la base del triangulo #2: "))

while base2 <=0 or base1<=0 or altura2<=0 or altura1<=0:
    print("Las medidas tiene que ser expresadas en numeros mayores que 0\n")
    base1 = int(input("Digite nuevamente la base del triangulo #1: "))
    altura1 = int(input("Digite nuevamente la altura del triangulo #1: "))
    base2 = int(input("Digite nuevamente la base del triangulo #2: "))
    altura2 = int(input("Digite nuevamente la base del triangulo #2: "))

resultado_area1 = area (base1,altura1)
resultado_area2 = area (base2,altura2)
suma_areas = resultado_area2 +  resultado_area1

print("El area del triangulo #1 es: ", resultado_area1)
print("El area del triangulo #2 es: ", resultado_area2)
print ("La suma de las areas es de: ", suma_areas)
