const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

console.log("_________ MAIOR NUMERO _________");

rl.question("Digite o primeiro numero: ", function (numero1) {
  rl.question("Digite o segundo numero: ", function (numero2) {
    rl.question("Digite o terceiro numero: ", function (numero3) {
      numero1 = Number(numero1);
      numero2 = Number(numero2);
      numero3 = Number(numero3);

      if (numero1 > numero2 && numero1 > numero3) {
        console.log("Primeiro numero é maior");
      } else if (numero2 > numero1 && numero2 > numero3) {
        console.log("Segundo numero é maior");
      } else {
        console.log("Terceiro numero é maior");
      }

      rl.close();
    });
  });
});
