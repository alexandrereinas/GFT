n1=float(input("Digite a nota 1: "))
n2=float(input("Digite a nota 2: "))
media=(n1*0.4+n2*0.6)
if n1 >10 or n2>10:
    print("nota inválida")
else:
    if (media>=5.0):
        print("Aprovado")
    else:
        print("Reprovado")
print("Fim de programa")