#Desconto

p = float(input('Qual o preço do produto? '))
d = 0.05
print('O preço do produto é R${:.2f}, na promoção com o desconto de 5% o produto vai custar R${:.2f}.'.format(p, p-(p*d)))
