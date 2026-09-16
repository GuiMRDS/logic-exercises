// [1,2,3,1]
// true

function HashSet(array) {
  let visto = new Set();

  for (let i = 0; i < array.length; i++) {
    if (visto in array) {
      return true;
    }

    visto.add(i);
  }

  return false;
}

console.log(HashSet([1, 2, 3, 1]));
console.log(HashSet([1, 2, 3, 4]));
