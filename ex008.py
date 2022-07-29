# conversor de medidas

medida = float(input('Informe um valor em metros para conversão: '))
km = float(medida/1000)
hm = float(km*10)
dam = float(hm*10)
cm = float(medida*100)
mm = float(cm*10)

print('A medida de {:.2f} Metros corresponde a\n{:.2f} Quilômetros'.format(medida, km))
print('{:.2f} Hectômetro\n{:.2f} Decâmetro'.format(hm, dam))
print('{:.2f} Centímetros\n{:.2f} Milímetros'.format(cm, mm))
