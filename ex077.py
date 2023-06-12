palavras = ["aprender","programar","python","gratis"]

for p in palavras:
    print(f"\n na palavra {p.upper()} temos", end= " ")
    for letra in p:
        if letra in "aeiou":
            print(letra, end= "")
print("")
