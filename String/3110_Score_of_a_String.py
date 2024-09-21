class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(len(s)-1):
            diff = ord(s[i]) - ord(s[i+1])
            score += abs(diff)
        return score

res = Solution()
print(res.scoreOfString("hello"))