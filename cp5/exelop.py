# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou 
# igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na tela "Você precisa trabalhar!"
dia = str(input('Qual dia da semana é hoje? ')).lower()
if dia in 'domingo' or dia in 'sabado' or dia in 'sábado':
    print('Hoje é dia de descanso!')
else:
    print('Infelizmente, você precisa trabalhar!!')
print('-' * 60)

# Exercício 2 - Crie uma lista de 5 frutas e verifique se a fruta 'Morango' faz parte da lista
fruits = ['Banana', 'Manga', 'Laranja', 'Uva', 'Mamão']
if 'Morango' in fruits:
    print('Há morango nesta lista')
else:
    print('Não há morango nesta lista!')
print('-' * 60)

# Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os resultados em uma 
# lista
tp = (3, 8, 5, 1)
lista = []
for i in tp:
    mult = i * 2
    lista.append(mult)
print(lista)
print('-' * 60)

# Exercício 4 - Crie uma sequência de números pares entre 100 e 150 e imprima na tela
for i in range(100, 151, 2):
    print(i, end=' ')
print()
print('-' * 60)

# Exercício 5 - Crie uma variável chamada temperatura e atribua o valor 40. Enquanto temperatura for maior que 35, 
# imprima as temperaturas na tela

temp = 40
while temp > 35:
    print(temp, end=' ')
    temp -= 1
print()
print('-' * 60)

# Exercício 6 - Crie uma variável chamada contador = 0. Enquanto counter for menor que 100, imprima os valores na tela,
# mas quando for encontrado o valor 23, interrompa a execução do programa
count = 0
while count < 100:
    print(count, end=' ')
    if count == 23:
        break
    count += 1
print()
print('-' * 60)

# Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou igual a 20, 
# adicione à lista, apenas os valores pares e imprima a lista
pares = []
num = 4
while num <= 20:
    if num % 2 == 0:
        pares.append(num)
    num += 1
print(pares)
print('-' * 60)

# Exercício 8 - Transforme o resultado desta função range em uma lista: range(5, 45, 2)
nums = range(5, 45, 2)
print(list(nums))
print('-' * 60)

# Exercício 9 - Faça a correção dos erros no código abaixo e execute o programa. Dica: são 3 erros.
temperatura = float(input('Qual a temperatura? '))
if temperatura > 30:
    print('Vista roupas leves.')
else:
    print('Busque seus casacos.')
print('-' * 60)

# Exercício 10 - Faça um programa que conte quantas vezes a letra "r" aparece na frase abaixo. Use um placeholder na 
# sua instrução de impressão

# “A gratidão é a virtude das almas nobres. O quão feliz é uma pessoa depende da profundidade de sua gratidão.” 

frase = "A gratidão é a virtude das almas nobres. O quão feliz é uma pessoa depende da profundidade de sua gratidão." 
érres = 0
for i in frase:
    if i in 'r':
        érres += 1
print(f'Na frase acima, há {érres} letras "r".')