print('=== Bem Vindo ao simuldador de investimentos! ===')

valor_aplicação = float(input('Digite o valor da aplicação:'))
tempo_aplicado = int(input('Expectativa de tempo em meses:'))

juros_ano = float(input('Digite o valor dos juros ao ano:'))

juros_mensais = round(juros_ano/12, 2)
juros_mensais = juros_mensais/100
print(juros_mensais)

for i in range(tempo_aplicado):
    valor_aplicação += valor_aplicação*juros_mensais
    print(f'mes {i}: Valor total: R$ {valor_aplicação:.2f}')