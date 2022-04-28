class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        my_list = []
        answer = []
        distances = []
        
        for point in points:
            
            x = point[0]
            y = point[1]
            distance = (x**2 + y**2)**0.5
            distances.append(distance)
            point.append(distance)
            answer.append(point)
            
        for i in range(k):
            for j in range(len(distances)-i-1):
                if distances[j] < distances[j+1]:
                    distances[j], distances[j+1] = distances[j+1], distances[j]
                    
        distances = distances[len(distances)-k:len(distances)]
            
       
        for index in range(k):
            for point in answer:
                if point[2] in distances and point[0:2] not in my_list:
                    my_list.append(point[0:2])
                    break
              
        return my_list

        