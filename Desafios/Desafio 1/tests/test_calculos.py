from src.processamento import calcular_impostos

def test_calculo_clt_com_irrf():
    bruto, inss, irrf, liquido = calcular_impostos("clt", 3000)
    assert inss == 240
    assert irrf == 300
    assert liquido == 2460

def test_calculo_freelancer():
    bruto, inss, irrf, liquido = calcular_impostos("freelancer", 100, 10)
    assert bruto == 1000
    assert irrf == 50
    assert liquido == 950

print("Testes concluídos com sucesso!")