#coding: utf-8

print("conversor de medidas")

m = float(input("insira a medida em metros:"))
cm = m * 100
mm = m * 1000

print("a medida {} tem {} centímetros e {} milímetros".format(m,cm,mm))