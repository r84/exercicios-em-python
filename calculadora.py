print ("calculadora")

n1 = int(input("insira o primeiro número:"))
n2 = int(input("insira o segundo número:"))
op = input("qual operação deve ser feita?")

if op == "+":
    print (n1 + n2)
elif op == "-":
    print (n1 - n2)
elif op == "*":
    print (n1 * n2)
elif op == "/":
    print (n1 / n2)
