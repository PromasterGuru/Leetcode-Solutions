class Solution:
    def intToRoman(self, num: int) -> str:
        convertor = [
            ["","M", "MM", "MMM"],
            ["","C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
            ["","X", "XX", "XXX", "XL", "L", "LX","LXX","LXXX", "XC"],
            ["","I","II","III","IV","V","VI","VII","VIII","IX"]
        ]
        return convertor[0][num//1000] + convertor[1][(num//100)%10] + convertor[2][(num//10)%10] + convertor[3][num%10]

if __name__ == "__main__":
   sol = Solution()
   num = 58
   print(sol.intToRoman(num))
