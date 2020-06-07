print("costo del producto")
costo=float(input())
if costo>=200:
    cost1=costo-(costo*0.15)
    print("total a pagar: ",cost1)
else:
    if costo>100 and costo<200:
        cost2=costo-(costo*0.12)
        print("total a pagar: ",cost2)
    else:
        if costo>100 and costo<200:
            cost2=costo-(costo*0.12)
            print("total a pagar: ",cost2)
        else:
            cost3=costo-(costo*0.10)
            print("total a pagar: ",cost3)
      