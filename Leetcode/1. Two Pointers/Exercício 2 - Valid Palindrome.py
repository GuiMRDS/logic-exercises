frase = "A man a plan a canal Panama"
# true

def isPalindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] == s[right]:
            return True

        left += 1
        right -= 1

    return False


print(isPalindrome(frase))