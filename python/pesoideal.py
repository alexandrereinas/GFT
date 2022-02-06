sexo=input("Digite M para masculino e F para feminino: ")
altura=float(input("Digite a sua altura: "))
if (sexo=="M"):
    peso=(72.7*altura)-58
else:
    peso=(62.1*altura)-44.7
print(f"O seu peso ideal é de {peso:.2f}")


 