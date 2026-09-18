function funcao(params) {
  let total = 0;
  for (let argument of arguments) {
    total += argument;
  }

  console.log(total);
}

funcao(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
