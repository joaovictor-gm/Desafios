def calcular_impostos(tipo, valor_base, horas = 0):
    bruto = 0
    inss = 0
    irrf = 0

    if tipo == "freelancer":
        bruto = valor_base * horas
        irrf = bruto * 0.05

    elif tipo == "clt":
        bruto = valor_base
        inss = bruto * 0.08
        if bruto > 2000:
            irrf = bruto * 0.10
            
    elif tipo == "estagiario":
        bruto = valor_base

    liquido = bruto - inss - irrf
    return bruto, inss, irrf, liquido

def formatar_relatorio(funcionarios):
    linhas = []
    total_empresa = 0
    for f in funcionarios:
        linha = f"{f['nome']} ({f['tipo']}) - Bruto: R$ {f['bruto']:.2f} | Líquido: R$ {f['liquido']:.2f}\n"
        linhas.append(linha)
        total_empresa += f['liquido']
    
    rodape = f"Total Empresa: R$ {total_empresa:.2f}\n"
    return linhas, rodape