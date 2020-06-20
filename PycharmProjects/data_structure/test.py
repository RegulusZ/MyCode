class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lengh = len(s)
        if lengh == 0:
            return 0

        ans = 1
        head = 0
        tail = 0

        while tail < lengh-1:
            cur = s[head:tail+1]
            temp = s[tail + 1]
            if temp not in cur:
                tail += 1
                if len(cur) >= ans:
                    ans += 1
            elif temp in cur:
                head += 1

        return ans


if __name__ == "__main__":
    test = "abcabcbb"
    a = Solution()
    print(a.lengthOfLongestSubstring(test))