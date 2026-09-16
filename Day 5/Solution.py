class Solution:
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]
num = 121
result = Solution().isPalindrome(num)
print(result)