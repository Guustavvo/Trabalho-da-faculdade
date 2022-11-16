idade = int(input(&#39;Digite sua idade: &#39;))
if idade &lt; 21:
    print(&#39;Você é menor de idade&#39;)
elif idade &gt;= 21 and idade &lt; 65:
    print(&#39;Você esta na flor da idade&#39;)
elif idade &gt;= 65 and idade &lt;= 120:
    print(&#39;Você esta no bico do corvo&#39;)
else:
    print(&#39;Valor não encontrado!&#39;)