#coding: utf-8

print("média aritmética")

n1 = int(input("insira a primeira média do aluno:"))
n2 = int(input("insira a segunda média do aluno:"))
m = (n1+n2) / 2 

if m > 7.0:
    print ("a média do aluno foi {} e ele está aprovado".format(m))
else:
    print ("a média do aluno foi {} e ele está reprovado".format(m))