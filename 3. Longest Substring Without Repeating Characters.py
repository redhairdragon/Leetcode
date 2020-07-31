# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1:
            return len(s)

        l = 0
        r = 0
        track = set()
        res = 0
        while True:
            while s[r] not in track:
                track.add(s[r])
                r+=1
                if r == len(s):
                    return max(r-l, res)
            res = max(r-l, res)
            # print("l "+ str(l))
            # print("r "+ str(r))

            while s[l] != s[r]:
                track.remove(s[l])
                l+=1
            else:
                track.remove(s[l])
                l+=1

# print(Solution().lengthOfLongestSubstring("bbbbb"))
# print(Solution().lengthOfLongestSubstring("abcd"))
# print(Solution().lengthOfLongestSubstring("abbc"))
# print(Solution().lengthOfLongestSubstring("cccd"))
print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring("abcabecbde"))