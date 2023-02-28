from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def pointMaker(): #Random Point Generator
    x = np.random.randint(500)
    fig = plt.figure(figsize=(5,5))

    ax = fig.add_subplot(111, projection='3d')
    
    xs = np.random.random(x)
    ys = np.random.random(x)
    zs = np.random.random(x)
    scatter = ax.scatter(xs,ys,zs)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    points = np.array(scatter._offsets3d)

    vector = []
    for i in range(len(points[0])):
        list = []
        list.append(points[0][i])
        list.append(points[1][i])
        list.append(points[2][i])
        vector.append(list)

    return vector, ax

def pointMakerManual(n): #Manual Point Generator
    fig = plt.figure(figsize=(5,5))

    ax = fig.add_subplot(111, projection='3d')

    xs = np.random.random(n)
    ys = np.random.random(n)
    zs = np.random.random(n)
    scatter = ax.scatter(xs,ys,zs)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    points = np.array(scatter._offsets3d)

    vector = []
    for i in range(len(points[0])):
        list = []
        list.append(points[0][i])
        list.append(points[1][i])
        list.append(points[2][i])
        vector.append(list)

    return vector, ax