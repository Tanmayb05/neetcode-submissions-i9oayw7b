class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1; B = nums2
        # Get total and half
        total = len(A)+len(B); middle = total//2

        # 'A' should always be the shorter Array
        if len(B)<len(A):
            A,B=B,A
        

        left = 0; right = len(A) - 1
        while True:
            middle_A = (left+right)//2
            middle_B = middle - middle_A - 2 # A starts at 0 and B starts at 0 so minus 2

            # indices can be out of bounds
            # if i<0 can we give default value? float("-inf")
            A_lpi = A[middle_A] if middle_A>=0 else float("-inf")
            A_rpi = A[middle_A+1] if middle_A+1<len(A) else float("inf")
            B_lpi = B[middle_B] if middle_B>=0 else float("-inf")
            B_rpi = B[middle_B+1] if middle_B+1<len(B) else float("inf")

            # partiiton is correct
            if A_lpi <= B_rpi and B_lpi <= A_rpi:
                # odd
                if total%2: return min(A_rpi, B_rpi)
                # even
                return (max(A_lpi,B_lpi) + min(A_rpi,B_rpi))/2
            elif A_lpi > B_rpi: right = middle_A - 1
            else: left = middle_A + 1