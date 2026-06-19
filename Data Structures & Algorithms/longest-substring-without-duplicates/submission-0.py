class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        longest = 0
        charSet = set()

        for end in range(len(s)):
            while s[end] in charSet:
                charSet.remove(s[start])
                start +=1
            charSet.add(s[end])
            longest = max(longest, end - start+1)
        return longest
