maior = 0
menor = 0
totalPessoas = 10
for pessoa in range(1, 11):
  idade = int(input("Digite a idade: "))
  if idade >= 18:
    maior += 1
  else:
    menor += 1

print("Quantidade de pessoas maior de idade: ", maior)
print("Quantidade de pessoas menor de idade: ", menor)

print("Porcentagem de pessoas menores de idade = ", (menor*100)/totalPessoas, "%")
print("Porcentagem de pessoas maiores de idade = ", (maior*100)/totalPessoas, "%")