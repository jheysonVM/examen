print("ingrese el nombre del trabajador")
nombre=input()
print("ingrese su salario por hora")
salario=float(input())
print("cuantas horas trabaja al dia")
horastrab=int(input())
if salario<-150:
        total=salario-(salario*0.05)
else:
    if salario>150 and salario<300:
        total=salario-(salario*0.07)
    else:
        if salario>-300 and salario<450:
            total=salario-(salario*0.09)
salariototal=total*horastrab*7
print("el salario semanal de "+nombre+" es:",salariototal)