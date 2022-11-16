ladoA = int(input("Informe o valor do lado A"))
ladoB = int(input("Informe o valor do lado B:"))
ladoC = int(input("Informe o valor do lado C:"))
if ladoA == ladoB and ladoB == ladoC:
    print (&quot;Este é um Triangulo Equilatero&quot;)
elif ladoA != ladoB and ladoB != ladoC and ladoA != ladoC:
    print(&quot;Este é um Triangulo Escaleno&quot;)
else:
    print(&quot;Triangulo Isésceles&quot;)