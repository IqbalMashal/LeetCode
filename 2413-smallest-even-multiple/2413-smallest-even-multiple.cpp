class Solution {
public:
    int smallestEvenMultiple(int n) {

        int evenMult;

        if(n % 2 == 0){
            evenMult = n;
        }
        else{
            evenMult = n * 2;
        }
        

        return evenMult;
    }
};