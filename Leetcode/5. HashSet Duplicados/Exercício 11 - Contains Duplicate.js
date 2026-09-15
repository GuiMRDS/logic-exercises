// [1,2,3,1]
// true

function HashSet(nums) {
  let visto = new Set();

  for (num of nums) {
    if (num in visto) {
      return true;
    }

    visto.add(num);
  }

  return false;
}

console.log(HashSet([1, 2, 3, 1]));
