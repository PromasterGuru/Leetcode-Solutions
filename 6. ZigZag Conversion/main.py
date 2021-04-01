class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        row = 0
        step = 1
        arr = [""]*numRows
        for i in range(len(s)):
            arr[row] += s[i]
            if row == 0:
                step = 1
            elif(row == numRows  - 1):
                step = -1
            row += step
        return "".join(arr)
            

if __name__ == "__main__":
    sol = Solution()
    s = "PAYPALISHIRING"
    print(sol.convert(s, 3))
    
