frase = "A man a plan a canal Panama"
# true

def TwoPointer(string):
    left = 0
    right = len(string)-1

    while left < right:
        if string[left] == string[right]:
            return True

        left += 1
        right -= 1

    return False


print(TwoPointer(frase))