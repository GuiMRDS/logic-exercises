# "A man a plan a canal Panama"
#
# true


def Palindrome(str):
    left = 0
    right = len(str)-1

    while left < right:
        if str[left] == str[right]:
            return True

        left += 1
        right -= 1

    return False



print(Palindrome('A man a plan a canal Panama'))