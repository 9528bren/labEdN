# Informações do produto
nome_produto = "Cadeira Infantil"
preco_unitario = 12.40
quantidade = 3

# Cálculo do preço total
preco_total = preco_unitario * quantidade

# Exibindo as informações formatadas
print("Produto:", nome_produto)
print(f"Preço unitário: R$ {preco_unitario:.2f}".replace('.', ','))
print("Quantidade:", quantidade)
print(f"Preço total: R$ {preco_total:.2f}".replace('.', ','))
