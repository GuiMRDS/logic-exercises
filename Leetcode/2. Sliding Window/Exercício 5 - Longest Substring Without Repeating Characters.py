# abcabcbb
import collections


# Resposta:
# 3


def lengthOfLongestSubstring(string):
    left = 0
    ans = 0
    counter = {}

    for right in range(len(string)):
        counter[string[right]] = counter.get(string[right], 0) + 1

        while counter[string[right]] > 1:
            counter[string[right]] -= 1
            left += 1

        ans = max(ans, right - left + 1)

    return ans



print(lengthOfLongestSubstring("abcabcbb"))