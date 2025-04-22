# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        
        graph = defaultdict(list)

        for i in range(len(equations)):

            dividend, divisor = equations[i]
            quotient = values[i]

            graph[dividend].append((divisor, quotient))
            graph[divisor].append((dividend, 1/quotient))

        ans = []

        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                ans.append(float(-1))
                continue

            q = deque()
            q.append((dividend, 1))
            flag = False
            visited = set()

            while q:

                x, product = q.popleft()
                visited.add(x)

                
                if x==divisor:
                    print(dividend, divisor)
                    ans.append(product)
                    flag = True
                    break

                else:
                    dividend = x
                    for neighbor in graph[x]:

                        if neighbor[0] in visited:
                            continue

                        q.append((neighbor[0], neighbor[1]*product))

            if not flag:
                ans.append(float(-1))


        return ans


