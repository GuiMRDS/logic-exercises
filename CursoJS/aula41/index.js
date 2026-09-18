function MaiorNumero(x, y) {
  return x > y ? x : y;
}

const MaiorNumero2 = (x, y) => (x > y ? x : y);

console.log(MaiorNumero(20, 5));
console.log(MaiorNumero2(20, 50));

// function ePaisagem(lagura, altura) {
//  return lagura >= altura;
// }

const ePaisagem = (lagura, altura) => lagura > altura;

console.log(ePaisagem(1920, 1080));
console.log(ePaisagem(1080, 1920));

function FizzBuzz(numero) {
  if (typeof numero !== Number) return numero;
  if (numero % 3 == 0 && numero % 5 == 0) return "FizzBuzz";
  if (numero % 3 == 0) return "Fizz";
  if (numero % 5 == 0) return "Buzz";
  return numero;
}

for (let i = 0; i <= 100; i++) {
  console.log(i, FizzBuzz(i));
}
