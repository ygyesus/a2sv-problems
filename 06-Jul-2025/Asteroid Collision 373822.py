# Problem: Asteroid Collision - https://leetcode.com/problems/asteroid-collision/

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        

        stack = []

        for num in asteroids:
            
            if num<0:
                if not stack: 
                    stack.append(num)
                else:
                    # demolish existing
                    while stack and stack[-1]>0 and abs(stack[-1])<abs(num):
                        stack.pop()

                    if stack and stack[-1]<0:
                        stack.append(num)
                        continue

                    if stack:
                        if stack[-1]>0 and abs(stack[-1]) > abs(num):
                            continue
                        if stack[-1]>0 and abs(stack[-1]) == abs(num):
                            print("HERE")
                            stack.pop()
                            continue
                    else:
                        stack.append(num)

            elif num > 0:
                stack.append(num)

                        

            elif num>0:
                stack.append(num)

        return stack
