class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num = x
        res = 0
        while num > 0:
            res = res * 10 + num%10
            num = num//10
        return x == res
        

if __name__ == "__main__":
    sol = Solution()
    n = 121
    print(sol.isPalindrome(n))