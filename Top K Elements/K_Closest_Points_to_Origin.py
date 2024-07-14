"""
Given a list of points on a plane, where the plane is a 2-D array with (x, y) coordinates, find the k closest points to the origin 
(0,0).

Constraints:  
1 ≤ k ≤ points.length ≤ 10^3   
-10^4 < x[i], y[i] < 10^4  
"""

from point import Point
import heapq

# Time Complexity: O(Nlogk)
# Space Complexity: O(k)

def k_closest(points, k):
  
    
    max_heap = []
    #Adding k points to max_heap
    for i in range(k):
        heapq.heappush(max_heap, points[i])

    for i in range(k, len(points)):
        # Comparing remaining points to the root whether the new point is closer to origin
        if points[i].distance_to_origin()<max_heap[0].distance_to_origin():
            heapq.heappop(max_heap)
            heapq.heappush(max_heap, points[i])
    
    return max_heap

point_res = k_closest([Point(2187,1683), Point(-8324,9941),Point(-3659,-4206),Point(2920,9816),Point(-4113,-6415),Point(2094,115), Point(-297,-162)], 4)


