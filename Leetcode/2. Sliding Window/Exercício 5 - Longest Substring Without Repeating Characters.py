# abcabcbb

# Resposta:
# 3


def lengthOfLongestSubstring(s):
    l = 0
    ans = 0
    counter = {}

    for r in range(len(s)):
        counter[s[r]] = counter.get(s[r], 0) + 1

        while counter[s[r]] > 1:
            counter[s[r]] -= 1
            l += 1

        ans = max(ans, r - l + 1)


    return ans


print(lengthOfLongestSubstring("abcabcbb"))