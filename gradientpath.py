import numpy as np
import matplotlib.pyplot as plt

# potential functions
def goalPotential(goal, gridX, gridY, gain):
    goalpot = np.zeros_like(gridX)
    for i in range(gridX.shape[0]):
        for j in range(gridX.shape[1]):
            goalpot[j, i] = 0.5 * gain * np.sqrt((goal[0] - (gridX[j, i], gridY[j, i])[0]) ** 2 + (goal[1] - (gridX[j, i], gridY[j, i])[1]) ** 2)
    return goalpot

def obstaclePotential(obstacle, gridX, gridY, threshold, gain, gain2):
    obstaclepot = np.zeros_like(gridX)
    distance = 0
    for i in range(gridX.shape[0]):
        for j in range(gridY.shape[1]):
            distance = np.sqrt((obstacle[0] - (gridX[j, i], gridY[j, i])[0]) ** 2 + (obstacle[1] - (gridX[j, i], gridY[j, i])[1]) ** 2)
            if distance <= threshold:
                obstaclepot[j, i] = 0.5 * gain * ((1 / distance) - (1 / threshold)) ** gain2
            else:
                obstaclepot[j, i] = 0
    return obstaclepot

# def totalPotential(goal, obstaclepoints, gridX, gridY, goalgain, obstaclegain, threshold):
#     goalpot = goalPotential(goal, gridX, gridY, goalgain)
#     totalpot = goalpot
#     for obstaclepoint in obstaclepoints:
#         obstaclepotential = obstaclePotential(obstaclepoint, gridX, gridY, threshold, obstaclegain)
#         totalpot = totalpot + obstaclepotential
#     return totalpot
    
# def generateWall(start, end, iter):
#     points = []
#     direction = np.asarray(end) - np.asarray(start)
#     for i in range(iter):
#         point = np.asarray(start) + (direction * i / (iter - 1))
#         points.append(point)
#     return points

# main function
if __name__ == "__main__":
    threshold = 5
    goalgain = 1
    obstaclegain = 1
    goal = (5, 5)
    obstacle = (2, 2)
    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.zeros_like(X)
    goalpot = goalPotential(goal, X, Y, goalgain)
    obstaclepot = obstaclePotential(obstacle, X, Y, threshold, obstaclegain, 1)
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            Z[i, j] = goalpot[i, j] + obstaclepot[i, j]
    
    plt.contourf(X, Y, Z, levels=50, cmap='viridis')
    plt.colorbar()
    
    plt.plot(goal[0], goal[1], 'ro')
    plt.title('Potential Field')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
    
    
    