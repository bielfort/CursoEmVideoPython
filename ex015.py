# Aluguel de carros

p = 60
km = 0.15

d = float(input('Quantos dias ficou com o carro? '))
km1 = float(input('Quantos km rodou com o carro? '))

bill = (p * d) + (km * km1)

print('O preço a ser pago pelo carro é R${}'.format(bill))
