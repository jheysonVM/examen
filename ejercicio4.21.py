print("cantidad de billetes de 10 pesos")
bi10=int(input())
print("cantidad de billetes de 20 pesos")
bi20=int(input())
print("cantidad de billetes de 50 pesos")
bi50=int(input())
print("cantidad de monedas de 10 pesos")
mon10=int(input())
print("cantidad de monedas de 5 pesos")
mon5=int(input())
print("cantidad de monedas de 1 pesos")
mon1=int(input())
total1=(bi10*10)+(bi20*20)+(bi50*50)
total2=(mon10*10)+(mon5*5)+(mon1*1)
total=total1+total2
print("la cantidad total que hay en el monedero es: ",total)

