const array = [1, 2, 3];
array.push(4);
array[0] = "Guilherme";

console.log(array);

const nome01 = "Guilherme";
const sobreNome01 = "Marinho";
const idade01 = 25;

const pessoa1 = {
  nome: "Guilherme",
  sobrenome: "Marinho",
  idade: 21,
};

const pessoa2 = {
  nome: "Marcella",
  sobrenome: "Fogaça",
  idade: 21,
};

console.log(pessoa1.nome);
console.log(pessoa2.sobrenome);

function criarPessoa(nome, sobrenome, idade) {
  return {
    nome: nome,
    sobrenome: sobrenome,
    idade: idade,
  };
}

const pessoa01 = criarPessoa("Guilherme", "Marinho", 21);
const pessoa02 = criarPessoa("Marcella", "Fogaça", 21);
console.log(pessoa01.nome);
console.log(pessoa02.nome);
