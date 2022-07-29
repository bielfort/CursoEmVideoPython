# Reajuste salárial

#salario
s = float(input('Qual o salário do funcionario? '))
#reajuste
r = 0.15
novo = (s * r) + s
print('O salário atual do funcionário é {}, portanto com o reajuste de 15% ficará {:.2f}'.format(s, novo))
