"""from platform import python_version
print(python_version())

dia = str(input('Digite o dia da semana: '))
if dia == 'Segunda':
    print('Hoje fará sol!')
elif dia == 'Terça':
    print('Hoje vai chover!')
else:
    print('Sem previsão do tempo para o dia selecionado')
    
print('-' * 30)

nome = 'Bob'
idade = 18
if idade > 13 and nome == 'Bob':
    print('Ok, Bob, você está autorizado a entrar')
else:
    print('Desculpe, mas você não pode entrar')

print('-' * 30)

número = 4
if número > 5 or número % 2 == 0:
    print('Isso está sendo impresso porque uma das condições é vedadeira')
else:
    print('Isso está sendo impresso porque as duas condições são falsa')

disciplica = str(input('Digite a disciplina: '))
nota = float(input(f'Digite a sua nota em {disciplica}: '))
seme = int(input('Qual semestre você está? '))
if disciplica == 'Data Science' and nota >= 7 and seme != 1:
    print('Parabéns, você foi aprovado em Data Science!')
else:
    print('Que pena, você não foi aprovado em Data Science, mas não desanime, continue a estudar!')

lista = ['Abacaxi', 'Banana', 'Morango', 'Uva']
for i in range (0, len(lista)):
    print(lista[i])
    
help(lista.clear

def primeiraFun(arg1, *arg2):
    print(f'Óla {arg1}, seja bem vindo!!')
    for i in arg2:
        print(i)
lista = [1, 2, 3, 4, 5]
primeiraFun('Mário', lista)

from math import sqrt


def numpri(num):
    if num % 2 == 0 and num < 2:
        return "Este número não é primo."
    for i in range(3, int(sqrt(num)) + 1, 2):
        if num % i == 0:
            return "Este número não é primo."
    return "Este número é primo"


print(numpri(9)

text = 'Esta função é bastante útil para separar grande volumes de dados'
def token(texto):
    text = texto.upper()
    for i in text:
        if i == ' ':
            continue
        print(i)

print(token(text))"""

pares = [x for x in range (0, 101) if x % 2 == 0]
impares = [i for i in range (0, 101) if i % 2 != 0]
print(pares)
print(impares)