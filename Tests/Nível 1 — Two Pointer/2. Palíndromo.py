# Entrada: "racecar"
# Saída: true

# Entrada: "hello"
# Saída: false


def TwoPointer(pal):
    left = 0
    right = len(pal) - 1

    while left < right:
        if pal[left] == pal[right]:
            return True

        left += 1
        right -= 1

    return False


print(TwoPointer('racecar'))
print(TwoPointer('hello'))