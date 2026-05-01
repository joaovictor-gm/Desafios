def realizar_venda(produtos, vendas):
    """Lógica para processar uma venda e atualizar o estoque."""
    if not produtos:
        print("\nErro: Não há produtos cadastrados para venda.")
        return

    print("\nRealizar Venda")
    try:
        cliente = input("Nome do cliente: ").strip()
        if not cliente:
            print("Erro: O nome do cliente é obrigatório.")
            return

        print("\nProdutos Disponíveis:")
        for i, p in enumerate(produtos):

            info = f"[{i}] {p['nome']} - R$ {p['preco']:.2f}"
            print(f"{info} Estoque: {p['estoque']}")

        indice = int(input("\nSelecione o índice (número) do produto: "))
        if indice < 0 or indice >= len(produtos):
            print("Erro: Índice inválido.")
            return

        produto_sel = produtos[indice]

        if produto_sel['estoque'] <= 0:
            print(f"Erro: O produto '{produto_sel['nome']}' está esgotado.")
            return

        msg_qtd = f"Quantidade Disponível ({produto_sel['estoque']}): "
        qtd = int(input(msg_qtd))

        if qtd <= 0:
            print("Erro: A quantidade deve ser pelo menos 1.")
            return
        if qtd > produto_sel['estoque']:

            print(f"Erro: Estoque insuficiente. "
                f"Temos apenas {produto_sel['estoque']} em estoque.")
            return

        valor_bruto = produto_sel['preco'] * qtd
        desconto = 0.0
        if qtd > 10:
            desconto = valor_bruto * 0.05

        valor_final = valor_bruto - desconto
        produto_sel['estoque'] -= qtd

        nova_venda = {
            "cliente": cliente,
            "produto": produto_sel['nome'],
            "quantidade": qtd,
            "valor_bruto": valor_bruto,
            "desconto": desconto,
            "valor_final": valor_final
        }

        vendas.append(nova_venda)
        print(f"\nVenda concluída! Total a pagar: R$ {valor_final:.2f}")

    except ValueError:
        print("Erro: Entrada inválida. Use números para índice e quantidade.")


def formatar_relatorio(vendas):
    """Transforma os dados das vendas em uma string formatada."""
    if not vendas:
        return "Nenhuma venda registrada no sistema."

    saida = "Relatório de Vendas\n"
    total_arrecadado = 0

    for v in vendas:
        saida += f"\nCliente: {v['cliente']}\n"
        saida += f"Produto: {v['produto']}\n"
        saida += f"Quantidade: {v['quantidade']}\n"
        saida += f"Valor Bruto: R$ {v['valor_bruto']:.2f}\n"
        saida += f"Desconto: R$ {v['desconto']:.2f}\n"
        saida += f"Valor Final: R$ {v['valor_final']:.2f}\n"
        saida += "-" * 30 + "\n"
        total_arrecadado += v['valor_final']

    saida += f"\nTotal arrecadado pela loja: R$ {total_arrecadado:.2f}\n"
    return saida


def salvar_arquivo(vendas):
    """Gera um arquivo .txt com o conteúdo do relatório."""
    if not vendas:
        print("Erro: Não há dados para salvar.")
        return

    try:
        nome_arquivo = "relatorio_vendas.txt"
        conteudo = formatar_relatorio(vendas)

        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(conteudo)

        print(f"Sucesso: Arquivo {nome_arquivo} "
            f"gerado com sucesso no diretório")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")
