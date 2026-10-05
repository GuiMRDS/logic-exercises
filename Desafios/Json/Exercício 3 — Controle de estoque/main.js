// {
//   id: 1,
//   descricao: "Venda",
//   codigoProduto: 101,
//   quantidade: 20,
//   tipo: "saida"
// }

// Produto: Caneta
// Estoque anterior: 150
// Estoque final: 130

import dados from "./dados.json" with { type: "json" };

const movimentacao = {
  id: 1,
  descricao: dados.estoque[0].descricaoProduto,
  codigoProduto: dados.estoque[0].codigoProduto,
  quantidade: dados.estoque[0].estoque,
  tipo: "saida",
};

if (dados.estoque.codigoProduto === movimentacao.codigoProduto) {
  if (movimentacao.tipo === "entrada") {
    dados.estoque[0].estoque = -1;
  } else {
    dados.estoque[0].estoque = +1;
  }
}

console.log(movimentacao);
