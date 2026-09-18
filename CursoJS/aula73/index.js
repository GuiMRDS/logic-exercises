const produto = { nome: "Produto", preco: 1.8 };
const canetaAzul = {
  ...produto,
  material: "porcelana",
};

const caneca = Object.assign({}, produto, { meterial: "porcelana" });

console.log(caneca);
console.log(canetaAzul);
