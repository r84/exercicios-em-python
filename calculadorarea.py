#coding: utf-8

print ("calculador de área")

l = float(input("largura da parede:"))
a = float(input("altura da parede:"))
ar = l * a
tinta = ar / 2

print("a sua parede tem {}x{} e uma área de {} metros quadrados".format(l,a,ar))
print("portanto serão necessários {} litros de tinta".format(tinta))

          