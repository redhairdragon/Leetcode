# https://leetcode.com/problems/minimum-window-substring/
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        track = {}
        for i in t:
            if i in track:
                track[i] += 1
            else:
                track[i] = 1
        letter_collected = len(track)

        
        left = 0 
        right = 0

        best_left = -1
        best_right = -1
        best_size = len(S)+2


        while True:
            while letter_collected != 0 and right < len(S):
                if S[right] in track:
                    track[S[right]] -= 1
                    if track[S[right]] == 0:
                        letter_collected -= 1
                        if letter_collected == 0:
                            break
                right += 1

            while letter_collected == 0:
                if right - left < best_size:
                    best_left = left
                    best_right = right
                left += 1
                if S[left] in track:
                    track[S[left]] += 1
                    if track[S[right]] == 1:
                        letter_collected += 1
        
        if best_left == -1:
            return ""
        return S[best_left:best_right]


                
            
print(Solution().minWindow("ADOBECODEBANC","ABC"))