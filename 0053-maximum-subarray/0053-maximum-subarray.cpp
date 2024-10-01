class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int current_sum = nums[0];
        int total= nums[0];
        for (int i=1 ;i<nums.size();i++){
         current_sum=max(current_sum+nums[i], nums[i]);
         total=max(total,current_sum);
        }
        return total;
    }
};