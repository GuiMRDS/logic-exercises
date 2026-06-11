const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

console.log("_________ Tabuada _________");

rl.question("Digite o primeiro numero: ", function (numero) {
  for (let i = 0; i < 11; i++) {
    console.log(" 5 X " + i + " = " + numero * i);
  }
  return numero;
});
