class Solution {
public:
    vector<int> findWordsContaining(vector<string>& words, char x) {


        std::vector<int> ans;
        for(int i = 0; i < words.size(); i++){

            for(auto& elem: words[i]){
                if(elem == x){
                    ans.push_back(i);
                    break;
                }
            }

        }

        return ans;
        
    }
};