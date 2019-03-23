#coding: utf-8

print("conversor de temperatura")

c = float(input("qual a temperatura em celsius:"))
f = (c * 1.8) + 32

print ("{:.2f} graus celsius convertidos em fahrenheidt são {:.2f} graus".format(c,f))