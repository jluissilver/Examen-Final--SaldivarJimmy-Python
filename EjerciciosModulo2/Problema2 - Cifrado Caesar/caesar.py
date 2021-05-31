abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
mayus = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lista = []
lista2= []
final =[]
n = int(input("Escriba el número de desplazamientos : "))
if n>26:
    le = int(n/26)
    n = n-(26*le)
for i in range(n,len(abc)):
    
    lista.append(abc[i])
  
for i in range(0,n):
    lista.append(abc[i])
for i in range(n,len(mayus)):
    lista2.append(mayus[i])
    
for i in range(0,n):
    lista2.append(mayus[i])
for i in range(len(mayus)):
    abc.append(mayus[i])
for i in range(len(lista2)):
    lista.append(lista2[i])
abc.append(" ")
abc.append(",")
lista.append(" ")
lista.append(",")       


w = input("Escriba texto : ")
for i in range(len(w)):
    u= abc.index(w[i])
    
    final.append(lista[u])
fin = "".join(final)
print(fin)