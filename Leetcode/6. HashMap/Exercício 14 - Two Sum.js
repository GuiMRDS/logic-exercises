const nums = [2, 7, 11, 15];
let target = 9;

// Resposta:
// [0,1]

function twoSumHash(nums, target) {
  hashMap = {};

  for (let i = 0; i < nums.length; i++) {
    hashMap[nums[i]] = i;

    for (let j = 0; j < nums.length; j++) {
      if (nums[j] in hashMap) {
        return hashMap[nums[j]];
      }
    }

    return false;
  }
}

console.log(twoSumHash(nums, target));
