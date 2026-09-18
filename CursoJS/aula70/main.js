const pessoa = {
  nome: "Guilherme",
  sobrenome: "Marinho",
};

const chave = "sobrenome";

console.log(pessoa[chave]);

console.log(pessoa["nome"]);
console.log(pessoa["sobrenome"]);

// Factory functions / Constructor functions / Classes
const pessoa1 = new Object();
pessoa1.nome = "Guilherme";
pessoa1.sobrenome = "Marinho";
pessoa1.idade = 21;
pessoa1.falarNome = function () {
  console.log(`${this.nome} está falando seu nome.`);
};
pessoa1.getDataNascimento = function () {
  const dataAtual = new Date();
  return dataAtual.getFullYear() - this.idade;
};

pessoa1.falarNome();
console.log(pessoa1.getDataNascimento());

function criarPessoa(nome, sobrenome) {
  return {
    nome,
    sobrenome,
    nomeCompleto() {
      return `${this.nome} ${this.sobrenome}`;
    },
  };
}

const p1 = criarPessoa("Guilherme", "Marinho");
console.log(p1.nomeCompleto());

function Pessoa(nome, sobrenome) {
  this.nome = nome;
  this.sobrenome = sobrenome;
}

// {} <- this
const p2 = new Pessoa("Marcella", "Fogaça");
console.log(p2);
