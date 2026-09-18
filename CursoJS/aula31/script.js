const verdadeira = true;

// Let tem escopo de bloco { ...bloco }
// Var só tem escopo de função

let nome = "Guilherme";
var nome2 = "Guilherme";

if (verdadeira) {
  let nome2 = "Marinho";
  // console.log(nome, nome2);

  if (verdadeira) {
    // let nome = "Outra coisa";
    console.log(nome, nome2);
  }
}

function falaOi(params) {
  let nome = "Gui";
  console.log(nome);
}

falaOi();
