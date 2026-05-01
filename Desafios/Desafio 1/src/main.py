from processamento import calcular_impostos, formatar_relatorio

funcionarios = []

while True:
    print("\n1. Cadastrar | 2. Relatório | 3. Salvar | 4. Sair")
    opcao = input("Opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        if nome == "":
            print("Nome vazio!")
            continue
        
        tipo = input("Tipo (estagiario/clt/freelancer): ").lower()
        
        try:
            if tipo == "freelancer":
                valor = float(input("Valor/Hora: "))
                horas = float(input("Horas: "))
                bruto, inss, irrf, liquido = calcular_impostos(tipo, valor, horas)
            elif tipo in ["clt", "estagiario"]:
                valor = float(input("Salário: "))
                bruto, inss, irrf, liquido = calcular_impostos(tipo, valor)
            else:
                print("Tipo inválido!")
                continue

            if bruto <= 0:
                print("Valor deve ser maior que zero")
                continue

            funcionarios.append({
                "nome": nome,
                "tipo": tipo.title(),
                "bruto": bruto,
                "inss": inss,
                "irrf": irrf,
                "liquido": liquido
            })
            print("Cadastrado!")
        except ValueError:
            print("Erro: Digite apenas números para valores e horas.")

    elif opcao == "2":
        linhas, rodape = formatar_relatorio(funcionarios)
        for linha in linhas:
            print(linha, end="")
        print(rodape)

    elif opcao == "3":
        linhas, rodape = formatar_relatorio(funcionarios)
        with open("relatorio.txt", "w") as arquivo:
            arquivo.writelines(linhas)
            arquivo.write(rodape)
        print("Salvo em relatorio.txt!")

    elif opcao == "4":
        break