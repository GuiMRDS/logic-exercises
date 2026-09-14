nums = [1, 3, 5, 7, 9];
target = 7;

// Resposta:
// 3

function BinarySeach(nums, target) {
  let left = 0;
  let right = nums.length;

  while (left < right) {
    let mid = (left + right) / 2;

    if (nums[mid] == target) {
      return mid;
    }

    if (nums[mid] < target) {
      left++;
    } else {
      right++;
    }
  }
}

console.log(BinarySeach(nums, target));
