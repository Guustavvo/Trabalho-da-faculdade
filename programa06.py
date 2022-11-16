salario_fixo = float(input(&quot;insira o salario fixo&quot;))
venda = float(input(&quot;Insira o valor das vendas: &quot;))
comissão = venda * (4/100)
salario_final = salario_fixo + comissão
print(&quot;Comissão: &quot; , comissão , &quot; Salário final: &quot;, salario_final)