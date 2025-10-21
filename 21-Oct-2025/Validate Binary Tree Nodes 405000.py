# Problem: Validate Binary Tree Nodes - https://leetcode.com/problems/validate-binary-tree-nodes/

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        incoming = Counter()

        for node in range(n):
            if leftChild[node] != -1:
                incoming[leftChild[node]] += 1
                if incoming[leftChild[node]] > 1: return False

            if rightChild[node] != -1:
                incoming[rightChild[node]] += 1
                if incoming[rightChild[node]] > 1: return False

        visited = set()
        stack = [node for node in range(n) if incoming[node] == 0]
        if len(stack) > 1: return False

        while stack:
            node = stack.pop()
            if node in visited: return False
            visited.add(node)
            if leftChild[node] != -1:
                incoming[leftChild[node]] -= 1
                if incoming[leftChild[node]] == 0:
                    stack.append(leftChild[node])

            if rightChild[node] != -1:
                incoming[rightChild[node]] -= 1
                if incoming[rightChild[node]] == 0:
                    stack.append(rightChild[node])

        return len(visited) == n