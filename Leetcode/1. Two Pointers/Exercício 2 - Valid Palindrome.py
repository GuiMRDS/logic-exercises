frase = "A man a plan a canal Panama"
# true
frase1 = "lorem canal Panama";
# false

def isPalindrome(s):
    left = 0
    right = len(s) - 1

    while(left < right):
        if s[left] == s[right]:
            return True

        left = left + 1
        right = right - 1

    return False


print(isPalindrome(frase))
print(isPalindrome(frase1))
