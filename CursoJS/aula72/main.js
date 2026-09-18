// defineProprty -> Getter e Setters
function Produto(nome, preco, estoque) {
  this.nome = nome;
  this.preco = preco;

  Object.defineProperty(this, "estoque", {
    enumerable: true, // mostrar chave
    value: estoque, // valor
    writable: true, // poder alterar
    configurable: true, // configurável
  });
}

const p1 = new Produto("Camiseta", 20, 3);
console.log(p1);
