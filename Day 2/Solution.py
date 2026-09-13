class Solution:
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
num = [1, 2, 3, 1]
result = Solution().containsDuplicate(num)
print(result)

