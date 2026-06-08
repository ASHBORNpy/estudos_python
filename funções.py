##  Função que receba o ano de nascimento e o ano atual e retorne à idade correspondente
nasc = input('Digite o ano de nascimento: ')
atual = input('Digite o ano atual: ')

def idade(nasc, atual):
    idade = int(atual) - int(nasc)
    return idade
print('A idade é ' + str(idade(nasc, atual)))

## Outra alternativa interessante de código
def calcular_idade(ano_nascimento, ano_atual): 
    return ano_atual - ano_nascimento 
 
nascimento = int(input("Digite o ano de nascimento: ")) 
atual = int(input("Digite o ano atual: ")) 
idade = calcular_idade(nascimento, atual) 
print(f"A idade é {idade} anos.")








## Função que recebe uma palavra e retorna a quantidade de caracteres
def contar_caracteres(palavra):
    return len(palavra)
palavra = input('Digite uma palavra: ')
print(f'A palavra {palavra} tem {contar_caracteres(palavra)} caracteres.')






## Programa que exiba uma saudação personalizada dependendo da hora do dia que o usuário acessa a plataforma.
## Regras:
## 1. Se for antes das 12h, exibir "Bom dia";
## 2. Entre 12h e 18h, exibir "Boa tarde";
## 3. Após 18h, exibir "Boa noite".

def saudacao(hora): 
    if hora < 12: 
        return "Bom dia!" 
    elif hora < 18: 
        return "Boa tarde!" 
    else: 
        return "Boa noite!" 
 
hora_atual = int(input("Digite a hora atual (0-23): ")) 
print(saudacao(hora_atual)) 
## Dificil... preciso estudar melhor esse aqui.







## Pedro está criando um sistema de cadastro de produtos para sua loja e percebeu que todos os números de telefone dos clientes estão 
## armazenados como strings. No entanto, para facilitar buscas e validações, ele precisa que esses números sejam tratados como inteiros.

def converter_telefones(lista):  
   return [int(telefone) for telefone in lista] 

def verifica_tipos(lista):  
   for num in lista:  
       if not isinstance(num, int):  
          return "Erro na conversão."  
   return "Todos os números foram convertidos corretamente!" 

telefones = ["11987654321", "21912345678", "31987654321", "11911223344"] 
telefones_convertidos = converter_telefones(telefones) 
print(verifica_tipos(telefones_convertidos))






## Carlos trabalha em um comércio e precisa saber o valor total de vendas realizadas no dia. 
## As vendas são informadas em uma única linha separadas por espaços.
## Sua tarefa é criar um programa que receba essa linha, converta os valores para números e exiba o total.

valores = input("Digite os valores das vendas: ").split() 
total = sum(map(float, valores)) 
print(f"O total de vendas foi: {total}")
## não era list->map->sum, sum pode vir primeiro. Lição aprendida. .split = O método split() em Python 
## é usado para dividir uma string em uma lista, com base em um separador especificado. Caso nenhum separador seja informado, o padrão será qualquer espaço em branco.







## Crie um programa que receba uma lista de números e exiba apenas os pares usando a função filter().
# Filtrar números pares de uma lista
numeros = input("Digite os números separados por espaço: ").split()

pares = filter(lambda x: int(x) % 2 == 0, numeros)
print("Números pares:", " ".join(pares))







## Clara está gerenciando o estoque de sua loja e recebeu duas listas separadas: uma contendo os nomes dos produtos e outras com seus respectivos preços. Para facilitar a organização, ela precisa combinar essas listas de forma que cada produto seja associado ao seu preço.
## Crie um programa que junte as listas e exiba o resultado no formato produto: preço

produtos = input("Digite os produtos separados por vírgula: ").split(",") 
precos = input("Digite os preços separados por vírgula: ").split(",") 
 
for produto, preco in zip(produtos, precos): 
    print(f"{produto.strip()}: {preco.strip()}")





## Joana está participando de um processo seletivo para uma vaga de desenvolvedora e recebeu um desafio técnico de criar uma calculadora para somar, subtrair, multiplicar e dividir dois números.
## Sua tarefa é criar um programa usando funções lambda que receba dois números e um operador matemático escolhido pelo usuário (+, -, * ou /) e exiba o resultado correspondente.

soma = lambda x, y: x + y 
subtrai = lambda x, y: x - y 
multiplica = lambda x, y: x * y 
divide = lambda x, y: x / y if y != 0 else "Erro: Divisão por zero" 

x = float(input("Digite o primeiro número: ")) 
y = float(input("Digite o segundo número: ")) 

operacao = input("Escolha a operação (| + | - | * | / |): ") 
 
if operacao == '+': 
    print(f"O resultado é: {soma(x, y)}") 
elif operacao == '-': 
    print(f"O resultado é: {subtrai(x, y)}") 
elif operacao == '*': 
    print(f"O resultado é: {multiplica(x, y)}") 
elif operacao == '/': 
    print(f"O resultado é: {divide(x, y)}") 
else: 
    print("Operação inválida")







## Miguel está desenvolvendo um sistema de cupons de desconto e precisa de uma forma para aplicar diferentes taxas de desconto sobre os valores das compras.
## Diante deste problema, crie uma closure que gere uma função capaz de calcular o preço final com um desconto fixo definido pelo usuário.

def criar_desconto(porcentagem):  

   def calcular_preco(valor):  

       return valor - (valor * (porcentagem / 100))  

   return calcular_preco 

desconto = float(input("Digite a porcentagem de desconto: "))  
calcular_preco_final = criar_desconto(desconto) 
valor = float(input("Digite o valor da compra: "))  
print(f"Preço final com desconto: {calcular_preco_final(valor)}")






## Paulo está desenvolvendo um programa para calcular valores acumulados em um sistema financeiro. Ele precisa somar os todos os números inteiros de 1 até n, onde n é um valor escolhido pelo usuário.
## Ajude Paulo criando uma função recursiva que receba um número n e retorne a soma de todos os números inteiros de 1 até N.

def soma_recursiva(n): 
    if n == 1: 
        return 1 
    return n + soma_recursiva(n - 1) 
 
numero = int(input("Digite um número: ")) 
print(f"A soma de 1 a {numero} é: {soma_recursiva(numero)}")





## Conclusão final: Preciso praticar muito ainda a parte das funções. Tive bastante dificuldade em resolver os exercícios