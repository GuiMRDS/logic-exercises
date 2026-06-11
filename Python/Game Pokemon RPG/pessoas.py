import random

from pokemon import *

NOMES = [
        "João", "Isabela", "Lorena", "Francisco", "Ricardo", "Maria",
        "Diego", "Patricia", "Macella", "Giulia", "Leticia", "Gary"
]

POKEMONS = [
    PokemonFogo("Chamander"), PokemonFogo("Charmilion"), PokemonFogo("Charizard"),
    PokemonEletrico("Pikachu"), PokemonEletrico("Raichu"),
    PokemonAgua("Squirte"), PokemonAgua("Watertooler"), PokemonAgua("Balstoise"),
    PokemonPlata("Bulbasauro"), PokemonPlata("Vernosauro"),
]

class Pessoa:
    def __init__(self, nome = None, pokemons=[]):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons

    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):
        if self.pokemons:
            print("Pokemons de {}:".format(self.nome))
            for pokemon in self.pokemons:
                print(pokemon)
        else:
            print("{} não tem nenhum pokemon".format(self))


class Player(Pessoa):
    tipo = 'player'

    def captutar(self, pokemon):
        self.pokemons.append(pokemon)
        print('{} capturou {}'.format(self, pokemon))


class Inimigo(Pessoa):
    tipo = 'inimigo'

    def __init__(self, nome=None, pokemons=[]):
        if not pokemons:
            for i in range(random.randint(1,6)):
                pokemons.append(random.choice(POKEMONS))

        super().__init__(nome=nome, pokemom=pokemons)


meu_inimigo = Inimigo()
print(meu_inimigo)
meu_inimigo.mostrar_pokemons()