class Pokemon:

    def __init__(self, tipo, especie):
        self.tipo = tipo
        self.especie = especie


meu_pokemon = Pokemon("fogo", "charmander")

print(meu_pokemon.especie)
print(meu_pokemon.tipo)