import arcpy
from arcpy import env

input = arcpy.GetParameterAsText(0)

weedPoints = input+"_lyr"

arcpy.MakeFeatureLayer_management(input, weedPoints)
# FEATURES THAT HAVE A MONTH VALUE (NOT 00)
arcpy.SelectLayerByAttribute_management(weedPoints, "NEW_SELECTION", """ "Month" <> '00' """ )
arcpy.CalculateField_management(weedPoints,"date","""DateValue ( [Year] & "-"+[Month]+"-01")""","VB","#")
# FEATURES THAT DO NOT HAVE A MONTH VALUE (00)
arcpy.SelectLayerByAttribute_management(weedPoints, "SWITCH_SELECTION")
arcpy.CalculateField_management(weedPoints,"date","""DateValue ( [Year] & "-01-01")""","VB","#")
