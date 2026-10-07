# Two Sum HashMap

def TwoSum(nums: List[int], target: int) -> List[int]:
    hasher = {}

    for idx, i in enumerate(nums):
        if hasher.get(i) is not None:
            return [hasher.get(i), idx]

        hasher[target-i] = idx



TwoSum([2,7,11,15], 9)