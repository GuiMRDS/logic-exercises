try {
  console.log("Abri um arquivo");
  console.log("Manipulei o arquivo e gerou erro");
  console.log("Fechei o arquivo");
} catch (error) {
  console.log("Tratando Erro");
} finally {
  console.log("'finally' Eu sempre sou executado");
}
