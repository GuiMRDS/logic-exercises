frase = "A man a plan a canal Panama"
# true

def validPalindrome(frase):
    left = 0
    right = len(frase)-1

    while left < right:
        if frase[left] == frase[right]:
            return True

        left += 1
        right -= 1

    return False


print(validPalindrome(frase))