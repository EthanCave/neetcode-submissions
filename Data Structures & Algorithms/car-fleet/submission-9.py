class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def sorting_time(position, speed):
            combined = []
            for i in range(len(position)):
                combined.append((position[i],speed[i]))
            combined.sort(reverse= True, key = lambda a: a[0])
            return combined

        time_per_fleet = []
        combined = sorting_time(position,speed)
        for i in range(len(position)):
            
            time = (target - combined[i][0]) / combined[i][1]
            if time_per_fleet and time <= time_per_fleet[-1]:
                continue
            else:
                time_per_fleet.append(time)
        return len(time_per_fleet)
        


