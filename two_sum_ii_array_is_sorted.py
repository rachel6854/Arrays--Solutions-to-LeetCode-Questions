#Two Sum II - Input array is sorted
#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/



#Time Complexity: O(n)
#Space Complexity: O(1)



class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i=0
        j=len(numbers)-1
        while True:
            if numbers[i]+numbers[j]==target:
                return i+1,j+1
            elif numbers[i]+numbers[j]>=target:
                j-=1
            else:
                i+=1
