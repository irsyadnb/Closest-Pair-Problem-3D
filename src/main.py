import time
import matplotlib.pyplot as plt
import numpy as np
from divideNconquer import *
from points import *
from utility import *
import platform

start = True

while(start):
    print("Welcome to Closest Pair Problem using Divide and Conquer Algorithm")
    print("Select how do you wanna inser the points : ")
    print("1. Manual Insertion")
    print("2. Generate Random")
    while True:
        try:
            inputs = int(input("> "))
            break
        except ValueError:
            print("Invalid entry. Please try again")
    while(inputs!=1 and inputs != 2):
        print("Welcome to Closest Pair Problem")
        print("Select how do you wanna inser the points : ")
        print("1. Manual Insertion")
        print("2. Generate Rnadom")
        while True:
            try:
                inputs = int(input("> "))
                break
            except ValueError:
                print("Invalid entry. Please try again")
    start = False
    flag = False
    if (inputs == 1):
        while True:
            try:
                points = int(input("Insert n points you would like to try : "))
                if(points < 2):
                    print("The minimum points is 2!")
                else:
                    flag = True
                    break
            except ValueError:
                print("Invalid entry. Please try again")
        start = time.time()
        vector, ax= pointMakerManual(points)
    else:
        start = time.time()
        print("Generating points...")
        vector, ax = pointMaker()

    pointsSortedByX = quickSort(vector)

    closestPair, distance, ctr = divideAndConquer(pointsSortedByX)
    end = time.time()

    dncTime = end - start

    print("Using bruteforce algorithm... (for comparison purposes)")
    start = time.time()
    test = 999
    eucCtrbf = 0
    for i in range(len(vector)):
        for j in range(i+1,len(vector)):
            eucCtrbf += 1
            if(eucDist(vector[i], vector[j]) < test):
                test = eucDist(vector[i], vector[j])
                if(test == distance):
                    point1 = vector[i]
                    point2 = vector[j]
    end = time.time()

    bfTime = end - start

    xpair = [point1[0], point2[0]]
    ypair = [point1[1], point2[1]]
    zpair = [point1[2], point2[2]]

    ax.scatter(xpair,ypair,zpair,c='red',s=80)
    print()
    print("===Divide & Conquer===")
    print("^Nearest Points^")
    print("Point 1 <x,y,z> : ", point1)
    print("Point 2 <x,y,z> : ", point2)
    print("Euclidean Distance  : ", distance)
    print(test)
    print("Euclidean distance used counter on Divide & Conquer : ", ctr)
    print("Euclidean distance used counter on BruteForce : ", eucCtrbf)
    print("Execution time using Divide & Conquer : ", dncTime, "seconds")
    print("Execution time using BruteForce : ", bfTime, "seconds")
    print("Computer Specifitation : ", platform.platform())

    print("Do you want to visualize?")
    print("(Y/y) or (N/n)")
    v = str(input("> "))
    if(v == "Y" or v == "y"):
        plt.show()
    print("Goodbye!")
    start = False