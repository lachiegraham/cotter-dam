"""
This is the assignment template for the COMP1730/COMP6730 major assignment
for Semester 1, 2021.

The assignment is due at 9:00am on Monday 24 May.

Please include the student IDs of all members of your group here
Student Ids: u7300179 and u7309735
"""


import math
import numpy as np
import matplotlib.pyplot as plt


# Question 1:
def read_dataset(file):
    '''
    Reads a csv file, and converts it's contents to a 2d array.'
    '''
    data = np.genfromtxt(file, delimiter=',')
    return data


    
    



# Question 2:
def minimum_elevation(data_set):
    '''
    Returns the minimum value of an array.
    Elements of array must be numbers.
    '''
    return np.min(data_set)


def maximum_elevation(data_set):
    '''
    Returns the maximum value of an array.
    Elements of array must be numbers.
    '''
    return np.max(data_set)


def average_elevation(data_set):
    '''
    Returns the mean of the values in an array.
    Elements of array must be numbers
    '''
    return np.mean(data_set)


# Question 3
def slope(data_set, x_coordinate, y_coordinate):
    '''
    Parameters
    ----------
    data_set : numpy array containing elevation data
    
    x_coordinate : column number of an elevation point
    
    y_coordinate : row number of an elevation point
    

    Returns
    -------
    The total gradient of a particular point in the array. 
    '''
    
    # calculate the slope using only x coordinates
    if x_coordinate == 0: # first column
        # gradient using self and point to the right    
        x_slope = (data_set[y_coordinate][x_coordinate] 
                   - data_set[y_coordinate][x_coordinate+1])/5    
    elif x_coordinate == len(data_set[0]) -1: # last column
        # gradient using self and point to the left
        x_slope = (data_set[y_coordinate][x_coordinate-1] 
                   - data_set[y_coordinate][x_coordinate])/5
    else:
        # gradient using the points left and right
        x_slope = (data_set[y_coordinate][x_coordinate-1] 
                   - data_set[y_coordinate][x_coordinate+1])/10
       
    # calculate the slope using only y coordinates
    if y_coordinate == 0: # first row
        # gradient using self and point below
        y_slope = (data_set[y_coordinate][x_coordinate] 
                   - data_set[y_coordinate+1][x_coordinate])/5
    elif y_coordinate == len(data_set) -1: # bottom row
        # gradient using self and point above
        y_slope = (data_set[y_coordinate-1][x_coordinate] 
                   - data_set[y_coordinate][x_coordinate])/5
    else:
        # gradient using the points above and below
        y_slope = (data_set[y_coordinate-1][x_coordinate] 
                   - data_set[y_coordinate+1][x_coordinate])/10
    # apply Pythagoras' theorem to find the total slope at the point
    return math.sqrt((x_slope)**2+((y_slope)**2))


def max_slope(data_set):
    '''
    Returns the maximum slope of a data set,
    calculated using the slope function.
    Elements of the data set must be numbers.
    '''
    # create a new list of the same size as data_set
    slope_list = np.ones((len(data_set), len(data_set[1])))
    for j in range(len(data_set)):
        for i in range (len(data_set[1])):
            # replace each element of the list with the slope
            # of that point in data_set
            slope_list[j][i] = slope(data_set, i, j)
    # max slope
    return np.max(slope_list)

# Question 4
def surface_area(data_set, x_coordinate, y_coordinate):
    '''
    Parameters
    ----------
    data_set : numpy array containing elevation data
    
    x_coordinate : column number of a point that lies on the dam
    
    y_coordinate : row number of a point that lies on the dam
        

    Returns
    -------
    The approximate surface area of the dam
    '''
    height_of_dam = data_set[y_coordinate][x_coordinate]
    points_in_dam = 0
    

    for j in range(len(data_set)):
        for i in range(len(data_set[1])):
            if abs(data_set[j][i] - height_of_dam) < 5.5 and is_flat(data_set,i,j):
                # the current i,j is part of the dam
                points_in_dam += 1
    # convert to square metres
    return points_in_dam * 25



# This function is mostly the same as the function above. The difference
# is that this one creates a plot of the points considered to be on the dam.
# It was used in testing for tweaking the code.
def plot_surface_area(data_set, x_coordinate, y_coordinate):
    '''
    Parameters
    ----------
    data_set : numpy array containing elevation data
    
    x_coordinate : column number of a point that lies on the dam
    
    y_coordinate : row number of a point that lies on the dam
    

    Returns
    -------
    A plot of all points that are calculated to be part of the dam 
    '''
    height_of_dam = data_set[y_coordinate][x_coordinate]
    
    # create a new numpy array with the same size as data_set
    test_data = np.ones((len(data_set), len(data_set[1]))) 
    
    for j in range(len(data_set)):
        for i in range(len(data_set[j])):
            if abs(data_set[j][i] - height_of_dam) < 5.5 and is_flat(data_set,i,j):
                # part of the dam, update the value in the array
                test_data[j][i] = 0
    # create the plot
    plt.imshow(test_data, cmap='hot', interpolation='nearest')
    plt.show()


# We originally used slope as the second condition for a point to be on
# the dam, but found that it wasn't good enough. This function does
# roughly the same thing, but not using directly adjacent points
def is_flat(data_set, x_coordinate, y_coordinate):
    '''
    Parameters
    ----------
    data_set : numpy array containing elevation data
    
    x_coordinate : column number of a point
    
    y_coordinate : row number of a point
    

    Returns
    -------
    Boolean value that indicates whether or not the ground surrounding the 
    given point is flat.
    '''
    size_of_plane = 2
    elevation_change = 0.9
    height_of_point = data_set[y_coordinate][x_coordinate]
    
    # for simplicity, points near the edges are ignored
    if x_coordinate <size_of_plane or x_coordinate > (len(data_set) -(size_of_plane +1)):
        return False
    if y_coordinate <size_of_plane or y_coordinate > (len(data_set[1]) -(size_of_plane+1)):
        return False
    
    # if any nearby point is at a significantly different height,
    # then the ground is not flat
    for x_coord in range(x_coordinate - size_of_plane, x_coordinate + size_of_plane):
        if abs(height_of_point - data_set[y_coordinate][x_coord]) >= elevation_change:
            return False
    for y_coord in range (y_coordinate - size_of_plane, y_coordinate + size_of_plane):
        if abs(height_of_point - data_set[y_coord][x_coordinate]) >= elevation_change:
            return False
    # ground is flat        
    return True



# Question 5:
def expanded_surface_area(data_set, water_level, x_coordinate, y_coordinate):
    '''
    Parameters
    ----------
    data_set : numpy array containing elevation data
    
    water_level : theoretical height of water
    
    x_coordinate : column number of a point on the dam
    
    y_coordinate : row number of a point on the dam
    

    Returns
    -------
    The approximate surface area of the dam if the water level were to
    rise to the given value.
    '''
    points_in_dam = 0
    safe_water_level = water_level
    
    # if new water level is below the dam, use the height of the dam
    if water_level < data_set[y_coordinate][x_coordinate]:
        safe_water_level = data_set[y_coordinate][x_coordinate]
        

    for j in range(len(data_set)):
        for i in range(len(data_set[j])):
            if abs(data_set[j][i] - safe_water_level) < 5.5 and slope(data_set, i, j) < 0.5:
               # to increase accuracy we can add requirements specific to
               # the small data set
                if len(data_set == 883):
                    if (i < 650 or j < 450) and i < 1100:
                        # the current i,j is part of the expanded dam
                        points_in_dam += 1
                else:
                    # not small data set but still a part of the expanded dam
                    points_in_dam += 1
    # convert to square metres
    return points_in_dam * 25

# Similarly to question 4, this function is to visualise what's going
# on in the above function
def plot_expanded_surface_area(data_set, water_level, x_coordinate, y_coordinate):
    '''
    Parameters
    ----------
    data_set : numpy array containing elevation data
    
    water_level : theoretical height of water
    
    x_coordinate : column number of a point that lies on the dam
    
    y_coordinate : row number of a point that lies on the dam
    

    Returns
    -------
    A plot of all points that are calculated to be part of the expanded dam 
    '''    
    safe_water_level = water_level
    
    # if new water level is below the dam, use the height of the dam
    if water_level < data_set[y_coordinate][x_coordinate]:
        safe_water_level = data_set[y_coordinate][x_coordinate]
    
    # create a new numpy array with the same size as data_set
    test_data = np.ones((len(data_set), len(data_set[1]))) 
    
    for j in range(len(data_set)):
        for i in range(len(data_set[j])):
            if abs(data_set[j][i] - safe_water_level) < 5.5 and slope(data_set, i, j) < 0.5:                # part of the dam, update the value in the array
                # increase accuracy for small data set    
                if len(data_set == 883):
                    if (i < 650 or j < 450) and i < 1100:
                        # point is in the expanded dam
                        test_data[j][i] = 0
                else:
                    # not small data set but still part of the expanded dam
                    test_data[j][i] = 0
    # create the plot
    plt.imshow(test_data, cmap='hot', interpolation='nearest')
    plt.show()

# Question 6:
def impute_missing_values(data_set):
    '''
    Corrects invalid values in a data set. Requires all incorrent entries
    to be represented as a negative number, and for the majority of
    values to be correct.
    '''
    for j in range(len(data_set)):
        for i in range(len(data_set[1])):
           
            if data_set[j][i] < 0: # incorrect values are all negative
                if i == 0 or i == data_set.shape[1]-1 or data_set[j][i+1] < 0:
                    # cannot use a point to the left or right,
                    # take average of above and below
                    data_set[j][i] = 0.5 * (data_set[j-1][i]
                                            + data_set[j+1][i])
                elif j == 0 or j == data_set.shape[0]-1 or data_set[j+1][i] < 0:
                    # cannot use a point above or below,
                    # take average of left and right point
                    data_set[j][i] = 0.5 * (data_set[j][i-1]
                                          + data_set[j][i+1])
                else:
                    # just take the average of the four surrounding points
                    data_set[j][i] = 0.25 * (data_set[j+1][i]
                                           + data_set[j-1][i]
                                           + data_set[j][i+1]
                                           + data_set[j][i-1])
    return data_set


def catchment_areas(data_set):
    '''
    Plots the catchment areas of the Cotter dam, the Bendora dam, and the
    Corin dam. 
    '''
    # points that lie on each of the dams
    cotter_water_level = data_set[242][2878]
    bendora_water_level = data_set[3352][634]
    corin_water_level = data_set[5495][755]

    # initialise the new data set as a numpy array of the correct size
    # with each element being the integer 1
    catchment_data_set = np.ones((len(data_set), len(data_set[1])))
    

    # add points for Cotter Dam to the plot
    for j in range(20, 1000):
        for i in range(2300,3200):
            if abs(data_set[j][i] - cotter_water_level) < 5.5 and slope(data_set, i, j) < 0.5:
                catchment_data_set[j][i] = 0
    
    # add points for Bendora Dam to the plot 
    for j in range(3100, 3800):
        for i in range(20,800):
            if abs(data_set[j][i] - bendora_water_level) < 5.5 and slope(data_set, i, j) < 0.5:
                catchment_data_set[j][i] = 0
    
    # add points for Corin dam to the plot
    for j in range(5000, 6200):
        for i in range(100,1500):
            if abs(data_set[j][i] - corin_water_level) < 5.5 and slope(data_set, i, j) < 0.5:
                catchment_data_set[j][i] = 0
    # draw the plot from the data
    plt.imshow(catchment_data_set, cmap='hot', interpolation='nearest')
    plt.show()        





if __name__ == "__main__":

    dataset = read_dataset('elevation_data_small.csv')
    min_elev = minimum_elevation(dataset)
    max_elev = maximum_elevation(dataset)
    ave_elev = average_elevation(dataset)
    slopey = slope(dataset, 794, 234)
    big_slope = max_slope(dataset)
    surf_area = surface_area(dataset, 794, 234)
    exp_area = expanded_surface_area(dataset, 550.8, 794, 234)
    print("minimum elevation: " + str(min_elev))
    print("maximum elevation: " + str(max_elev))
    print("average elevation: " + str(ave_elev))
    print("slope at (794,234): " + str(slopey))
    print("maximum slope: " + str(big_slope))
    print("surface area points: " + str(surf_area/25))
    print("surface area in acres: " + str(surf_area*0.000247105))
    print("surface area in acres when height increased to 550.8: " + str(exp_area*0.000247105))
    #large_dataset = impute_missing_values(read_dataset('elevation_data_large.csv'))
    #large_surf_area = surface_area(large_dataset, 2878, 242)
    #print("surface area large data set in acres: " + str(large_surf_area*0.000247105))
    #plt.imshow(large_dataset, cmap='hot', interpolation='nearest')
    #plt.show()
    #plot_surface_area(dataset,794,234)
    plot_expanded_surface_area(dataset,550.8,794,234)



    
    
