class Solution {
public:
    int minMovesToSeat(vector<int>& seats, vector<int>& students) {

        int moves = 0;
        std::sort(seats.begin(), seats.end());
        std::sort(students.begin(), students.end());

        for(int i = 0; i<seats.size();i++){
            moves += (seats[i] > students[i]) ? (seats[i] - students[i]) : (students[i] - seats[i]);
        }
        return moves;
        
    }
};