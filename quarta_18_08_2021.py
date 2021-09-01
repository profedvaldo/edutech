#este é um comentário
#imports, é importar os modulos para executar algo
from random import seed
from random import randint

#alimentar
seed(1)

valor = randint(0, 10)

valorSugerido = input("Digite um valor ->")

valorSugerido = int(valorSugerido)

if valor == valorSugerido :
  print("acertou!!!")

else:
  print("errooooooou")

print(valor)
