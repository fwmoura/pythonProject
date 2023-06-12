times = ("Corinthians", "Palmeiras","Santos","Gremio","Cruzeiro","Flamengo","Vasco",'Chapecoense', 'Atletico','Botafogo','Atlhetico - PR','Bahia','Sao Paulo',"Sport",'vitória','Coritiba', 'Avai', 'Ponte Preta','Goias')

print("=-"*15)
print(f"Lista de times do Brasileirão: {times}")
print("=-"*15)
print(f"Os 5 primeiros colocados são: {times[0:5]}")
print("=-"*15)
print(f"Os 4 últimos colocados são: {times[-4:]}")
print("=-"*15)
print(f"Times em ordem alfabética {sorted(times)}")
print("=-"*15)
print(f"A chapecoense está na {times.index ('Chapecoense')+1}ª posição")

