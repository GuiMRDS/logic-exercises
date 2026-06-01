class Pokemon:
    def __init__(self, tipo, especie, level, nome = None, ):
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
        print("{} atacou {}!".format(self, pokemon.especie))



meu_pokemon = Pokemon("fogo", "charmander", nome="Bagela", level=50)
print(meu_pokemon)
