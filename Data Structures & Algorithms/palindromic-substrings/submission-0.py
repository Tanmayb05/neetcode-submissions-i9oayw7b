class Solution:
    def countSubstrings(self, s: str) -> int:
        output = 0

        for i in range(len(s)):
            # ODD (left and right are the same)
            left = i; right = i
            # LOOP: left and right in bounds and palindrome condition
            while left>=0 and right<len(s) and s[left]==s[right]:
                # UPDATE output palindrome found!
                output+=1
                # UPDATE pointers
                left-=1; right+=1

            # EVEN (left and right will be beside each other)
            left = i; right = i+1
            # LOOP: left and right in bounds and palindrome condition
            while left>=0 and right<len(s) and s[left]==s[right]:
                # UPDATE output palindrome found!
                output+=1
                # UPDATE pointers
                left-=1; right+=1
        return output