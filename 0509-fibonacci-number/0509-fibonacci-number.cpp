class Solution {
public:
    int fib(int n) {
        int result = 0;

        if(n == 0){
            return 0;
        }
        else if(n == 1){
            return 1;
        }

        return n-1;
        
    }
};