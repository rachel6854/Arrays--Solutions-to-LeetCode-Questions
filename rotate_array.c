/* Rotate Array​ (Could you do it in-place with O(1) extra space?)
https://leetcode.com/problems/rotate-array/ */

/*Time Complexity: O(n*k)
Space Complexity: O(1) */

void rotate(int* nums, int numsSize, int k){
    for(int i=0;i<k;++i)
    {
        int tmp=nums[numsSize-1];
        for(int j=numsSize-1;j>0;--j)
        {
           nums[j]=nums[j-1];
        }
        nums[0]=tmp;
    }

}



