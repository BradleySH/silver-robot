from typing import List

# remove duplicates from a sorted array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # check to make sure the length of the array is greater than 0
        if len(nums) == 0:
            return 0
        
        # initialize a pointer to the first element
        i = 0

        # iterate through the array
        for j in range(1, len(nums)):
            # if the current element is not equal to the previous element
            if nums[j] != nums[i]:
                # move the pointer to the next element
                i += 1
                # swap the current element with the element at the pointer
                nums[i] = nums[j]
        return i + 1