frase = "A man a plan a canal Panama";
frase1 = "lorem canal Panama";
// True

function isValidPalidrome(frase) {
  let left = 0;
  let right = frase.length - 1;

  while (left < right) {
    if (frase[left] == frase[right]) return true;

    left++;
    right--;
  }

  return false;
}

console.log(isValidPalidrome(frase));
console.log(isValidPalidrome(frase1));
