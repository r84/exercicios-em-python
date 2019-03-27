# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado

#coding: utf-8

print ("aluguel de carros")

dias = int(input("quantos dias foram usados o carro?"))
km = float(input("quantos km foram rodados?"))
totaldias = dias * 60
totalkm = km * 0.15
total = totaldias + totalkm

print ("total a pagar: R${:.2f}".format(total))