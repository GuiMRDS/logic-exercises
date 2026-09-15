function bubleSort(nums) {
  for (let i; i < nums.length; i++) {
    for (let j; j < nums.length - i - 1; j++) {
      if (nums[i] < nums[j + 1]) {
        (nums[j], (nums[j + 1] = nums[j + 1]), nums[j]);
      }
    }
  }

  return nums;
}

console.log(bubleSort([5, 4, 3, 2, 1]));
