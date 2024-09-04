def verifica_letra_a(s):
    contagem = 0
    for letra in s:
        if letra.lower() == 'a':
            contagem += 1
    return contagem

string = input("Informe uma string: ")

quantidade = verifica_letra_a(string)

if quantidade > 0:
    print(f"A letra 'a' aparece {quantidade} vez(es) na string.")
else:
    print("A letra 'a' não aparece na string.")
