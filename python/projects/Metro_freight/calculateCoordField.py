#--------------------------------
# Name: Calculate NHPN Unique ID
# Purpose:
# Author: Alexa Todd @ Metro
# Created: 12/14/15
# ArcGIS Version: 10.1
# Python Version: 2.7
#--------------------------------
import os
import sys
import arcpy
from arcpy import env

#Environments
env.workspace = arcpy.GetParameterAsText(0) # Work Space #
env.overwriteOutput = True

##Declare Tool Variables
#Variables: Input
nhpn = arcpy.GetParameterAsText(1) # Input NHPN Dataset #
#coord_dict = {}

def calc_coords(in_data):
    #Calculates fields for the x or y coordinate of the 
    #start and end of the line, multiplied by 1,000 to make it
    #a 5-6 digit integer
#    fieldList = ["startx_long","starty_long","endx_long","endy_long"]
#    multValues = [-1000, 1000]

#    for f in fieldList:
#        if "x" in f:
            
             
#    xExp = "fieldListX*multValues[0]"
#    yExp = "!starty!*multValues[1]"
#    arcpy.CalculateField_management(nhpn, fieldListX, )
    xExpStart = "!startx! *-1000000"
    arcpy.CalculateField_management(in_data, "startx_long", xExpStart, "PYTHON")
    yExpStart = "!starty!*1000000"
    arcpy.CalculateField_management(in_data, "starty_long", yExpStart, "PYTHON")
    xExpEnd = "!endx! *-1000000"
    arcpy.CalculateField_management(in_data, "endx_long", xExpEnd, "PYTHON")
    yExpEnd = "!endy!*1000000"
    arcpy.CalculateField_management(in_data, "endy_long", yExpEnd, "PYTHON")

    
def create_UID(in_data):
    """Combines the first 5 digits of the x and y coordinate for
       the start and the end nodes of each link"""
    arcpy.AddField_management(in_data, "UID", "LONG")
    

##Define Main Function
def Main():
#    calc_coords(nhpn)
    create_UID(nhpn)

#Run Main Function
Main()