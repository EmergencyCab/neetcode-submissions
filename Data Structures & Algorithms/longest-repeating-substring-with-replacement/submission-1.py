class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0 
        maxFreq = 0 
        count = {}
        longest = 0 

        #go through the list to find the character counts 
        for end in range(len(s)):
            count[s[end]] = count.get(s[end],0) + 1

            #after the char is added, update the frequency 
            maxFreq = max(maxFreq, count[s[end]])

            #Now check if there are valid replacement needed 
            #size of the window - frequency > k 
            while (end-start+1) - maxFreq > k:
                #if size if good we move start 
                count[s[start]] -= 1 #remove the leftmost char
                start += 1 #shrink size of window

            longest = max(longest, end-start + 1)
        
        return longest 
        
                

