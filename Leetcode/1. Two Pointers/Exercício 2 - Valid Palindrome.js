frase = "A man a plan a canal Panama";
// True
frase1 = "lorem canal Panama";
// False

function isValidPalidrome(string) {
  let left = 0;
  let right = string.length - 1;

  while (left < right) {
    if (string[left] == string[right]) return true;

    left++;
    right--;
  }

  return false;
}

console.log(isValidPalidrome(frase));
console.log(isValidPalidrome(frase1));
