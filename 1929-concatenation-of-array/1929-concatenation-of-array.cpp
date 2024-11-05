class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> newArr{nums};

        for(auto& elem: nums){
            newArr.push_back(elem);
        }

        return newArr;
        
    }
};