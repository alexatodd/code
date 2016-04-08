#-----------------------------------------------------------------------------------------------------------
# File Name Insert
# Script written by Rocky Rudolph - April, 2006 - Channel Islands National Park, California
# Purpose: for creating a field called "FILENAME" and attaching the filename of the shapefile to each entry 
#   in the attribute table. Use with as many shapefiles within a specified directory.
#   Useful when picking apart shapefile entries and combining into a separate file to
#   maintain a breadcrumb trail of the original shapefile name.  
#
# Run file within a directory containing all the shapfiles needing modification
# Make sure FILENAME field doesn't already exist in any of the shapefiles
#
#-----------------------------------------------------------------------------------------------------------

#import relevant modules, create geoprocessing dispatch object
import win32com.client, sys, string, os

gp = win32com.client.Dispatch("esriGeoprocessing.gpDispatch.1")

# Remember to change this to wherever your shapefiles are stored
gp.workspace = "C:\\temp\\path"

try:
    fcs = gp.ListFeatureClasses("*", "all")
    fcs.reset()
    fc = fcs.Next()

    while fc:
        # Create the new field
        gp.AddField_management (fc, "FILENAME", "text", "", "", "50")

        # Apply the filename to all entries       
        gp.CalculateField_management (fc, "FILENAME", '"' + fc + '"')
        fc = fcs.Next()

except:
	print gp.GetMessages ()