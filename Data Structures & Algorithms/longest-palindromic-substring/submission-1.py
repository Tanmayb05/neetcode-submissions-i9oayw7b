class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            # ODD (left and right are the same)
            left = i; right = i
            # LOOP: left and right in bounds and palindrome condition
            while left>=0 and right<len(s) and s[left]==s[right]:
                # UPDATE res and resLen if the len(substring) is greater than the current resLen
                if right - left + 1 > resLen:
                    res = s[left:right+1]
                    resLen = right - left + 1
                # UPDATE pointers
                left-=1; right+=1

            # EVEN (left and right will be beside each other)
            left = i; right = i+1
            # LOOP: left and right in bounds and palindrome condition
            while left>=0 and right<len(s) and s[left]==s[right]:
                # UPDATE res and resLen if the len(substring) is greater than the current resLen
                if right - left + 1 > resLen:
                    res = s[left:right+1]
                    resLen = right - left + 1
                # UPDATE pointers
                left-=1; right+=1
        return res