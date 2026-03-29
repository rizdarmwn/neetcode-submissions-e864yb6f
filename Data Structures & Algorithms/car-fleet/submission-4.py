class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        st = []

        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            st.append((position[i], time))
        st = sorted(st)

        fleets = []
        while st:
            fleets.append(st.pop()[1])
            if len(fleets) >= 2 and fleets[-1] <= fleets[-2]:
                fleets.pop()
        
        return len(fleets)
            

