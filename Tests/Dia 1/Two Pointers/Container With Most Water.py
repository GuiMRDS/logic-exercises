height = [1,8,6,2,5,4,8,3,7]
base = 5

def maiorArea(height, base):
    if not height:
        return 0

    left = 0

    for right in range(len(height)):
        if height[right] > height[left]:
            left += 1
            height[left] = height[right]


    area = base * height[left]
    return area


print(maiorArea(height, base))