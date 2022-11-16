numero = int(input(&quot;Digite um numero   &quot;))
print(&quot;           Menu de opções     &quot;)
print(&quot;    1: somar doi numeros &quot;)
print(&quot;    2: Numeros ao quadrado&quot;)
escolha = int(input(&quot;  qual opção você deseja   &quot;))
if escolha == 1:
    numero2 = int(input(&quot; Digite o numero que sera somado ao numero escolhido
anteriormente   &quot;))
    print (&quot;O resultado da soma dos numeros escolhidos é =&quot;, numero + numero2)
else:
        print(&quot;O numero escolhido elevado ao quadrado é=&quot;, numero**2)