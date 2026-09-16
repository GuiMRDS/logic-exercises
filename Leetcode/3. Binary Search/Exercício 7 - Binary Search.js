nums = [1, 3, 5, 7, 9];
target = 7;

// Resposta:
// 3

function BinarySeach(nums, target) {
  let left = 0;
  let right = nums.length - 1;

  while (left < right) {
    let mid = (left + right) / 2;

    if (mid == target) return [mid];

    if (mid > target) {
      mid++;
    } else {
      mid--;
    }
  }
}

console.log(BinarySeach(nums, target));
