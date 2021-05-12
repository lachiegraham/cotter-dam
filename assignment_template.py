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

# I hope we are allowed to import stuff otherwise have to redo q1
# if can't then data = [line.split(',') for line in open(file)]
# or
# csvfile = open(file, "r")
# data = list(csv.reader(csvfile))
# csvfile.close()

# Question 1:
def read_dataset(file):
    data = np.genfromtxt(file, delimiter=',')
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
    elif x_coordinate == dataset.shape[1]-1: #Last Column.
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
    elif y_coordinate == dataset.shape[0]-1:   #Last row.
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
    return(math.sqrt((x_slope)**2+((y_slope)**2)))

# Question 4
def surface_area(data_set, x_coordinate, y_coordinate):
    pass


# Question 5:
def expanded_surface_area(data_set, water_level, x_coordinate, y_coordinate):
    pass


# Question 6:
def impute_missing_values(data_set):
    pass

# You'll need to decide what other functions you want for Question 6
# It should be clear from your code, what we need to do in order to produce the plot(s).


# Code in the following if statement will only be executed when this file is run - not when it is imported.
# If you want to use any of your functions (such as to answer questions) please write the code to
# do so inside this if statement. We'll cover it in more detail in an upcoming lecture.
if __name__ == "__main__":
    # these values will need to be tested, probably by opening the
    # csv file in excel and using it
    dataset = read_dataset('elevation_data_small.csv')
    min_elev = minimum_elevation(dataset)
    max_elev = maximum_elevation(dataset)
    ave_elev = average_elevation(dataset)
    slopey = slope(dataset, 100, 100)
    print("minimum elevation: " + str(min_elev))
    print("maximum elevation: " + str(max_elev))
    print("average elevation: " + str(ave_elev))
    print("slope at (100, 100): " + str(slopey))
    
    
    
