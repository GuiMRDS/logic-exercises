function rand(min, max) {
  min *= 1000;
  max *= 1000;
  return Math.floor(Math.random() * (max - min) + min);
}

function esperaAI(msg, tempo) {
  return new Promise((resolve, reject) => {
    if (typeof msg !== "string") return reject;

    setTimeout(() => {
      resolve(msg.toUpperCase() + " - Passei na promise");
      return;
    }, tempo);
  });
}

const promisse = [
  esperaAI("Promise 1", 3000),
  esperaAI("Promise 2", 5000),
  esperaAI("Promise 3", 1000),
];

Promise.all(promisse)
  .then(function (valor) {
    console.log(valor);
  })
  .catch(function (erro) {
    console.log(erro);
  });
