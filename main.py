class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # answer = []

        # for i in range(len(temperatures)):
        #     count = 0
        #     found = False

        #     for j in range(i + 1, len(temperatures)):
        #         count += 1
        #         if temperatures[j] >  temperatures[i]:
        #             found = True
        #             break

        #     if not found:
        #         count = 0        
        #     answer.append(count)
        # return answer

# The time complexity of this approach is O(n) because each index is pushed and popped from the stack exactly once.

        answer = [0] * len(temperatures)  # Initialize the answer array with zeros
        stack = []  # Stack to store indices of temperatures 
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index

            stack.append(i)
        return answer    
        
