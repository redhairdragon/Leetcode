# https://leetcode.com/problems/permutation-in-string/
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        def allzero(l):
            for i in l:
                if i !=0:
                    return False
            return True

        track = {}
        for char in s1:
            if char in track:
                track[char] += 1
            else:
                track[char] = 1


        for i in range(0,len(s1)):
            if s2[i] in track:
                track[s2[i]] -= 1
        if allzero(track.values()):
                return True

        for i in range(len(s1),len(s2)):
            if s2[i-len(s1)] in track:
                track[s2[i-len(s1)]] += 1

            if s2[i] in track:
                track[s2[i]] -= 1

            if allzero(track.values()):
                return True
        return False
            


print(Solution().checkInclusion("ab","eidoooba"))
print(Solution().checkInclusion("ab","eidoooab"))
print(Solution().checkInclusion("ab","abdooo"))
print(Solution().checkInclusion("abbb","abdooabbbo"))
print(Solution().checkInclusion("ab","eidboaoo"))