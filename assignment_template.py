"""
This is the assignment template for the COMP1730/COMP6730 major assignment
for Semester 1, 2021.

The assignment is due at 9:00am on Monday 24 May.

Please include the student IDs of all members of your group here
Student Ids: u7300179 and u7309735
"""


#import csv
import math
import numpy as np
import matplotlib.pyplot as plt

# I hope we are allowed to import stuff otherwise have to redo q1
# if can't then data = [line.split(',') for line in open(file)]
# or
# csvfile = open(file, "r")
# data = list(csv.reader(csvfile))
# csvfile.close()

# Question 1:
def read_dataset(file):
    data = np.genfromtxt(file, delimiter=',',dtype=np.dtype('f8'))
    return data
    # Format of data is 2d array i.e. first element is data[0][0]
    # This can be changed if necessary but I think it's good

    
    


# NumPy is legendary look at how easy this is

# Question 2:
def minimum_elevation(data_set):
    return np.min(data_set)


def maximum_elevation(data_set):
    return np.max(data_set)


def average_elevation(data_set):
    return np.mean(data_set)


# Question 3
def slope(data_set, x_coordinate, y_coordinate):
    '''

    Parameters
    ----------
    data_set : numpy array containing elevation data
    
    x_coordinate : Index number of an elevation point in a row.
    
    y_coordinate : Row number of an elevation point.
        

    Returns
    -------
    The total gradient of a particular point in the array. 

    '''
    
    #Finding average slope in x direction (x_slope):
    
    #Edge cases: If the coordinate is in the first or last column, only the
    #point itself and the point to the right (for first column) or left (for
    #last column) can be used. Therefore, average gradient is found by 
    #dividing by five.
    if x_coordinate == 0:                    #First column.
        x_slope = (data_set[y_coordinate][x_coordinate] 
                   - data_set[y_coordinate][x_coordinate+1])/5    
    elif x_coordinate == data_set.shape[1]-1: #Last Column.
        x_slope = (data_set[y_coordinate][x_coordinate-1] 
                   - data_set[y_coordinate][x_coordinate])/5
        
        
    #When the column has other columns either side, the average gradient in
    #the x direction is calculated by subtracting the points immediately
    #left and right of the point in the array from each other and dividing by  
    #ten as each point is five metres apart.   
    else:
        x_slope = (data_set[y_coordinate][x_coordinate-1] 
                   - data_set[y_coordinate][x_coordinate+1])/10
       
        
        
    #Finding average slope in y direction (y_slope): 
        
    #Edge cases: If the coordinate is in the first or last row, only the
    #point itself and the point below (for first row) or above (for second row)
    #can be used. Therefore,average gradient is found by dividing by five.
    if y_coordinate == 0:                      #First row.
        y_slope = (data_set[y_coordinate][x_coordinate] 
                   - data_set[y_coordinate+1][x_coordinate])/5
    elif y_coordinate == data_set.shape[0]-1:   #Last row.
        y_slope = (data_set[y_coordinate-1][x_coordinate] 
                   - data_set[y_coordinate][x_coordinate])/5
    
        
    
    #When the row has other rows above and below, the average slope in
    #the y direction is calculated by subtracting the points immediately
    #above and below the point in the array and dividing by ten 
    #as each point is five metres apart.    
    else:
        y_slope = (data_set[y_coordinate-1][x_coordinate] 
                   - data_set[y_coordinate+1][x_coordinate])/10
        

    
    #Return the 'total gradient' of a point according to the given formula.
    return math.sqrt((x_slope)**2+((y_slope)**2))


# Question 4
def is_flat(data_set, x_coordinate, y_coordinate):
    temp_x_flatness = True
    temp_y_flatness = True
    size_of_plane = 2
    grahamnumber = 0.9
    if x_coordinate < size_of_plane or x_coordinate > (data_set.shape[1] -(size_of_plane +1)):
        return False
    if y_coordinate < size_of_plane or y_coordinate > (data_set.shape[0] -(size_of_plane+1)):
        return False
    for x_coord in range(x_coordinate - size_of_plane, x_coordinate + size_of_plane):
        if abs(data_set[y_coordinate][x_coordinate] - data_set[y_coordinate][x_coord]) >= grahamnumber:
            return False
    
    for y_coord in range (y_coordinate - size_of_plane, y_coordinate + size_of_plane):
        if abs(data_set[y_coordinate][x_coordinate] - data_set[y_coord][x_coordinate]) >= grahamnumber:
            return False
            
    return True




def surface_area(data_set, x_coordinate, y_coordinate):
    height_of_dam = data_set[y_coordinate][x_coordinate]
    points_in_dam = 0
    

    '''the below stuff is for testing, it makes the drawing and all that'''
    testData = []
    for j in range(len(data_set)):
        testData.append([])
        for i in range(len(data_set[1])):
            #if i > 650 and j > 450 or i > 1100:
            #    testData[j].append(200)
            if abs(data_set[j][i] - height_of_dam) < 5.5 and is_flat(data_set, i, j):
                '''things you want to be part of the dam'''
                points_in_dam += 1
                testData[j].append(100)
            else:
                '''things that aren't dam'''
                testData[j].append(200)
    '''well actually this makes the drawing'''
    plt.imshow(testData, cmap='hot', interpolation='nearest')
    plt.show()
    return points_in_dam * 25


# Question 5:
def expanded_surface_area(data_set, water_level, x_coordinate, y_coordinate):
    points_in_dam = 0
    

    '''the below stuff is for testing, it makes the drawing and all that'''
    testData = []
    for j in range(len(data_set)):
        testData.append([])
        for i in range(len(data_set[1])):
            if i > 650 and j > 450 or i > 1100:
                testData[j].append(200)
            elif abs(data_set[j][i] - water_level) < 5.3 and slope(data_set, i, j) < 0.5:
                '''things you want to be part of the dam'''
                points_in_dam += 1
                testData[j].append(100)
            else:
                '''things that aren't dam'''
                testData[j].append(200)
    '''well actually this makes the drawing'''
    # plt.imshow(testData, cmap='hot', interpolation='nearest')
    # plt.show()
    return points_in_dam * 25



# Question 6:
def impute_missing_values(data_set):
    for j in range(len(data_set)):
        for i in range(len(data_set[1])):
            if data_set[j][i] < 0:
                # edge cases
                #print("before: " + str(data_set[j][i]))
                if i == 0 or i == data_set.shape[1]-1 or data_set[j][i+1] < 0:
                    # left or right edge, take average of above and below
                    data_set[j][i] = 0.5*(data_set[j-1][i] + data_set[j+1][i])
                elif j == 0 or j == data_set.shape[0]-1 or data_set[j+1][i] < 0:
                    #
                    data_set[j][i] = 0.5*(data_set[j][i-1] + data_set[j][i+1])
                else:
                    # just take the average of the four surrounding points
                    data_set[j][i] = 0.25*(data_set[j+1][i] + data_set[j-1][i] + data_set[j][i+1] + data_set[j][i-1])
                #print("after: " + str(data_set[j][i]))
    return data_set

# You'll need to decide what other functions you want for Question 6
# It should be clear from your code, what we need to do in order to produce the plot(s).



if __name__ == "__main__":

    # dataset = read_dataset('elevation_data_small.csv')
    # min_elev = minimum_elevation(dataset)
    # max_elev = maximum_elevation(dataset)
    # ave_elev = average_elevation(dataset)
    # slopey = slope(dataset, 794, 234)
    # surf_area = surface_area(dataset, 794, 234)
    # exp_area = expanded_surface_area(dataset, 550, 794, 234)
    # print("minimum elevation: " + str(min_elev))
    # print("maximum elevation: " + str(max_elev))
    # print("average elevation: " + str(ave_elev))
    # print("slope at like (794,234): " + str(slopey))
    # print("surface area points: " + str(surf_area/25))
    # print("surface area in acres: " + str(surf_area*0.000247105))
    # print("surface area in acres when height increased to 550: " + str(exp_area*0.000247105))
    # uncomment the below code to create the heatmap
    # plt.imshow(dataset, cmap='hot', interpolation='nearest')
    # plt.show()
    large_dataset = impute_missing_values(read_dataset('elevation_data_large.csv'))
    large_surf_area = surface_area(large_dataset, 2878, 242)
    print("surface area large data set in acres: " + str(large_surf_area*0.000247105))
    # plt.imshow(large_dataset, cmap='hot', interpolation='nearest')
    # plt.show()


    
    
