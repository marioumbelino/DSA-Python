print('-' * 20)
print('Calculadora')
print('-' * 20)
num1 = float(input('Digite o primerio número: '))
num2 = float(input('Digite o segundo número: '))
while True:
    op = str(input('Qual operação deseja realizar? Adição, subtração, multiplicação ou divisão? ')).strip().lower()
    if op in 'adição':
        ad = num1 + num2
        print(f'A soma entre {num1:.2f} e {num2:.2f} é igual a {ad:.2f}')
        break
    elif op in 'subtração':
        su = num1 - num2
        print(f'A subtração entre {num1:.2f} e {num2:.2f} é igual a {su:.2f}')
        break
    elif op in 'multiplicação':
        mul = num1 * num2
        print(f'A multiplicação entre {num1:.2f} e {num2:.2f} é igual a {mul:.2f}')
        break
    elif op in 'divisão':
        if num2 != 0:
            div = num1 / num2
            print(f'A divisão entre {num1:.2f} e {num2:.2f} é igual a {div:.2f}')
        else:
            print('A divisão entre qualquer número por 0 é indeterminado!')
        break
    else:
        print('\033[31mOcorreu um erro, tente novamente!\033[m')