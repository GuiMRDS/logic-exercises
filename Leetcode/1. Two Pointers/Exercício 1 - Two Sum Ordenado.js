nums = [0, 3, 2, 4];
target = 6;

// Resposta:
// [2,3]

function TwoPointerBruteForce(nums, target) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] == target) return [i, j];
    }
  }
}

function TwoPointer(nums, target) {
  let left = 0;
  let right = length.nums - 1;

  while (left < right) {
    let sum = nums[left] + nums[right];

    if (sum == target) {
      return [nums[left], nums[right]];
    }

    if (right < target) {
      right--;
    } else {
      left++;
    }
  }
}

console.log(TwoPointerBruteForce(nums, target));
console.log(TwoPointer(nums, target));
