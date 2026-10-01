class Pessoa {
  constructor(nome, sobrenome) {
    this.nome = nome;
    this.sobrenome = sobrenome;
  }

  falar() {
    console.log(`${this.nome} está falando.`);
  }

  comer() {
    console.log(`${this.nome} está comendo.`);
  }

  beber() {
    console.log(`${this.nome} está bebendo.`);
  }
}

const p1 = new Pessoa("Guilherme", "Marinho");
const p2 = new Pessoa("Marcella", "Fogaça");
const p3 = new Pessoa("Bruno", "Marinho");

console.log(p1);
console.log(p2);
console.log(p3);

console.log(p1.falar());
console.log(p2.comer());
console.log(p3.beber());
