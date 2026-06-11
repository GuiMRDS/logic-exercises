const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

console.log("_________ NUMEROS POSITIVOS _________");

let array = [];
let contador = 0;

function perguntarNumero() {
  rl.question("Digite um numero: ", function (numero) {
    numero = Number(numero);

    array.push(numero);

    contador++;

    if (contador < 3) {
      perguntarNumero();
    } else {
      console.log("Array:", array);

      rl.close();
    }
  });
}

perguntarNumero();
