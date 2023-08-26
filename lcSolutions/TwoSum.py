class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a map
        # enumerate each value in nums for the index and value at the same time
        # create a temp variable that calculates the difference from the current value and the target
        # if that difference is in the map you can return
        # otherwise add the value to the map and mvoe on

        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return