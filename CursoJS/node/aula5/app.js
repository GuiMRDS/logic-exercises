const path = require("path");
const caminhoArquivo = path.resolve(__dirname, "teste.json");
const escreve = require("./modules/escrever.js");
const ler = require("./modules/ler.js");

// const pessoas = [
//   { nome: "Guilherme" },
//   { nome: "Bruno" },
//   { nome: "Augusto" },
//   { nome: "André" },
// ];
// const json = JSON.stringify(pessoas, "", 2);
// escreve(caminhoArquivo, json);

async function lerArquivo(caminho) {
  const dados = await ler(caminho);
  renderizaDados(dados);
}

function renderizaDados(dados) {
  dados = JSON.parse(dados);
  dados.forEach((val = console.log(val.nome)));
}
lerArquivo(caminhoArquivo);
