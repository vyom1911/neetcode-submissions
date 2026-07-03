class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
            # Start computing arrival time (target-position)/speed
            # target = 10, position = [4,1,0,7], speed = [2,2,1,1]
            # t = [3,4.5,10,3]
            # [7,4,1,0].   [1,2,2,1]
            # [3,3,4.5,10]
            # sl = 4.5 
            # fl = 2

            cars = sorted(zip(position,speed),reverse=True)
            fleets = 0
            slowest_time = 0


            for pos, spd in cars:
                time = (target - pos)/spd
                if time > slowest_time:
                    slowest_time = time
                    fleets+=1
            return fleets
