#Merge Sorted Array (Restriction: Time Complexity - O(m + n))
#https://leetcode.com/problems/merge-sorted-array/

#Time Complexity: O(m+n)
#Space Complexity: O(1)

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
 
        curr=0
        for i in range(m+n):
            if i-curr>=n or (curr<m and nums2[i-curr]>nums1[i]):
                curr+=1
            else :
                nums1.insert(i,nums2[i-curr])
                nums1.pop(len(nums1)-1)
