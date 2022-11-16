peso = float(input(&quot;informe o seu peso &quot;))
altura = float(input(&quot;Informe sua altura &quot;))
imc = peso / (altura * altura)
print(f&quot;{imc:.1f}&quot;)
if (imc &lt; 18.5):
 print(&quot;Abaixo do peso&quot;)
elif (imc &lt;= 25):
print(&quot;Peso normal&quot;)
elif (imc &gt; 25):
 print(&quot; Acima do peso&quot;)
else:
 print(&quot;Obesidade&quot;)