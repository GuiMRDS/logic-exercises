class Pokemon:
    def __init__(self, tipo, especie, level=1, nome = None):
        self.tipo = tipo
        self.especie = especie
        self.level = level

        if nome:
            self.nome = nome
        else:
            self.nome = especie

    def __str__(self):
        return "{} ({})".format(self.nome, self.level)

    def atacar(self, pokemon):
        print("{} atacou {}!".format(self, pokemon))



class PokemonEletrico(Pokemon):
    def atacar(self, pokemon):
        print("{} atacou um raio do trovão {}!".format(self, pokemon))

    def dar_choque(self):
        print("Deu choque!")


meu_pokemon = PokemonEletrico("Elerico", 'Pikachu')
pokemon_meu_amigo = Pokemon("Fogo", 'Charmamder')

meu_pokemon.atacar(pokemon_meu_amigo)
pokemon_meu_amigo.atacar(meu_pokemon)
