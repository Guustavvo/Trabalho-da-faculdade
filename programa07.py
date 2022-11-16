n1 = float(input(&#39;Insira a primeira nota&#39;))
n2 = float(input(&#39;Insira a segunda nota&#39;))
n3 = float(input(&#39;insira a terceira nota&#39;))
p1= float(input(&#39;Insira a primeira peso&#39;))
p2 = float(input(&#39;Insira a segunda peso&#39;))
p3 = float(input(&#39;insira a terceira peso&#39;))
media_pondeirada1 = n1 * p1
media_pondeirada2 = n2 * p2
media_pondeirada3 = n3 * p3
soma_media = media_pondeirada1 + media_pondeirada2 + media_pondeirada3
soma_pesos = p1 + p2 + p3
media_final = soma_media / soma_pesos
print(soma_pesos)