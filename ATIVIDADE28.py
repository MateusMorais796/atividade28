# Crie um programa que receba uma lista com o nome de 5 produtos e outra lista com as quantidades em estoque de cada um desses produtos. O programa deve exibir os produtos que estão com o estoque zerado.

# Exemplo de entrada:
# Produtos: ['Arroz', 'Feijão', 'Macarrão', 'Açúcar', 'Sal']
# Estoque: [10, 0, 5, 0, 20]

# Exemplo de saída:
# Produtos com estoque zerado: Feijão, Açúcar

produtos = []
estoque = []
for a in range(0, 5):
    produtos.append(str(input("Digite o nome do produto ")))
    estoque.append(int(input("Digite a quantidade de estoque do produto digitado acima ")))


produtos_zerados = []

for p in range(len(produtos)):
    if estoque[p] == 0:
        produtos_zerados.append(produtos[p])

p_zerado = ','.join(produtos_zerados)
print(f'os produtos com estoque zerado são: {p_zerado}')
