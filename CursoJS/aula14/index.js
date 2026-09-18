function saudacao(nome) {
  return `Bom dia ${nome}!`;
}

const variavel = saudacao("Guilherme");
console.log(variavel);

function soma(x, y) {
  const resultado = x + y;
  return resultado;
}

const resultado = soma(2, 2);
console.log(resultado);

const raiz = (n) => n ** 0.5;

console.log(raiz(9));
