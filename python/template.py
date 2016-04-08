#--------------------------------
# Name: 
# Purpose:
# Author: Alexa Todd @ Metro
# Created: 
# ArcGIS Version: 10.1
# Python Version: 2.7
#--------------------------------
import os
import sys
import arcpy

def do_analysis(*argv):
    """TODO: Add documentation about this function here"""
    try:
        #TODO: Add analysis here
        pass
    except arcpy.ExecuteError:
        print arcpy.GetMessages(2)
    except Exception as e:
        print e.args[0]
#End do_analysis function

#This test allows the script to be used from the operating
#system commmand prompt (stand-alone), in a Python IDE,
#as a geoprocessing script tool, or as a module imported in
#another script
if __name__ == '__main__':
    #Arguments are optional
    argv = tuple(arcpy.GetParameterAsText(i)
                 for i in range(arcpy.GetArgumentCount())
    do_analysis(*argv)