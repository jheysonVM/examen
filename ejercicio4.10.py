contador=0
suma=0
numero=1
while numero !=0:
    numero=int(input("ingrese la edad (finalice digitando 0) "))
    
    if numero !=0:
        suma+=numero
        contador+=1
if contador==0:

    print("no digito ninguna edad ")
else:
    promedio=suma/contador
    print("el promedio de las {} edades igual a {}.".format(contador,promedio))
