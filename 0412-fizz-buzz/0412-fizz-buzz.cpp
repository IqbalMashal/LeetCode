class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<std::string> str;
        if (n == 0){
            return str;
        }
        for (int i = 1; i <= n; i++){
            if(i % 3 == 0 && i % 5 == 0){
                str.push_back("FizzBuzz");
            }
            else if(i % 3 == 0){
                str.push_back("Fizz");
            }else if(i % 5 == 0){
                str.push_back("Buzz");
            }else{
                str.push_back(std::to_string(i));
            }
        }
        return str;
    }
};