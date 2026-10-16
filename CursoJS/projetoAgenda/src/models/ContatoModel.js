const mongoose = require("mongoose");
const validator = require("validator");

const ContatoSchema = new mongoose.Schema({
  nome: { type: String, required: true },
  sobrenome: { type: String, required: false, default: "" },
  email: { type: String, required: false, default: "" },
  telefone: { type: String, required: false, default: "" },
  criadoEm: { type: Date, default: Date.now },
});

const ContatoModel = mongoose.model("Contato", ContatoSchema);

function Contato(body) {
  this.body = body;
  this.errors = [];
  this.contato = null;
}

Contato.prototype.register = async function () {
  this.valida();

  if (this.errors.length > 0) return;
  this.contato = await ContatoModel.create(this.body);
};

Contato.prototype.valida = function () {
  this.cleanUp();

  if (this.body.email && !validator.isEmail(this.body.email))
    this.errors.push("E-mail inválido.");
  if (!this.body.nome) this.errors.push("O nome é um campo obrigatório.");
  if (!this.body.email && !this.body.telefone) {
    this.errors.push(
      "Pelo menos um contato precisa ser enviado: e-mail ou telefone",
    );
  }
};

Contato.prototype.cleanUp = function () {
  const campos = ["nome", "sobrenome", "email", "telefone"];
  const dados = {};

  for (const campo of campos) {
    dados[campo] =
      typeof this.body[campo] === "string" ? this.body[campo].trim() : "";
  }

  this.body = dados;
};

Contato.prototype.edit = async function (id) {
  if (typeof id !== "string") return;
  this.valida();
  if (this.errors.length > 0) return;
  this.contato = await ContatoModel.findByIdAndUpdate(id, this.body, {
    new: true,
  });
};

Contato.buscaPorId = async function (id) {
  if (typeof id !== "string") return;
  const contato = await ContatoModel.findById(id);
  return contato;
};

Contato.buscaContatos = async function () {
  const contatos = await ContatoModel.find().sort({ criandoEm: -1 });
  return contatos;
};

Contato.delete = async function (id) {
  if (typeof id !== "string") return;
  const contato = await ContatoModel.findOneAndDelete({ _id: id });
  return contato;
};

module.exports = Contato;
