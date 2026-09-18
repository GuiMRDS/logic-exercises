const data = new Date();
const diaSemana = data.getDay();
const diaSemandaTexto = getDiaSemanaTexto(diaSemana);

function getDiaSemanaTexto(diaSemana) {
  let diaSemandaTexto;

  switch (diaSemana) {
    case 0:
      diaSemandaTexto = "Domingo";
      return diaSemandaTexto;

    case 1:
      diaSemandaTexto = "Segunda";
      return diaSemandaTexto;

    case 2:
      diaSemandaTexto = "Terça";
      return diaSemandaTexto;

    case 3:
      diaSemandaTexto = "Quarta";
      return diaSemandaTexto;

    case 4:
      diaSemandaTexto = "Quinta";
      return diaSemandaTexto;

    case 5:
      diaSemandaTexto = "Sexta";
      return diaSemandaTexto;

    case 6:
      diaSemandaTexto = "Sábado";
      return diaSemandaTexto;

    default:
      diaSemandaTexto = "";
      return diaSemandaTexto;
  }
}

console.log(diaSemandaTexto);
