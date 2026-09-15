nums = [0, 3, 2, 4];
target = 6;

// Resposta:
// [2,3]

function TwoPointerBruteForce(nums, target) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] == target) {
        return [i, j];
      }
    }
  }
}

console.log(TwoPointerBruteForce(nums, target));
