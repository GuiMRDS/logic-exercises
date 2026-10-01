frase = "A man a plan a canal Panama";
// True
frase1 = "lorem canal Panama";
// False

function isValidPalidrome(s) {
  let left = 0;
  let right = s.length - 1;

  while (left < right) {
    if (s[left] == s[right]) return true;
    left++;
    right--;
  }

  return false;
}

console.log(isValidPalidrome(frase));
console.log(isValidPalidrome(frase1));
