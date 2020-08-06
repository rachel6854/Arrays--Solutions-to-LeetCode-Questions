#Majority Element (Restriction: Time Complexity - O(n))
#https://leetcode.com/problems/majority-element/


#Time Complexity: O(n)
#Space Complexity: O(n)




class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter={}
        for num in nums:
            if num in counter:
                counter[num]+=1
            else:
                counter[num]=1
        length=len(nums)//2
        for num in counter:
            if counter.get(num)>length:
                return num
        
