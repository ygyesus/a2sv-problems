# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        myDigits = {str(x) for x in range(10)}
        
        stack = []

        for char in s:
            if char != ']':
                stack.append(char)

            else:
                string = ""
                while stack[-1] != '[':
                    string = stack.pop() + string

                # print(string)
                stack.pop()

                digits = ""
                # print(stack)
                while stack and stack[-1] in myDigits:
                    digits = stack.pop() + digits

                # print(digits)

                stack.append(int(digits)*string)

        # print(stack)
        return ''.join(stack)