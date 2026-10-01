// [1,2,3,1]
// true

function HashSet(array) {
  let visto = new Set();

  for (const num of array) {
    if (visto.has(num)) {
      return true;
    }

    visto.add(num);
  }
  
  return false;
}

console.log(HashSet([1, 2, 3, 1]));
console.log(HashSet([1, 2, 3, 4]));
