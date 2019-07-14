class Solution:
    def maxArea(self, height: List[int]) -> int:
        water_area = 0
        
        # initializing the values of the first and the last container bars 
        
        head = 0
        tail = len(height) - 1 
        
        # looping through the list of heights and finding the optimal solution
        
        for iteration in range(len(height)):
            
            # the width of the container
            width = abs(head - tail)
            # if height of head <= height of tail , store the area and increment head
            if height[head] <= height [tail]:
                temp_area = width * height[head]
                head += 1
            # idicates that the tail < head so store the area and decrement  
            else:
                temp_area = width * height[tail]
                tail -= 1 
            
            # check if the stored area is smaller than the previous stored area, update if true
            if temp_area > water_area:
                water_area = temp_area
        
        return water_area
                
