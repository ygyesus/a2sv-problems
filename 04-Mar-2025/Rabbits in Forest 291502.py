# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # answer -> answer+1

        ansTotal = 0
        answers.sort(key = lambda x: -x)
        
        while answers:
            
            others = answers[-1]
            rabbits = others + 1
            # print(answers, rabbits)
            ansTotal += rabbits

            
            while answers and answers[-1] == others and rabbits:
                answers.pop()
                rabbits -= 1

        return ansTotal

