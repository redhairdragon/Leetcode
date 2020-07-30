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

        # print(track)
        left = 0 
        right = 0

        best_left = -1
        best_right = -1
        best_size = len(s)+2


        while True:
            while right < len(s):
                # print("s right: "+ s[right])
                if s[right] in track: 
                    track[s[right]] -= 1
                    if track[s[right]] == 0:
                        letter_collected -= 1
                        # print(letter_collected)
                        # print(track)
                        # print(s[right])
                        if letter_collected == 0:
                            right += 1
                            break
                right += 1
                
                
            # print("finish moving right ")

            while left<right and letter_collected == 0:
                # print("left moved")
                # print("s left: "+ s[left])

                if right - left < best_size:
                    best_left = left
                    best_right = right
                    best_size = right-left
                    # print("update best")
                    # print(best_left)
                    # print(best_right)
                    # print(s[best_left:best_right])

                if s[left] in track:
                    track[s[left]] += 1
                    # print(letter_collected)
                    # print(track)
                    if track[s[left]] == 1:
                        letter_collected += 1
                        left += 1
                        break;
                left += 1
            # print("finish moving left ")

            if right == len(s):
                break
            
        if best_left == -1:
            return ""
        return s[best_left:best_right]


                
            
print(Solution().minWindow("ADOBECODEBANC","CD"))