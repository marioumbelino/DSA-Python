# Exercício 1 - Crie uma função que imprima a sequência de números pares entre 1 e 20 (a função não recebe parâmetro) 
# e depois faça uma chamada à função para listar os números

def seqnum():
    for i in range(2, 21, 2):
        print(i, end=' ')
    print()
seqnum()

# Exercício 2 - Crie uam função que receba uma string como argumento e retorne a mesma string em letras maiúsculas.
# Faça uma chamada à função, passando como parâmetro uma string

def mai(string):
    print(string.upper())
mai('Mário')

# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e 
# imprima a lista

def addlista(lista):
    lista.append(int(input('Qual elemento deseja adicionar? ')))
    lista.append(int(input('Qual elemento deseja adicionar? ')))
        
lista1 = [1, 2, 3, 4]
addlista(lista1)
print(lista1)

# Exercício 4 - Crie uma função que receba um argumento formal e uma possível lista de elementos. Faça duas chamadas 
# à função, com apenas 1 elemento e na segunda chamada com 4 elementos

def func(arg1, *arg2):
    print(arg1)
    for i in arg2:
        print(i)
func("I'm the best")
func('Mário', lista1)

# Exercício 5 - Crie uma função anônima e atribua seu retorno a uma variável chamada soma. A expressão vai receber 2 
# números como parâmetro e retornar a soma deles
soma1 = lambda num1, num2: num1 + num2
print(soma1(5, 10))

# Exercício 6 - Execute o código abaixo e certifique-se que compreende a diferença entre variável global e local
total = 0
def soma( arg1, arg2 ):
    total = arg1 + arg2
    print ("Dentro da função o total é: ", total)
    return total


soma( 10, 20 )
print ("Fora da função o total é: ", total)

# Exercício 7 - Abaixo você encontra uma lista com temperaturas em graus Celsius
# Crie uma função anônima que converta cada temperatura para Fahrenheit
# Dica: para conseguir realizar este exercício, você deve criar sua função lambda, dentro de uma função 
# (que será estudada no próximo capítulo). Isso permite aplicar sua função a cada elemento da lista
# Como descobrir a fórmula matemática que converte de Celsius para Fahrenheit? Pesquise!!!
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda num: (num * 9 / 5) + 32, Celsius)
print (list(Fahrenheit))

# Exercício 8 - Crie uma list comprehension que imprima o quadrado dos números de 1 a 10
print([x ** 2 for x in range(1,11)])

# Exercício 9 - Crie uma list comprehension que imprima as palavras com a letra a no nome
palavras = ["maça", "coiote", "banana", "terreno", "Python"]
print([i for i in palavras if 'a' in i])

# Exercício 10 - Crie uma list comprehension que imprima os números menores que 5 em um intervalo de 1 a 10
print([p for p in range(1, 11) if p < 5])