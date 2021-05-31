n=int(input("Digite un número entre 1 y 8 : "))

while(n<1 or n>8):
    print("Digite un número entero entre 1 y 8 : ")
    n=int(input("Digite un número entre 1 y 8 : "))

for i in range(1,n+1,1):
    print(" "*(n+1-i)+"#"*i)