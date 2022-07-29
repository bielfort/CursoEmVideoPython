#exercicio parede

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))

dimensao = largura * altura
tinta = dimensao / 2

print('A dimensão da sua parede é de {:.2f}m².'.format(dimensao))
print('Para pintar sua parede você precisara de {:.2f}l de tinta'.format(tinta))
