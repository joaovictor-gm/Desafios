from src.produtos import cadastrar_produto
from src.operacoes import realizar_venda, formatar_relatorio, salvar_arquivo


def exibir_menu():
    print("\n=== SISTEMA DE GESTÃO DE VENDAS ===")
    print("1. Cadastrar Produto")
    print("2. Realizar Venda")
    print("3. Gerar Relatório")
    print("4. Salvar Relatório em Arquivo")
    print("5. Sair")


def main():
    estoque_produtos = []
    historico_vendas = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-5): ")

        if opcao == "1":
            cadastrar_produto(estoque_produtos)
        elif opcao == "2":
            realizar_venda(estoque_produtos, historico_vendas)
        elif opcao == "3":
            print("\n" + formatar_relatorio(historico_vendas))
        elif opcao == "4":
            salvar_arquivo(historico_vendas)
        elif opcao == "5":
            print("Saindo do sistema... Até logo!")
            break
        else:
            print("Opção inválida! Escolha um número de 1 a 5.")


if __name__ == "__main__":
    main()
