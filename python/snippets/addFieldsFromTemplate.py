import arcpy
from arcpy import env
# arcpy.env.workspace = 
arcpy.env.overwriteOutput = True

prod_fc = r"G:\DATA\PRODUCTION\HR_PublicWorks.gdb\SEWER\sewer_points"
update_shp = r"G:\DATA\WORKING\UPDATED\sewer_po_NAD83.shp"
prod_fields = arcpy.ListFields(prod_fc)
fields = arcpy.ListFields(update_shp)
new_fields = []
for field in fields:
	if field not in prod_fields:
		new_fields.append(field)
for field in new_fields:
	name = field.name
	type = field.type
	print name, type
	if type == "String":
		type = "TEXT"
	if type == "SmallInteger":
		type = "SHORT"
	if type.upper() in ["DATE","BLOB","TEXT","FLOAT","DOUBLE","SHORT","LONG","RASTER","GUID"]:
		arcpy.AddField_management(prod_fc,name,type)