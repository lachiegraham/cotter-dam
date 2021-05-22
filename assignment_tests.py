"""
Test file for the COMP1730/COMP6730 major assignment,
Semester 1, 2021.

Please write all tests you develop in this file, and submit it
along with assignment_template.py

Please include the student IDs of all members of your group here
Student Ids: u7300179 and u7309735
"""
# maybe import unittest

import pytest
from assignment_template import *  # This will import all the functions from assignment_template.py


# something like this
# but with testing edge cases
def test_maximum():
    tests = (
        ([[1,2,3],[4,5,6],[7,8,9]], 9.0, 
        'maximum value is element [2][2], which has value 9'),
        ([[-8],[-15],[-99]], -8.0,
        'maximum value is element [0][0], which has value -8')
    )
    for data, correct, message in tests:
        result = maximum_elevation(data)
        assert abs(result - correct) < 1e-6, message


"""
this is some testing stuff from question 6
probably not going to be used but in the rare event
we can find a use for it it's here
"""
def how_many_problems_does_each_point_in_the_large_dataset_have(data_set):
    for j in range(len(data_set)):
        for i in range(len(data_set[1])):
            if data_set[j][i] < 0: # negative height is bad
                bad_value = 0 # the accumulator
                
                if i == 0: # edge or corner
                    bad_value += 1
                if j == 0: # edge or corner
                    bad_value += 1
                if i == data_set.shape[1]-1: # edge or corner
                    bad_value += 1
                if j == data_set.shape[0]-1: # edge or corner
                    bad_value += 1
                
                if j == data_set.shape[0]-1:
                    if data_set[j-1][i] < 0: # if we at bottom edge check above
                        bad_value += 1
                elif data_set[j+1][i] < 0: # point has bad neigbour below it
                    bad_value += 1
                
                if i == data_set.shape[1]-1:
                    if data_set[j][i-1] < 0: # if we at right edge check to the left
                        bad_value += 1
                elif data_set[j][i+1] < 0: # point has bad neighbour to its right
                    bad_value += 1
                
                if bad_value != 0:
                    # if it prints something other than 1, panic
                    print(bad_value)