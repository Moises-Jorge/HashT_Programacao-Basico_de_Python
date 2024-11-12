dict_produtos = {
    "airpod": 2000,
    "ipad": 9000,
    "iphone": 6000,
    "macbook": 11000
}





# Desafio 01: Cadastrar um novo produto no dicionario (se ele nao existir). Caso o produto exista, ele vai editar o seu valor.
nome_produto = str(input("Nome do Produto: ")).lower()
preco_produto = float(input("Preco do Produto: "))

dict_produtos[nome_produto] = preco_produto
print(dict_produtos)


# Desafio 02: Actualizar o preco de todos os produtos para novos valores que sao 10% a mais do preco original.
for produto in dict_produtos:
    dict_produtos[produto] = dict_produtos[produto] + (dict_produtos[produto] * 0.1)
print(dict_produtos)