class Solution {
public:
    vector<int> buildArray(vector<int>& nums) {
        std::vector<int> permutation;
        if(nums.empty()) return nums;

        for(int i =0; i < nums.size(); i++){
           permutation.push_back(nums[nums[i]]); 
        }
        
        return permutation; 
    }
};