valor_nota1=float(input("Qual o valor da primeira nota"))
print(valor_nota1)
valor_nota2=float(input("Qual o valor da segunda nota"))
print(valor_nota2)
valor_nota3=float(input("Qual o valor da terceira nota"))
print(valor_nota3)
valor_nota4=float(input("Qual o valor da quarta nota"))
print(valor_nota4)
media=(valor_nota1+valor_nota2+valor_nota3+valor_nota4)/4
print(media)
if media >= 7.0: 
    print("Aprovado")
elif media>=5: 
    print("Em recuperacao")
else:
    print("Reprovado")