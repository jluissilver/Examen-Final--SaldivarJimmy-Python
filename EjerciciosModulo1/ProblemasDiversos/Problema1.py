monto = float(input('Ingrese cantidad de dinero depositada en la cuenta de ahorros : ' ))
i = 0.04

for a in range(1,4):
    monto = monto * (1+i)
    print(f"El monto al final del año {a} es : {round(monto,2)}")
    
    #c1 = c + c * i c * (1 + i)