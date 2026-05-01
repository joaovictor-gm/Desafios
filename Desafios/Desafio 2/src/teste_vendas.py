def testar_calculo_desconto():
    qtd = 15
    preco = 100.0
    valor_bruto = preco * qtd
    desconto = valor_bruto * 0.05 if qtd > 10 else 0

    assert desconto == 75.0
    print("Teste de desconto: OK")


if __name__ == "__main__":
    testar_calculo_desconto()
