## Cálculo simples de soma, onde a saída é o resultado da soma de todos os valores que estão dentro da lista abaixo.
contador = 0
valores = [10, 20, 30, 40, 50]

for valor in valores:
    soma = sum(valores)
    print(f'a soma total é: {soma}')




## Testando o laço de repetição 'for' para a exibição do print em uma quantidade conhecida de vezes.
for contador in range(5):
    print('Bem-vindo ao Buscante!')

## Alternativa menos polida utilizando o While ao invés de for
while contador < 4:
    print('Bem-vindo ao Buscante!')
    contador += 1 
##  Nestes casos, em que situação cada uma seria melhor?





## Uso do 'continue' para substituir "none" da lista por "projeto ausente" na saída.
projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

for projeto in projetos:
    if projeto == None:
        print('Projeto Ausente')
        continue
    else:
        print(f'{projeto}')







## Uso do 'break' para interromper uma busca na lista.
livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]

for livro in livros:
    if livro == 'O Hobbit':
         print(f'livro encontrado: {livro}')
         break
    else:
        continue






## Simulação simples de vendas de um livro com estoque inicial de cinco exemplares, com saída de estoque esgotado.
estoque = 5

while estoque >= 0:
    print(f'Venda realizada! Estoque restante: {estoque}')
    estoque -= 1
print('estoque esgotado')







# Mensagens personalizadas conforme números pares ou ímpares, com saída de anúncio de uma promoção.
numeros = [2, 3, 4, 1, 5, 6, 7, 8, 9, 10]

# Aprendi nessa lição que "range" pode rearranjar a ordem dos números, mesmo que eles não estejam em ordem na lista. Muito útil em banco de dados
for numero in range(10, 0, -1):
    if numero % 2 == 0:
        print(f'Faltam apenas {numero} segundos - Não perca essa oportunidade!')
    else:
        print(f'A contagem continua: {numero} segundos restantes.')
print('Aproveite a promoção agora!')





## Sistema de filtragem de livros. A funcionalidade deve percorrer uma lista de livros e exibir o nome de cada livro disponível em estoque. 
## No entanto, se o livro estiver esgotado, ele deve ser ignorado durante a iteração
livros = [
    {"nome": "1984", "estoque": 5},
    {"nome": "Dom Casmurro", "estoque": 0},
    {"nome": "O Pequeno Príncipe", "estoque": 3},
    {"nome": "O Hobbit", "estoque": 0},
    {"nome": "Orgulho e Preconceito", "estoque": 2}
]

for livro in livros:
    if livro['estoque'] == 0:
        continue
    print(f"Livro disponível: {livro['nome']}")





##  Sistema de cadastro para um site de leitura. É necessário que usuários insiram um nome de usuário e uma senha válidos. As regras são as seguintes:
## 1. O nome de usuário deve ter pelo menos 5 caracteres.
## 2. A senha deve ter pelo menos 8 caracteres.
senha = input('senha: ')
user = input('usuário: ')

if len(senha) < 8:
    print('Senha deve conter oito caracteres')
elif len(user) < 5:
    print('Usuário deve conter cinco caracteres')
else:
    print('Cadastro realizado com sucesso!')
    