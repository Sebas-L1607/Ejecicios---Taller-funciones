def subtotal (base,descuento):
    basereal = base *(1-descuento/100)
    return basereal

def descimp (subtotal,impuestos):
    total = subtotal * (1+impuestos/100)
    return total

sueldo_base = int(input("Ingrese el sueldo base: $"))

while sueldo_base < 0: 
    print("Sueldo base no puede ser negativo")
    sueldo_base = int(input("Ingrese nuevamente el sueldo base: $"))

descuentos = int(input("Ingrese el porcentage de descuento "))

while 0 > descuentos > 100: 
    print ("El porcentaje de descuento tiene que se de 0 a 100.")
    descuentos = int(input("Ingrese nuevamente el porcentage de descuento "))


impuesto_real = int(input("Ingrese el porcentage de impuesto "))

while 0 > impuesto_real > 100: 
    print ("El porcentaje de impuestos tiene que ser positivo.")
    impuesto_real = int(input("Ingrese nuevamente el porcentage de impuestos "))

sueldo_subtotal = subtotal(sueldo_base,descuentos)
sueldo_after_impuesto = descimp (sueldo_subtotal,impuesto_real)

print ("El Subtotal es de: ", sueldo_subtotal)
print ("El total es de: ",sueldo_after_impuesto)

