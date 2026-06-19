class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        longest = 0
        charSet = set()

        #iterate through the list s
        for end in range(len(s)):
            #if the end character is already there we remove the start 
            #and take it to another index. 
            #E.G: abca --> end "a" at 4th is there so start "a" with ind 1 
            # remove that a and make start index 2 now 
            while s[end] in charSet:
                charSet.remove(s[start])
                start +=1 
            #remove the start and move it while add end to set
            charSet.add(s[end])
            longest = max(longest, end - start+1)
        return longest 
