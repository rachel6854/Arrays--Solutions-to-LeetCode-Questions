#Sort Colors (Could you come up with a one-pass algorithm using only constant space?)
#https://leetcode.com/problems/sort-colors/

#Time Complexity: O(n)- one-pass algorithm
#Space Complexity: O(1)



class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        start2 = len(nums)-1
        end0 = 0
        i=0
        
        while i <= start2:
            if nums[i] == 0:
                nums[i], nums[end0] = nums[end0], nums[i]
                end0 += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[start2] = nums[start2], nums[i]
                start2 -= 1
            else:
                i += 1
                
        return nums
