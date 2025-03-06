# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for folder in logs:
            if folder == "../":
                if stack:
                    stack.pop()

            elif folder == "./":
                pass

            else:
                folder = folder.split("/")[0]
                stack.append(folder)


        return len(stack)