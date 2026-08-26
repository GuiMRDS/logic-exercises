frase = "A man a plan a canal Panama"
# true

def validPalindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] == s[right]:
            return True

        left += 1
        right -= 1

    return False


print(validPalindrome(frase))