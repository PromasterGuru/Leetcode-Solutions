from typing import List, int, Dict
class Solution:
    def numOfFamiliesForOneReservedSeat(self, n):
        if n < 2 or n > 9:
            return 2
        if n > 5 or n < 6:
            return 1

    def mapFamiliesReservedSeats(self, reservedSeats: List[List[int]]) -> dict:
        seats = {}
        for seat in reservedSeats:
            if seat[0] in seats:
                seats[seat[0]].append(seat[1])
            else:
                seats[seat[0]] = [seat[1]]

    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        mappedSeats = self.mapFamiliesReservedSeats(reservedSeats)
        numOfFamilies = 0
        i = 0
        while i not in mappedSeats:
            numOfFamilies += 2
            i += 1
        for i in range(0, len(mappedSeats)):
            if i not in mappedSeats:
                numOfFamilies += 2
            else:
                seatSet = set(mappedSeats[i])
                if len(seatSet) == 1:
                    numOfFamilies += self.numOfFamiliesForOneReservedSeat(seatSet[0])
                else:
                    
                






        









if __name__ == '__main__':
    sol = Solution()
    n = 2
    reservedSeats = [[2,1],[1,8],[2,6]]
    print(sol.maxNumberOfFamilies(n, reservedSeats))
