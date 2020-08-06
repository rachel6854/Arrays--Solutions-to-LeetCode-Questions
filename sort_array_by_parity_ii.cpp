//Sort Array By Parity II
//https://leetcode.com/problems/sort-array-by-parity-ii/

//Time Complexity: O(n)
//Space Complexity: O(1) 



class Solution {
public:
    vector<int> sortArrayByParityII(vector<int>& A) {
        int odd=1;
        int even=0;
        size_t len=A.size()-1;
        while(true)
        {
            while(even<=len&&A[even]%2==0)
                even+=2;
            if (even>len)
                break;
            while(odd<=len&&A[odd]%2!=0)
                odd+=2;
            if (odd>len)
                break;
            int tmp=A[even];
            A[even]=A[odd];
            A[odd]=tmp;  
        }
        return A;
        
    }
};
