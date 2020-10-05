salario_bruto = float(input("Informe seu salário Bruto: "))
desc_vale_transporte = input("Informe se aderiu a vale transporte com SIM ou NAO: ")
valor_vale_alimentacao = float(input("Informe o valor do seu vale alimentacao"))
desc_vale_alimentacao = float(input("Informe a porcentagem de desconto do seu vale alimentacao ou refeiçao: "))
desc_plano_odontologico = float(input("Possui plano odontologico? Se houver desconto em folha favor informar o valor."))
des_plano_saude = float(input("Possui plano Saude? Se houver desconto em folha favor informar o valor."))


# TABELA INSS
valor_inss_A = 1045
valor_inss_B = 2089.60
valor_inss_C = 3134.40
valor_inss_D = 6101.06

# TABELA IRRF

valor_irrf_A = 1903.98
valor_irrf_B = 2826.65
valor_irrf_C = 3751.05
valor_irrf_D = 4664.68


# Base Para Calculo INSS

aliquota_minima = float((valor_inss_A * 7.5) / 100)
aliquota_minima2 = float(((valor_inss_B - valor_inss_A) * 9) / 100)
aliquota_minima3 = float(((valor_inss_C - valor_inss_B) * 12) / 100)
aliquota_minima4 = float(((valor_inss_D - valor_inss_C) * 14) / 100)

if salario_bruto <= valor_inss_A:
    valor = ((salario_bruto * 7.5) / 100)


if (salario_bruto > valor_inss_A) and (salario_bruto <= valor_inss_B):
    valor = (((salario_bruto - valor_inss_A) * 9) / 100) + aliquota_minima



elif (salario_bruto > valor_inss_B) and (salario_bruto <= valor_inss_C):
    valor = (((salario_bruto - valor_inss_B) * 12) / 100) + aliquota_minima + aliquota_minima2



elif (salario_bruto > valor_inss_C) and (salario_bruto <= valor_inss_D):
    valor = (((salario_bruto - valor_inss_C) * 14) / 100) + aliquota_minima + aliquota_minima2 + aliquota_minima3


elif salario_bruto > valor_inss_D:
    valor = 713.09



# SALARIO DESCONTO INSS

salario_desc_inss = salario_bruto - valor
print("o Salario descontado de INSS e " , salario_desc_inss)




# Base Para Calculo IRRF



aliquota_minima_ir2= float(((valor_irrf_B - valor_irrf_A) * 7.5) / 100)
aliquota_minima_ir3= float(((valor_irrf_C - valor_irrf_B) * 15) / 100)
aliquota_minima_ir4 = float(((valor_irrf_D - valor_irrf_C) * 22.5) / 100)


if salario_desc_inss < valor_irrf_A :
    valor_ir = 0

elif (salario_desc_inss >= valor_irrf_A) and (salario_desc_inss <= valor_irrf_B):
    valor_ir = (((salario_desc_inss - valor_irrf_A) * 7.5) / 100)
    print("Verificar o valor ", valor_ir)

elif (salario_desc_inss > valor_irrf_B) and (salario_desc_inss <= valor_irrf_C):
    valor_ir = (((salario_desc_inss - valor_irrf_B) * 15) / 100) + aliquota_minima_ir2
    print("Verificar o valor ", valor_ir)

elif (salario_desc_inss > valor_irrf_C) and (salario_desc_inss <= valor_irrf_D):
    valor_ir = (((salario_desc_inss - valor_irrf_C) * 22.50) / 100) + aliquota_minima_ir2 + aliquota_minima_ir3
    print("Verificar o valor ", valor_ir)

elif salario_desc_inss > valor_irrf_D:
    valor_ir = (((salario_desc_inss - valor_irrf_D) * 27.50) / 100) + aliquota_minima_ir2 + aliquota_minima_ir3 + aliquota_minima_ir4
    print("Verificar o valor ", valor_ir)



# DESCONTOS ADICIONAIS

if desc_vale_transporte == "SIM":
    vt = (salario_bruto * 6)/100

if desc_vale_alimentacao > 0:
    va = (valor_vale_alimentacao * desc_vale_alimentacao) / 100






# SALARIO LIQUIDO

total_descontos = valor + valor_ir + vt + va + desc_plano_odontologico + des_plano_saude

print("INSS VALOR = ", valor)
print("IRRF valor = ", valor_ir)
print("VT valor = ", vt)
print("VA valor = ", va)
print("Plano Odontologico valor = ", desc_plano_odontologico)
print("Plano de Saude valor = ", des_plano_saude)


salario_liquido = salario_bruto - total_descontos

print("TOTAL E " , salario_liquido)
