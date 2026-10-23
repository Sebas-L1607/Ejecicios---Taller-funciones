def precio_unitario (preciot, gramos):
        precio_por_gramo = preciot / gramos
        return precio_por_gramo

precio1 = int(input("Digite el precio del paquete #1: "))
peso1 = int(input("Digite el peso del paquete #1: "))
precio2 = int(input("Digite el precio del paquete #2: "))
peso2 = int(input("Digite el peso del paquete #2: "))

while precio1<0 or precio2<0 or peso1<=0 or peso2<=0:
    print ("Los precios no pueden ser negativos y los pesos no puede ser iguales o menos a 0")
    precio1 = int(input("Digite nuevamente el precio del paquete #1: "))
    peso1 = int(input("Digite nuevamente el peso del paquete #1: "))
    precio2 = int(input("Digite nuevamente el precio del paquete #2: "))
    peso2 = int(input("Digite nuevamente el peso del paquete #2: "))

precio_gramo_p1 = precio_unitario (precio1,peso1)
precio_gramo_p2 = precio_unitario (precio2,peso2)

if precio_gramo_p1 > precio_gramo_p2:
    print("el precio por gramo del parquete 1 es de ",precio_gramo_p1,"\n Y el precio por gramo del paquete 2 es de: ",precio_gramo_p2)
    print("El paquete que mas conviene es Paquete 2")
else:
    print("el precio por gramo del parquete 1 es de ",precio_gramo_p1,"\n Y el precio por gramo del paquete 2 es de: ",precio_gramo_p2)
    print("El paquete que mas conviene es Paquete 1")