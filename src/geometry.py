'''

Created on Feb 1, 2013

@author: Aria
'''

import math
import copy

#===============================================================================
# Class Point
#
# Defines the Point class which consists of two values
# representing an x and y coordinate.
#===============================================================================
class Point():
    def __init__(self, point_x, point_y):
        self.x = point_x
        self.y = point_y
        
#===============================================================================
# Class Rectangle
# 
# Defines the Rectangle class which consists of one point
# value, and two additional values defining the width and height
# of the rectangle from the point origin in the lower left corner
#===============================================================================
class Rectangle():
    def __init__(self, corner, width, height):
        self.corner = corner
        self.width = width
        self.height = height

#===============================================================================
# Function move_rectangle
# 
# Takes one rectangle and two numeric values representing
# new x and y coordinates for the rectangles corner Point object        
#===============================================================================
def move_rectangle(rect, x, y):
    rect.corner.x = x
    rect.corner.y = y
    
#===============================================================================
# Function move_new_rectangle
# 
# Takes one rectangle and two numeric values representing
# x and y coordinates for the rectangles corner Point object
# and returns a new rectangle with provided coordinates        
#===============================================================================
def move_new_rectangle(rect, x, y):
    rect = copy.deepcopy(rect)
    rect.corner.x = x
    rect.corner.y = y
    return rect
    
#===============================================================================
# Function distance_between_points
# 
# Takes two Point objects and returns a tuple containing 
# the absolute value distance between each
#===============================================================================
def distance_between_points(point_a, point_b):
    return (find_difference(point_a.x, point_b.x), find_difference(point_a.y, point_b.y))

#===============================================================================
# Function find_difference
# 
# Takes the x or y coordinates of two points,
# compares them, and returns the absolute value
# difference between them.    
#===============================================================================
def find_difference(point_x, point_y):
    point_x = math.fabs(point_x)
    point_y = math.fabs(point_y)
    
    if point_x > point_y:
        return point_x - point_y
    elif point_y > point_x:
        return point_y - point_x
    else:
        return 0;


#===============================================================================
# Main
#===============================================================================
some_point_a = Point(10, 15)    
some_point_b = Point(15, 25)
print "some_point_a = Point(10, 15)  "
print "some_point_b = Point(15, 25)"
print "distance_between_points(some_point_a, some_point_b)"
print distance_between_points(some_point_a, some_point_b)
print ""

some_rectangle_a = Rectangle(some_point_a, 10, 20)
print "some_rectangle_a = Rectangle(some_point_a, 10, 20)"
print "some_rectangle_a.corner.x"
print some_rectangle_a.corner.x
print "some_rectangle_a.corner.y"
print some_rectangle_a.corner.y
print "some_rectangle_a.width"
print some_rectangle_a.width
print "some_rectangle_a.height"
print some_rectangle_a.height
print ""

move_rectangle(some_rectangle_a, 20, 40)
print "move_rectangle(some_rectangle_a, 20, 40)"
print "some_rectangle_a.corner.x"
print some_rectangle_a.corner.x
print "some_rectangle_a.corner.y"
print some_rectangle_a.corner.y
print ""

some_rectangle_b = move_new_rectangle(some_rectangle_a, 100, 100)
print "some_rectangle_b = move_new_rectangle(some_rectangle_a, 100, 100)"
print "some_rectangle_a.corner.x"
print some_rectangle_a.corner.x
print "some_rectangle_a.corner.y"
print some_rectangle_a.corner.y
print "some_rectangle_b.corner.x"
print some_rectangle_b.corner.x
print "some_rectangle_b.corner.y"
print some_rectangle_b.corner.y
print ""