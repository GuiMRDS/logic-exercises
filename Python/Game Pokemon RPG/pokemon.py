class Pokemon:
    def __init__(self, tipo, especie):
        self.tipo = tipo
        self.especie = especie

    def __str__(self):
        return "{} ({})".format(self.especie, self.tipo)

    def atacar(self, pokemon):
        print("{} atacou {}!".format(self.especie, pokemon.especie))

meu_pokemon = Pokemon("fogo", "charmander")
meu_pokemon_do_visinho = Pokemon("eletrico", "pikachu")

print(meu_pokemon)
print(meu_pokemon_do_visinho)
print()

meu_pokemon_do_visinho.atacar(meu_pokemon)
meu_pokemon.atacar(meu_pokemon_do_visinho)