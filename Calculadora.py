# Calculadora em python

def calculo(val, val2, oper):
    if oper == 1:
        resultado = int(val) + int(val2)
        print("\n {} + {} = {} ".format(val, val2, resultado))
    elif oper == 2:
        resultado = int(val) - int(val2)
        print("\n {} - {} = {} ".format(val, val2, resultado))
    elif oper == 3:
        resultado = int(val) * int(val2)
        print("\n {} * {} = {} ".format(val, val2, resultado))
    elif oper == 4:
        resultado = int(val) / int(val2)
        print("\n {} / {} = {} ".format(val, val2, resultado))

print("********************** Python Calculadora ********************** \n")
print("Selecione o núemro da operação desejada: \n")
print("1 - Soma \n"
      "2 - Subtração \n"
      "3 - Multiplicação \n"
      "4 - Divisão \n")

operacao = int(input("Digite sua opção (1/2/3/4):"))

if operacao in [1, 2, 3, 4]:
    valor1 = input("Digite o primeiro número:")
    valor2 = input("Digite o segundo número:")
    calculo(valor1, valor2, operacao)
else:
    print("Opção invalida!")



