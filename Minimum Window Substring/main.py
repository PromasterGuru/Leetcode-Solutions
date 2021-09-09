class Solution:
    def minWindow(self, s: str, t: str) -> str:
        len_s = len(s)
        len_t = len(t)
        hash_s = [0] * (ord('z')+1)
        hash_t = [0] * (ord('z')+1)
        count, start, start_index, min_length = 0, 0, -1, float('inf')
        if len_t > len_s:
            return ""
        for j in t:
            hash_t[ord(j)] += 1
        for i in range(len_s):
            hash_s[ord(s[i])] += 1
            if(hash_s[ord(s[i])] <= hash_t[ord(s[i])]):
                count += 1
            if count == len_t:
                while(hash_s[ord(s[start])] > hash_t[ord(s[start])] or hash_t[ord(s[start])] == 0):
                    if(hash_s[ord(s[start])] > hash_t[ord(s[start])]):
                        hash_s[ord(s[start])] -= 1
                    start += 1
                window_len = i - start + 1
                if(window_len < min_length):
                    min_length = window_len
                    start_index = start
        if(start_index == -1):
            return ""
        return s[start_index: start_index + min_length]

if __name__ == "__main__":
    sol = Solution()
    s = "aaaaaaaaaaaabbbbbcdd"
    t = "abcdd"
    ans = "abbbbbcdd"
    s = "aa"
    t = "aa"
    s = "a"
    t = "a"
    s = "bba"
    t = "ba"
    f = open("s.txt", "r")
    f2 = open("t.txt", "r")
    s = f.read()
    t = f2.read()
    # print(len(s), len(t))
    print(sol.minWindow(s,t))