# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque([0])

        visited = set()
        while q:
            for _ in range(len(q)):
                room = q.popleft()
                visited.add(room)

                for key in rooms[room]:
                    if key in visited:
                        continue
                    q.append(key)

        return len(visited) == len(rooms)