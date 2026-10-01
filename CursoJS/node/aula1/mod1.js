class Pessoa {
  constructor(nome) {
    this.nome = nome;
  }
}

const nome = "Guilherme";
const sobrenome = "Marinho";

module.exports = {
  nome,
  sobrenome,
  Pessoa,
};

exports.nome = nome;
module.exports.sobrenome = sobrenome;
exports.OutraCoisa = "Outra Coisa";
