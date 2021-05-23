"""
Test file for the COMP1730/COMP6730 major assignment,
Semester 1, 2021.

Please write all tests you develop in this file, and submit it
along with assignment_template.py

Please include the student IDs of all members of your group here
Student Ids: u7300179 and u7309735
"""
# maybe import unittest

import sys
import pytest
from assignment_template import *




def test_minimum():
    tests = (
        ([[1,2,3],[4,5,6],[7,8,9]], 1, 
        'Minimum value is element [0][0], which has value 1'),
        ([[-8],[-15],[-99]], -99,
        'Minimum value is element [2][0], which has value -99'),
        ([[1]], 1,
        'Maximum value is element [0][0], which has value 1')
    )
    for data, correct, message in tests:
        result = minimum_elevation(data)
        assert abs(result - correct) < 1e-6, message  


def test_maximum():
    tests = (
        ([[1,2,3],[4,5,6],[7,8,9]], 9.0, 
        'Maximum value is element [2][2], which has value 9'),
        ([[-8],[-15],[-99]], -8.0,
        'Maximum value is element [0][0], which has value -8'),
        ([[1]], 1,
        'Maximum value is element [0][0], which has value 1')
    )
    for data, correct, message in tests:
        result = maximum_elevation(data)
        assert abs(result - correct) < 1e-6, message


def test_average():
    tests = (
        ([[1,2,3],[4,5,6],[7,8,9]], 5.0, 
        'Average value is 5'),
        ([[-8],[-15],[-99]], (-122/3),
        'Average value is (-122/3)'),
        ([[1]], 1,
        'Average value is element [0][0], which has value 1')
    )
    for data, correct, message in tests:
        result = average_elevation(data)
        assert abs(result - correct) < 1e-6, message
        
        
def test_slope():
    tests = (
        ([[1,2,3],[4,5,6],[7,8,9]], 1, 1, math.sqrt(10)/5,
        'Sample data set. Correct calculated by hand to be sqrt10 over 5.'),
        (read_dataset('elevation_data_small.csv'), 0, 0, 0.2657204546134851,
        'Edge case for when the first point in data is chosen. Correct calculated by hand.'),
        (read_dataset('elevation_data_small.csv'), 794, 234, 0.0008062257748234812,
        'Slope when on dam. Correct calculated by hand.'),
        (read_dataset('elevation_data_small.csv'), 1188, 882, 0.37737986167784465,
        'Edge case for when the last point in data is chosen. Correct calculated by hand.')
        
    )
    for data, x_coord, y_coord, correct, message in tests:
        result = slope(data, x_coord, y_coord)
        assert abs(result - correct) < 1e-6, message
        
def test_flatness():
    tests = (
        (read_dataset('elevation_data_small.csv'), 794, 234, True,
        'Surface of dam should return flat.'),
        (read_dataset('elevation_data_small.csv'), 0, 0, False,
        'Edge case for first point in data, not flat.'),
        (read_dataset('elevation_data_small.csv'), 1188, 882, False,
        'Edge case for last point in data, not flat.')
        
    )
    for data, x_coord, y_coord, correct, message in tests:
        result = is_flat(data, x_coord, y_coord)
        assert result == correct, message
        
        
def test_surface_area():
    tests = (
       ([[10,20,1,30,40],[220,66,1,301,123],[1,1,1,1,1],[44,55,1,66,77],[70,70,1,90,90]], 2, 2, 25,
        'Only the 1 in the very centre would be considered part of the dam as it is surrounded by other 1s'),
        ([[10,50,30],[33,77,199],[70,1,90]], 1, 1, 0,
        'Edge case where none would be considered part of dam so return 0')
    )
    for data, x_coord, y_coord, correct, message in tests:
        result = surface_area(data, x_coord, y_coord)
        assert abs(result - correct) < 1e-6, message
        
def test_surface_area2():
    tests = (
        
        (read_dataset('elevation_data_small.csv'), 794, 234, 700,
        'Online resources suggest a surface area of 700 acres for the Cotter dam.'),
        
    )
    for data, x_coord, y_coord, correct, message in tests:
        result = surface_area(data, x_coord, y_coord)
        assert abs(result*0.000247105 - correct) < 100, message
        
def test_expanded_area():
    tests = (
        (read_dataset('elevation_data_small.csv'), -1000, 794, 234, 3172825,
        'Edge case for when elevation is decreased, should return normal surface area with no changes.'),
        (read_dataset('elevation_data_small.csv'), 550, 794, 234, 3172825,
        'When elevation is increased should return a greater surface area than normal.')
        
    )
    for data, elevation, x_coord, y_coord, correct, message in tests:
        result = expanded_surface_area(data, elevation, x_coord, y_coord)
        assert abs(result - correct) < 1e-6 or result - correct >0, message

        


           
                    
                    
if __name__ == '__main__':
    pytest.main(sys.argv)