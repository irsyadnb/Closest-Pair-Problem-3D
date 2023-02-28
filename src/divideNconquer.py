import matplotlib.pyplot as plt
import numpy as np
from points import *
from utility import *

def divideAndConquer(points):
    size = len(points)

    # - Base Case
    if(size<4):
        closestpoints, closestDist, ctr = eucDistFewPoints(points, size)
        return closestpoints, closestDist, ctr

    # - Divide
    mid = size // 2  # Dividing the array into two sides
    leftside = points[:mid]
    rightside = points[mid:]

    # - Recursively conquering left and right
    leftpoints, deltaL, ctr = divideAndConquer(leftside)
    rightpoints, deltaR, ctr = divideAndConquer(rightside)

    closestDist = min(deltaL, deltaR)

    newClosestBetween = False

    # Finding distance near middle strip and comparing with earlier closest distance
    for i in range(len(leftside)):
        for j in range(len(rightside)):
            # Distance between left side and right side
            distanceNearMid = abs(leftside[i][0] - rightside[j][0]) 

            # Distance near middle must be smaller and check also for its euclidean distance
            if(distanceNearMid < closestDist and eucDist(leftside[i], rightside[j]) < closestDist): 
                closestpoints = []
                closestDist = eucDist(leftside[i], rightside[j])
                closestpoints.append(leftside[i])
                closestpoints.append(rightside[j])
                ctr+=2
                newClosestBetween = True

    # If no pair of points near middle strip with distance less than earlier closest distance
    # Keep using the earlier closes distance
    if not newClosestBetween : 
        # Assign two points with the earlier closest distance
        closestpoints = []
        if(deltaL < deltaR):
            closestpoints.append(leftpoints)
        else:
            closestpoints.append(rightpoints)

    return closestpoints, closestDist, ctr