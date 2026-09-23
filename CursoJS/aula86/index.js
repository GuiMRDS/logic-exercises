function rand(min, max) {
  min *= 1000;
  max *= 1000;
  return Math.floor(Math.random() * (max - min) + min);
}

function esperaAI(msg, tempo) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve(msg);
    }, tempo);
  });
}

esperaAI("Conexão com o BD", rand(1, 3))
  .then((resposta) => {
    console.log(resposta);
    return esperaAI("Buscando dados de BASE.", rand(1, 3));
  })
  .then((resposta) => {
    console.log(resposta);
    return esperaAI("Tratamento dos dados da BASE.", rand(1, 3));
  })
  .then((resposta) => {
    console.log(resposta);
  })
  .then(() => {
    console.log("Exibe dados da tela.");
  })
  .catch();

console.log("Isso aqui está exibido antes de qualquer promisse");
