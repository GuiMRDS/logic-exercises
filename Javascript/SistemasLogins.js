const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

console.log("----------- Sistema de Login ----------- ");

const loginCorreto = "Gui";
const senhaCorreta = 12345;

function perguntarLoginSenha() {
    rl.question("Login: ", function (answer) {
        rl.question("Senha: ", function (password) {
            login = String(answer);
            senha = Number(password);


                if (login === loginCorreto && senha === senhaCorreta) {
                    console.log("Acesso permitido");
                    rl.close();
                }
                else {
                    console.log("Acesso negado, usuario ou senha errada");
                    perguntarLoginSenha();
                }

        });
    });
}

perguntarLoginSenha();