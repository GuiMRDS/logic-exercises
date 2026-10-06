// Regras:
// Menor que R$100 → sem comissão
// Entre R$100 e R$499,99 → 1%
// A partir de R$500 → 5%

// Exibir:
// João - Venda: 1000 - Comissão: 50
// Maria - Venda: 300 - Comissão: 3
// João - Venda: 80 - Comissão: 0

// Desafio extra
// Mostrar a comissão total por vendedor.

import dados from "./dados.json" with { type: "json" };

for (let i = 0; i < dados.vendas.length; i++) {
  const vendedor = dados.vendas[i].vendedor;
  const valor = dados.vendas[i].valor;
  let comissao = 0;

  if (valor >= 500) {
    comissao = valor * 0.05;
  } else if (valor < 500 && valor > 100) {
    comissao = valor * 0.01;
  } else {
    comissao = 0;
  }

  console.log(`${vendedor} - Venda: ${valor} - Comissão: ${comissao}`);
}
