class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {

        std::vector<bool> greatest;

        int max = 0;
        for(auto& elem: candies){
            if(elem > max){
                max = elem;
            }
        }

        for(auto& elem : candies){
            greatest.push_back((elem + extraCandies) >= max);
        }
        
        return greatest;
    }
};