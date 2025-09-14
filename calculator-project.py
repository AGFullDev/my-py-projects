operação = int(input(
    "Escolha a operação que seseja: \n"
    "1 - Soma(+)\n"
    "2 - Subtração(-)\n"
    "3 - Multiplicacao(*)\n"
    "4 - Divisao(/)\n"
    "Digite o numero da operação que seseja: \n"
    ))

num1 = float(input("Digite o primeiro numero:"))
num2 = float(input("digite o segundo numero:"))

if operação == 1:
    print(f'Resultado:{num1 + num2}')
elif operação == 2:
    print(f'Resultado:{num1 - num2}')
elif operação == 3:
    print(f'Resultado: {num1 * num2}')
elif operação == 4:
    if num1 == 0 or num2 == 0:
        print('divisão por zero não é permitida')
    else:
        print(f'Resultado: {num1 / num2}')
else:
    print('Opção Invalida')

