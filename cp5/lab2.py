from math import sqrt, factorial
from time import sleep
print('-' * 40)
print(f'{"Calculadora Python":^40}')
print('-' * 40)
while True:
    print('\nSelecione qual operação deseja realizar: ')
    print('1 - Adição \n2 - Subtração \n3 - Multiplicação \n4 - Divisão \n5 - Potenciação \n6 - Raiz Quadrada \n7 - Fatorial \n')
    while True:
        ope = int(input(''))
        if ope in [1, 2, 3, 4, 5, 6, 7]:
            break
        else:
            print('Opção inválida, tente novamente!')
    if ope in [1, 2, 3, 4]:
        num1 = float(input('Digite o primeiro valor: '))
        num2 = float(input('Digite o segundo valor: '))
        if ope == 1:
            print(f'A adição entre {num1} e {num2} é igual a {num1 + num2}')
        elif ope == 2:
            print(f'A subtração entre {num1} e {num2} é igual a {num1 - num2}')
        elif ope == 3:
            print(f'A multiplicação entre {num1} e {num2} é igual a {num1 * num2}')
        else:
            print(f'A divisão entre {num1} e {num2} é igual a {num1 / num2}')
    elif ope == 5:
        num1 = float(input('Digite o número que deseja elevar: '))
        num2 = float(input('Digite o valor a qual deseja que o número seja elevado: '))
        print(f'O resultado é igual a {num1 ** num2}!')
    elif ope == 7:
        num1 = int(input('Deseja saber o fatorial de qual número? '))
        print(f'O fatorial de {num1} é igual a {factorial(num1)}')
    else:
        num1 = float(input('Deseja saber a raiz quadrada de qual número? '))
        print(f'A raiz quadrada de {num1} é igual a {sqrt(num1)}')
    res = ' '
    while True:
        res = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if res in 'SN':
            break
        else:
            print('\033[31mErro!! Tente novamente!\033[m')
    if res in 'N':
        break
print('Finalizando...')
sleep(1)
print('--Volte sempre--')
