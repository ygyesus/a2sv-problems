# Problem: Seat Reservation Manager - https://leetcode.com/problems/seat-reservation-manager/description/

class SeatManager:

    def __init__(self, n: int):
        self.unreserved = [x for x in range(1, n+1)]
        self.reserved = set()
        

    def reserve(self) -> int:
        seatNumber = heappop(self.unreserved)
        self.reserved.add(seatNumber)
        return seatNumber

    def unreserve(self, seatNumber: int) -> None:
        self.reserved.remove(seatNumber)
        heappush(self.unreserved, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)