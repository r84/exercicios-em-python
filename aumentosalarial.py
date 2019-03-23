#coding: utf-8
print ("calculador de aumento salarial")

s = float(input("qual o valor do salário do funcionário:"))
d = float(input("qual a porcentagem de aumento:"))
c= (s*d) / 100
t= c + s

print ("o funcionário com o aumento de {}% no salário irá receber R${:.2f}".format(d,t))
