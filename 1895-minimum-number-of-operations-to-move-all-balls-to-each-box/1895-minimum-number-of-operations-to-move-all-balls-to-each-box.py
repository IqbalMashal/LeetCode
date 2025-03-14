class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        if boxes == " ":
            return

        answer = []
        counter = 0

        for i in range(0, len(boxes)):
            for j in range(0, len(boxes)):
                if i != j:
                    if boxes[j] != "0":
                        counter += abs(i-j)
            answer.append(counter)
            counter = 0

        return answer 


        
        