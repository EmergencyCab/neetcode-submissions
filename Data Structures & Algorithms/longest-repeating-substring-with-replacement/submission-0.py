class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0 
        maxFreq = 0
        longest = 0 
        count = {}

        for end in range(len(s)):
            # add a new char to window 
            count[s[end]]= count.get(s[end],0) + 1

            #update the frequency 
            maxFreq = max(maxFreq, count[s[end]])

            #if window is invalid shrink from left 
            while (end - start + 1) - maxFreq > k:
                count[s[start]] -= 1 
                start += 1

            #update the longest 
            longest = max(longest, end - start + 1)

        return longest
        
                

