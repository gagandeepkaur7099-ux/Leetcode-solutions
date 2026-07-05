class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False

        original = x
        reverse = 0

        while x > 0:
            digit = x % 10
            reverse = reverse * 10 + digit
            x //= 10

        return original == reverse


# Example
number = 121

solution = Solution()
print(solution.isPalindrome(number))
