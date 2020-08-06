#Squares of a Sorted Array (Restriction: Time Complexity - O(n))
#https://leetcode.com/problems/squares-of-a-sorted-array/


#Time Complexity: O(n)
#Space Complexity: O(n)


class Solution(object):          
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        start=0;
        end=len(A)-1;
        res=[]
        while(start<=end):
            if A[start]*A[start]>A[end]*A[end]:
                res.append(A[start]*A[start])
                start+=1    
            else:
                res.append(A[end]*A[end]) 
                end-=1
        return res[::-1]
