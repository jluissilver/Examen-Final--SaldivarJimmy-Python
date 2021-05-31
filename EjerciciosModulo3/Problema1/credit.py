x=input("Digite el número de tarjeta : ")
lista = list(x)
lista1 = []
lista2 = []
lista3 = []
mo = 0
mf = []
multi = 0
suma = 0
fin = []
for i in range(0,len(lista),2):
    multi = int(lista[i]) * 2
    lista1.append(multi)

for i in range(len(lista1)):
    if lista1[i]>9:
        mo = lista1[i]
        mf = list(str(mo))
        lista2.append(mf[0])
        lista2.append(mf[1])
    else:
        lista2.append(lista1[i])

for i in range(len(lista2)):
    suma = suma + int(lista2[i])

for i in range(1,len(lista),2):
    lista3.append(lista[i])
    suma = suma + int(lista[i])

fin = list(str(suma))

if fin[1] == '0':
    print('VALIDO')
else:
    print('NO VALIDO')

if lista[0] =='3' and lista [1] =='4':
    print("AMEX")
if lista[0] =='3' and lista [1] =='7':
    print("AMEX")
if lista[0] =='5' and lista [1] =='1':
    print("MASTERCARD")
if lista[0] =='5' and lista [1] =='2':
    print("MASTERCARD")
if lista[0] =='5' and lista [1] =='3':
    print("MASTERCARD")
if lista[0] =='5' and lista [1] =='4':
    print("MASTERCARD")
if lista[0] =='5' and lista [1] =='5':
    print("MASTERCARD")
if lista[0] =='4':
    print("VISA")