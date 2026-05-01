def cadastrar_produto(produtos):
    print("\nCadastro de Produto")
    try:
        nome = input("Nome do produto: ").strip()
        if not nome:
            print("Erro: O nome não pode ser vazio.")
            return

        for p in produtos:
            if p['nome'].lower() == nome.lower():
                print(f"Erro: O produto '{nome}' já existe.")
                return

        preco = float(input("Preço unitário: R$ "))
        estoque = int(input("Quantidade inicial: "))

        if preco <= 0 or estoque < 0:
            print("Erro: Valores inválidos para preço ou estoque.")
            return

        produtos.append({"nome": nome, "preco": preco, "estoque": estoque})
        print(f"Sucesso: {nome} cadastrado!")
    except ValueError:
        print("Erro: Entrada inválida. Use apenas números.")
