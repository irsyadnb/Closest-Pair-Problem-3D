import numpy as np

eucCtr = 0

def quickSort(points): # QuickSort Divide & Conquer
    size = len(points)
    mid = size // 2
    
    if(size <= 1):
        return points
    else:
        pivot = points[mid]
        lessThanPivot = []
        biggerThanPivot = []
        isPivot = []
        for i in range(len(points)):
            if points[i] < pivot:
                lessThanPivot.append(points[i])
            elif points[i] == pivot:
                isPivot.append(points[i])
            else:
                biggerThanPivot.append(points[i])
        
    return quickSort(lessThanPivot) + isPivot + quickSort(biggerThanPivot)

def eucDist(point1, point2): # Basic euclidean distance
    return np.sqrt( pow(point1[0] - point2[0], 2) + pow(point1[1] - point2[1], 2) + pow(point1[2] - point2[2], 2) )

def eucDistFewPoints(point, size): #Solving few close pair points using brute force
    points = []
    temp = 9999
    for i in range(size):
        for j in range(i+1, size):
            if(eucDist(point[i], point[j]) < temp):
                temp = eucDist(point[i], point[j])
                points.append(point[i])
                points.append(point[j])
                global eucCtr
                eucCtr += 1
    return points, temp, eucCtr