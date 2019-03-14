#coding: utf-8

print("calculador de descontos")

pr = float(input("valor do produto:"))
d = int(input("valor do desconto:"))
v = pr * d
total = v / 100
prnovo = pr - total

print ("o produto que antes custava R${:.2f} vai custar agora R${:.2f}.".format(pr,prnovo))