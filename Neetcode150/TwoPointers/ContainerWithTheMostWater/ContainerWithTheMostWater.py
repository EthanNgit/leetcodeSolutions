class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxHeight = 0

        while l < r:
            area = min(height[l], height[r]) * (r - l)
            maxHeight = max(maxHeight, area)

            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                l += 1
                r -= 1
        
        return maxHeight