from pokemon import *

class Pessoa:
    def __init__(self, nome = None, pokemons=[]):
        if nome:
            self.nome = nome
        else:
            self.nome = "Pessoa anonima"

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



eu = Player('Guilherme')
pokemon_selvagem = PokemonFogo("Charmader")

print('Antes de caputurar')
eu.captutar(pokemon_selvagem)

eu.mostrar_pokemons()