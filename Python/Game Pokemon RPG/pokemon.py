import random


class Pokemon:

    def __init__(self, especie, level=random.randint(1,100), nome = None):
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
    tipo = "Eletrico"

    def atacar(self, pokemon):
        print("{} atacou um raio do trovão {}!".format(self, pokemon))


class PokemonFogo(Pokemon):
    tipo = "Fogo"

    def atacar(self, pokemon):
        print("{} atacou uma bola de fogo no {}!".format(self, pokemon))


class PokemonAgua(Pokemon):
    tipo = "Agua"

    def atacar(self, pokemon):
        print("{} atacou um jato d agua no {}!".format(self, pokemon))


class PokemonPlata(Pokemon):
    tipo = "Planta"

    def atacar(self, pokemon):
        print("{} atacou um folhas no {}!".format(self, pokemon))


