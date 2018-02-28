# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

import numpy as np

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    #Create a list of possible positions, where the first value is the number of steps to get there
    found = False
    pos_list = np.array([[0,0,0]])
    
    while (not found):
        if len(pos_list)==0:
            return -1 #no possible path
        steps = pos_list[:,0]
        idx_shortest = steps.argmin()

        position = pos_list[idx_shortest]
        #Expand to the nearest neighbors
        for i in range (0,4):
            expansion = np.array([position[0]+1,position[1]+delta[i][0],position[2]+delta[i][1]])
            #Check that expanded position lied inside the map
            if expansion [1] >= 0 and expansion [2] >= 0 and expansion [1] < len(grid) and expansion [2] < len(grid[0]):
                # check that expanded position doesn't lie on a wall
                if grid[expansion[1]][expansion[2]] == 0:
                    pos_list = np.vstack((pos_list,expansion))
                    grid[expansion[1]][expansion[2]] = 1

        #Build wall where we were before so that we don't go back            
        grid[position[1]][position[2]] = 1
        pos_list = np.delete(pos_list, idx_shortest, 0) # delete already searched position


                
        for i in range(0,pos_list.shape[0]):
            if pos_list[i][1]==goal[0] and pos_list[i][2]==goal[1]:
                return pos_list[i][0] #return number of steps
    
    
    return -1 #no path found

print search(grid, init, goal, cost)