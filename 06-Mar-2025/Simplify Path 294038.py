# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        
        path = path.split('/')
        stack = []
        print(path)
        for directory in path:
            if directory and directory != '.':
                if directory == '..':
                    if stack:
                        stack.pop()
                else:
                    stack.append(directory)

            print(directory, stack)


        return '/' + '/'.join(stack)