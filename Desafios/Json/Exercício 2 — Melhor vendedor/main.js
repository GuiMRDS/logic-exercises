// Calcule o total vendido por cada vendedor.

// Exibir:
// João: R$ 1080
// Maria: R$ 300

// E informar:
// Melhor vendedor: João

import dados from "./dados.json" with { type: "json" };

for (let i = 0; i < dados.vendas.length; i++) {

  if (dados.vendas[i] > dados.vendas[i+1]) {
    return dados.vendas[i].vendedor
  }
}
