class Solution:
    def expandFromMiddle(self, s:str, l:int, r:int):
        while (l >= 0 and r < len(s) and s[l] == s[r]):
            l -= 1
            r += 1
        return (r - l - 1)
        
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 1: return 0
        start = 0
        end = 0
        for i in range(len(s)):
            l1 = self.expandFromMiddle(s, i, i)
            l2 = self.expandFromMiddle(s, i, i+1)
            ls = max(l1,l2)
            if ls > end - start:
                start = i - ((ls - 1)//2)
                end = i + (ls//2)
        return s[start: end+1]

if __name__ == "__main__":
    sol = Solution()
    s = "babab"
    s = "cbbd"
    # s = 'bb'
    # s = "babc"
    # s = "aca"
    # s = "defggbac"
    # s = 'a'
    s = "babad"
    # s = "ccc"
    s = "abb"
    # s = "reifadyqgztixemwswtccodfnchcovrmiooffbbijkecuvlvukecutasfxqcqygltrogrdxlrslbnzktlanycgtniprjlospzhhgdrqcwlukbpsrumxguskubokxcmswjnssbkutdhppsdckuckcbwbxpmcmdicfjxaanoxndlfpqwneytatcbyjmimyawevmgirunvmdvxwdjbiqszwhfhjmrpexfwrbzkipxfowcbqjckaotmmgkrbjvhihgwuszdrdiijkgjoljjdubcbowvxslctleblfmdzmvdkqdxtiylabrwaccikkpnpsgcotxoggdydqnuogmxttcycjorzrtwtcchxrbbknfmxnonbhgbjjypqhbftceduxgrnaswtbytrhuiqnxkivevhprcvhggugrmmxolvfzwadlnzdwbtqbaveoongezoymdrhywxcxvggsewsxckucmncbrljskgsgtehortuvbtrsfisyewchxlmxqccoplhlzwutoqoctgfnrzhqctxaqacmirrqdwsbdpqttmyrmxxawgtjzqjgffqwlxqxwxrkgtzqkgdulbxmfcvxcwoswystiyittdjaqvaijwscqobqlhskhvoktksvmguzfankdigqlegrxxqpoitdtykfltohnzrcgmlnhddcfmawiriiiblwrttveedkxzzagdzpwvriuctvtrvdpqzcdnrkgcnpwjlraaaaskgguxzljktqvzzmruqqslutiipladbcxdwxhmvevsjrdkhdpxcyjkidkoznuagshnvccnkyeflpyjzlcbmhbytxnfzcrnmkyknbmtzwtaceajmnuyjblmdlbjdjxctvqcoqkbaszvrqvjgzdqpvmucerumskjrwhywjkwgligkectzboqbanrsvynxscpxqxtqhthdytfvhzjdcxgckvgfbldsfzxqdozxicrwqyprgnadfxsionkzzegmeynye"
    print(sol.longestPalindrome(s))
