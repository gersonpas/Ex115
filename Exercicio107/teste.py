#from Exercicio107 import moeda
import moeda
#from moeda import metade,diminuir, dobro

p = float(input('Digite o Preço: R$'))
print(f'A metade de R${p} é R${moeda.metade(p)}')
print(f'O dobro de R${p} é R${moeda.dobro(p)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(p, 10)}')
print(f'Diminuindo 10%, temos R${moeda.diminuir(p, 10)}')
