print('-' * 30)
print(f'{"Bubble Sort":^30}')
print('-' * 30)
ordem = []
for c in range (1, 11):
    num = float(input(f'Digite o {c}º valor: '))
    ordem.append(num)
while True:
    cres = str(input('Deseja ordenar em ordem crescente ou decrescente? [C/D] ')).strip()[0]
    if cres in 'Cc':
        ordem.sort()
        print(f'A lista de números digitados em ordem crescente é: {ordem}')
        break
    elif cres in 'Dd':
        ordem.sort(reverse=True)
        print(f'A lista de números digitados em ordem decrescente é: {ordem}')
        break
    else:
        print('\033[31mOcorreu um erro, tente novamente!!\033[m')
