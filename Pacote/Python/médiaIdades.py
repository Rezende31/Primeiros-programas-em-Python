# Calculando a média das idades
maxPessoas = 4
contador = 0
soma = 0

while contador < maxPessoas:
  aux = int(input("Digite a idade: "))
  if aux >= 0:
    soma += aux
    contador += 1
  else:
    print("Só serão válidas idades maiores que 0. ")

print("A média das idades é: ", (soma/maxPessoas))