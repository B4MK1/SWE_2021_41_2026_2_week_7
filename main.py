from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    s = {}  
    for i, n in enumerate(nums):
        comp = target - n
        if comp in s:
            return [s[comp], i]
        s[n] = i
    return[]