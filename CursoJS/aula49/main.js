// Decalração de função (função hoisting)
falaOi();
function falaOi(params) {
  console.log("Oi");
}

// First-class object (Objetos de primeria classe)
// Function expression
const souUmDado = function () {
  console.log("Sou um dados.");
};
souUmDado();

function executaFuncao(funcao) {
  console.log("Vou executar sua função abaixo");
  funcao();
}
executaFuncao(souUmDado);

// Arrow function
const funcaoArray = () => {
  console.log("Sou uma arroy function");
};
funcaoArray();

// Dentro de um objeto
const obj = {
  falar: function () {
    console.log("Estou falando...");
  },
};
obj.falar();
