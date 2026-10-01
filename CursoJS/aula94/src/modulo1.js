export const nome = "Guilherme";
export const sobrenome = "Marinho";
export const idade = 21;

function soma(x, y) {
  return x + y;
}

export class Pessoa {
  constructor(nome, sobrenome, idade) {
    this.nome = nome;
    this.sobrenome = sobrenome;
    this.idade = idade;
  }
}
