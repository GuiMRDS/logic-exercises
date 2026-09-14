frase = "A man a plan a canal Panama"
# true

def isPalindrome(frase):
    left = 0
    right = len(frase) - 1

    while left < right:
        if frase[left] == frase[right]:
            return True

        left = left + 1
        right = right - 1

    return False


print(isPalindrome(frase))