function bubbleSort(nums) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] > nums[j])
        return (nums[j], (nums[j + 1] = nums[j + 1]), nums[j]);
    }
  }
}

console.log(bubbleSort([9, 8, 7, 6, 5, 4, 3, 2, 1]));
