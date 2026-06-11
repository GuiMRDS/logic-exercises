const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

console.log("_________ Digite 10 numeros _________");
const numeros = [];

function perguntarNumero(i) {
    if (i >= 10) {
        console.log("Numeros digitados: ");
        console.log(numeros);
        rl.close();
        return;
    }

    rl.question("Digite numero: ", function(numero) {
        numeros.push(Number(numero));
        perguntarNumero(i + 1);
    });
}

perguntarNumero(0);