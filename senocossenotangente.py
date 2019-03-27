#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. 

#coding: utf-8

print ("seno,cosseno e tangente")

import math
ang = float(input("insira um ângulo:"))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))

print ("seno: {:.2f} graus".format(seno))
print ("cosseno: {:.2f} graus".format(cosseno))
print ("tangente: {:.2f} graus".format(tangente))