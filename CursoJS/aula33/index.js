const pessoa = {
  nome: "Guilherme",
  sobrenome: "Marinho",
  idade: 21,
  endereco: {
    rua: "Av Brasil",
    numero: 320,
  },
};

const {
  endereco: { rua, numero },
  endereco,
} = pessoa;
console.log(nome, sobrenome);
