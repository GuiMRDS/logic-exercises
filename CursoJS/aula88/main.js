function rand(min, max) {
  min *= 1000;
  max *= 1000;
  return Math.floor(Math.random() * (max - min) + min);
}

function esperaAI(msg, tempo) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (typeof msg !== "string") {
        reject("CAI NO ERRO");
        return;
      }

      resolve(msg.toUpperCase() + " - Passei na promise");
      return;
    }, tempo);
  });
}

/*
esperaAI("FASE 1", rand())
  .then((valor) => {
    console.log(valor);
    return esperaAI("FASE 2", rand());
  })
  .then((fase) => {
    console.log(fase);
    return esperaAI("FASE 3", rand());
  })
  .then((fase) => {
    console.log(fase);
    return fase;
  })
  .then((fase) => {
    console.log("Terminamos na fase", fase);
  })
  .catch((e) => console.log(e));
*/

async function executa(params) {
  try {
    const fase1 = await esperaAI("FASE 1", rand());
    console.log(fase1);
    const fase2 = await esperaAI("FASE 2", rand());
    console.log(fase2);
    const fase3 = await esperaAI("FASE 3", rand());
    console.log(fase3);

    console.log("Terminamos na fase", fase3);
  } catch (e) {
    console.log(e);
  }
}

executa();
