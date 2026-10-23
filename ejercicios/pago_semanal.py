def pago (horas,tarifa):
    if horas > 40:
        pagosem = (40 * tarifa) + ((horas - 40) * 1.5 * tarifa)
        return pagosem
    else:
        pagosem = horas * tarifa
        return pagosem

total_horas_p1 = float(input("Ingrese el numero de horas trabajadas persona #1: "))
tarifa_ordi_p1 = float(input("Ingrese la tarifa ordinaria persona #1: "))
total_horas_p2 = float(input("Ingrese el numero de horas trabajadas persona #2: "))
tarifa_ordi_p2 = float(input("Ingrese la tarifa ordinaria persona #2: "))

while total_horas_p1<0 or tarifa_ordi_p1<0 or total_horas_p2<0 or tarifa_ordi_p2<0: 
    print("Las horas y las tarifas no pueden ser negativas")
    total_horas_p1 = int(input("Ingrese el numero de horas trabajadas persona #1: "))
    tarifa_ordi_p1 = int(input("Ingrese la tarifa ordinaria persona #1: "))
    total_horas_p2 = int(input("Ingrese el numero de horas trabajadas persona #2: "))
    tarifa_ordi_p2 = int(input("Ingrese la tarifa ordinaria persona #2: "))

pagosem1 = pago (total_horas_p1, tarifa_ordi_p1)
pagosem2 = pago (total_horas_p2, tarifa_ordi_p2)
suma = pagosem1 + pagosem2

print ("El pago de la persona #1 es de ", pagosem1,"\n El pago de la persona #2 es de ", pagosem2, "\n La suma total de los dos pagos es de ", suma)




