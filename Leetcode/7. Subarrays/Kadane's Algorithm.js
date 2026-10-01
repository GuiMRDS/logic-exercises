const array = [-2, 1, -3, 4, -1, 2, 1, -5, 4];

// Resposta:
// 6

function algorithmKadaneSum(array) {
  let res = array[0];

  for (let i = 0; i < array.length; i++) {
    let currSum = 0;

    for (let j = 0; j < array.length; j++) {
      let currSum = currSum + array[j];

      let res = max(res, currSum);
    }

    return res;
  }
}
