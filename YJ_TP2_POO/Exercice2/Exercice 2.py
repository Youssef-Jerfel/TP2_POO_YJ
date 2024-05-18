import csv
def charger_pokemons_csv(nom_csv):
    with open(nom_csv, "r", encoding="utf-8") as f:
        lire_csv = csv.reader(f)
        pokm_dict = {}
        for i in lire_csv:
            cle=i[0]
            colonnes=[]
            for valeur in i[1:]:
                colonnes.append(int(valeur))
            pokm_dict[cle]=colonnes
    return pokm_dict



pkmn = charger_pokemons_csv("pokemon.csv")
for nom, stats in pkmn.items():
    print(f"{nom}: {stats}")

pkmn = charger_pokemons_csv("pokemon.csv")
print(isinstance(pkmn, dict))
print(isinstance(pkmn["Pikachu"], list))
print(isinstance(pkmn["Pikachu"][0], int))





