// abcabcbb

// Resposta:
// 3

function lengthOfLongestSubstring(string) {
  let left = 0;
  let ans = 0;
  let counter = {};

  for (let right = 0; right < string.length; right++) {
    counter[string[right]] = counter.get(string[right], 0) + 1;

    while (counter[string[right]] > 1) {
      counter[string[right]] -= 1;
      left += 1;
    }
  }
}
