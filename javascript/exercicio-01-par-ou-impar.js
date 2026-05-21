const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

console.log("_________ PAR OU IMPAR _________");
rl.question("Digite seu numero: ", function (numero) {
  if (numero % 2 === 0) {
    console.log("PAR");
  } else {
    console.log("IMPAR");
  }

  rl.close();
});
