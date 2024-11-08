def mais_ataque(character):
    return character[1][0]

def mais_defesa(character):
    return character[1][1]

key=mais_ataque
key=mais_defesa

def main():
    characters = []
    count = 3

    for i in range(count):
        name = input("")
        ataque = int(input(f""))
        defesa = int(input(f""))
        characters.append([name,(ataque,defesa)])
    print(characters)

    ataque_mais_elevado = max(characters, key=mais_ataque)
    defesa_mais_elevada = max(characters, key=mais_defesa)

    print(f"Ataque {ataque_mais_elevado[0]} {ataque_mais_elevado[1][0]}")
    print(f"Defesa {defesa_mais_elevada[0]} {defesa_mais_elevada[1][1]}")

main()