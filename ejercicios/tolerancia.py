def valor_absoluto(numero):
    if numero < 0:
        numero = numero * -1
    return numero

objetivo = float(input(" Ingrese la medida objetivo: "))
tolerancia = float(input("ingrese la tolerancia de la medida: "))
medida1 = float(input(" Ingrese la medida #1: "))
medida2 = float(input("ingrese la medida #2: "))

while tolerancia<0:
    print("La  tolerancia tiene que tener un valor mayor igual a 0")
    tolerancia = float(input("ingrese nuevamente la tolerancia de la medida: "))


lit_sup = valor_absoluto( objetivo + tolerancia )
lit_inf =valor_absoluto( objetivo - tolerancia )

medidainf = 0
if lit_inf <= medida1 <=lit_sup:    
    print("Medida 1 tiene criterio de aceptacion VERDADERO")
else: 
    print("Medida 1 tiene criterio de aceptacion FALSO")

if lit_inf<= medida2 <=lit_sup:
    print ("Medida 2 tiene criterio de aceptacion VERDADERO")
else:
    print ("Medida 2 tiene criterio de aceptacion FALSO")








