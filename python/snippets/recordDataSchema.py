

import arcpy, os
from arcpy import env
# TO RUN AS ARCMAP SCRIPT
ws = "I:/SHRP2-C20/Network/Workspace10.1/Data.gdb/"

arcpy.env.workspace = ws
arcpy.env.overwriteOutput = True

NHPN = "NHPNLine_Select"
SWIM = "SWIM_link_Select"
Natl = "NationalHighwayNet"

txtFile = r"J:\todda\FreightNetwork\FREIGHTDATA.txt"


def listUniqueValues(feat_class):
	with open(txtFile,'a') as writeFile:
		tempT = 'tempfcTable'
		fc = feat_class
		counter = 0
		# fclyr = "fclyr"
		print>>writeFile,"\n"+fc+"\n-----------------------------"
		# arcpy.MakeFeatureLayer_management(fc,fclyr)
		arcpy.MakeTableView_management(fc, tempT)
		fieldlist = arcpy.ListFields(tempT)
		for field in fieldlist:
			counter +=1
			if len(field.name) > 8:
				print>>writeFile,str(counter)+")	Field: "+field.name+"	Type: "+field.type
			else:
				print>>writeFile,str(counter)+")	Field: "+field.name+"		Type: "+field.type
	del tempT

listUniqueValues(Natl)
listUniqueValues(NHPN)
listUniqueValues(SWIM)


"""Input data to the Metro Freight Network includes: 

-- National Network from RSG (NationalHighwayNet)
-- NHPN (NHPNLine_Select)
-- SWIM (SWIM_link_Select)

These data table fields are outlined below:
"""