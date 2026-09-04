frase = "A man a plan a canal Panama"
# true

def validPalindrome(str):
    left, right = 0, len(str) - 1

    while left < right:
        if str[left] == str[right]:
            return True

        left += 1
        right -= 1

    return False


print(validPalindrome(frase))