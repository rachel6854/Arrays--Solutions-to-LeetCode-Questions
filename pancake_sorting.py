#Pancake Sorting
#https://leetcode.com/problems/pancake-sorting/

#Time Complexity: O(n*2)
#Space Complexity: O(n)



class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(len(A) - 1, 0, -1):
            imax = 0
            for j in range(i+1):
                if A[j] > A[imax]:
                    imax = j
            if imax!=i:
                result.append(imax + 1)
                A = A[imax::-1] + A[imax + 1:]
                result.append(i+1)
                A = A[i::-1] + A[i + 1:]
        return result
