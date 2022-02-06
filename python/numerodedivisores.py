numero=int(input("Insira um numero  "))
contador=1
divisores=0
while (contador<numero+1):
    if (numero%contador)==0:
        print(f"E um divisor {contador}")
        divisores+=1
        contador+=1
    else:
        contador+=1
print(f"O numero {numero} tem   {divisores}")   