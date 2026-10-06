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
  descricao: "Venda",
  codigoProduto: 101,
  quantidade: 20,
  tipo: "saida",
};

let estoqueAnterior = dados.estoque[0].estoque;
let estoqueFinal = dados.estoque[0].estoque;

if (movimentacao.codigoProduto == dados.estoque[0].codigoProduto) {
  if (movimentacao.tipo == "saida") {
    estoqueFinal = estoqueAnterior - movimentacao.quantidade;
  } else {
    estoqueFinal = estoqueAnterior + movimentacao.quantidade;
  }
}

console.log(`
  Produto: ${dados.estoque[0].descricaoProduto}
  Estoque anterior: ${estoqueAnterior}
  Estoque final: ${estoqueFinal}
  `);
