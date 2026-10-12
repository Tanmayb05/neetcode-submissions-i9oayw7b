class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # init stack and max_area
        stack = []
        max_area = 0

        for curr_index, curr_height in enumerate(heights):
            # init start_index for every element
            start_index = curr_index
            # stack exists and the histogram is descending
            while stack and stack[-1][1] > curr_height:
                # get the popped index and height
                popped_index, popped_height = stack.pop()
                # update the max_area
                max_area = max(max_area, popped_height * (curr_index-popped_index))
                start_index = popped_index
            stack.append((start_index, curr_height))
            
        for popped_index, popped_height in stack:
            max_area = max(max_area, popped_height * (len(heights)-popped_index))
        return max_area



