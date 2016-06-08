# ---------------------------------------------------------------------------
# summarizeFiles.py
# Completed: 2016-05-25
# Created by: Alexa Todd
# Usage: Summarize and process exported GPS data
# Description: 
# ---------------------------------------------------------------------------

# IMPORT ARCPY MODULE
import arcpy, os, time, sys, ntpath
# from filecmp import dircmp
from arcpy import env

workspace = ws = r"\\server-gis\data\DATA\WORKING\UPDATED"
arcpy.env.workspace = ws
arcpy.env.overwriteOutput = True
# CONSTANTS ------------------------
directory = r"\\server-gis\data\PROJECTS\20160110_GPS_Data_Update\WORKING\GNSS Projects\PublicWorks"
export_dir = directory+"\Export"
correct_dir = directory+"\Corrected"
summary_file = directory+"\Documentation\_SUMMARY.txt"

# LOCAL VARIABLES:
date = (time.strftime("%Y/%m/%d"))
date2 = (time.strftime("%Y%m%d"))

# DEFINE FUNCTIONS:
def addProjection(input_data):
	print "\nAdding projection to:	%s..." % input_data
	# sys.exit()
	current_ws = os.path.dirname(os.path.realpath(input_data))
	arcpy.env.workspace = current_ws
	input_coordsys = "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]"
	output_coordsys = "PROJCS['NAD_1983_HARN_StatePlane_Oregon_North_FIPS_3601_Feet_Intl',GEOGCS['GCS_North_American_1983_HARN',DATUM['D_North_American_1983_HARN',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',8202099.737532808],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-120.5],PARAMETER['Standard_Parallel_1',44.33333333333334],PARAMETER['Standard_Parallel_2',46.0],PARAMETER['Latitude_Of_Origin',43.66666666666666],UNIT['Foot',0.3048]]"
	tmethod = "WGS_1984_(ITRF00)_To_NAD_1983_HARN"
	transform_from = input_coordsys
	name = input_data.replace(current_ws,"")
	output_data = current_ws+"""\\APPEND"""+name[:-4]+"_NAD83"
	print "\tAppend data:	{:s}".format(output_data)
	arcpy.AddMessage(output_data)
	# Process: Define Projection
	arcpy.DefineProjection_management(input_data, input_coordsys)
	# Process: Project
	arcpy.Project_management(input_data, output_data, output_coordsys, tmethod, transform_from)
	return output_data
def processNewFiles(dir,wild):
	# ADDS NEW FILES TO SUMMARY TEXT FILE AND (IF .SHP) COPIES TO WORKING DATA FOLDER
	counter = 0
	count = 0
	file_list = []
	for root, dirs, files, in os.walk(dir):
		for file in files:
			if file.endswith(wild):
				count += 1
				full = (os.path.join(root,file))
				file_list.append(full)
	new_files = []
	with open(summary_file,'a') as writeFile:
		with open(summary_file,'r') as readFile:
			print>>writeFile,"New "+wild+" files\n"
			lines = set(l.strip() for l in readFile)
			for item in file_list:
				if str(item) in lines:
					pass
				else:
					counter += 1
					new_files.append(item)
					print>>writeFile, item
			print>>writeFile,"\nAdded "+str(counter)+" new "+wild+" files"
			print>>writeFile,"Total "+wild+" files = "+str(count)+"\n----------------------------------------\n"
		readFile.close()
	writeFile.close()
	if wild == ".shp":
		for shp in new_files:
			short = shp.replace(export_dir,"")
			name = short.replace("\\","")
			folder = name[8:-4]
			# arcpy.env.workspace = ws+"\\"+folder
			arcpy.CopyFeatures_management(shp,ws+"\\"+folder+"\\"+name[:-4])
def mergeNewShp():
	print "\nMerging new shapefiles (updated data) and adding projection..."
	# folders = os.listdir(ws)
	folders = [ name for name in os.listdir(ws) if os.path.isdir(os.path.join(ws, name)) ]
	for folder in folders:
		new_ws = ws+"\\"+folder
		merge_data = folder+"_merge_"+date2
		print "\n\tCurrent folder:	{:s}".format(folder)
		print "\tNew workspace:	{:s}".format(new_ws)
		# sys.exit()
		arcpy.env.workspace = new_ws
		files = []
		for file in os.listdir(new_ws):
			if file.endswith(".shp"):
				files.append(file)
		if len(files) > 1:
			print "\tMerging {:n} shapefiles:	{:s}...".format(len(files),files)
			arcpy.Merge_management(files,merge_data)
			print "\t\tName of merged data:	{:s}".format(merge_data)
			for file in files:
				arcpy.CopyFeatures_management(file,new_ws+"""\\DONE\\"""+file)
				arcpy.Delete_management(file)
			merged_data = new_ws+"\\"+merge_data+".shp"
			addProjection(merged_data)
			arcpy.CopyFeatures_management(merged_data,new_ws+"""\\DONE\\"""+merge_data)
			arcpy.Delete_management(merged_data)
		else:
			print "\tNo new shapefiles in {:s}.".format(new_ws)
def appendData():
	with open(summary_file,'a') as writeFile:
		folders = [ name for name in os.listdir(ws) if os.path.isdir(os.path.join(ws, name)) ]
		for folder in folders:
			append_ws = ws+"\\"+folder+"\\APPEND"
			# arcpy.env.workspace = append_ws
			file_list = []
			append_count = 0
			for root, dirs, files, in os.walk(append_ws):
				for file in files:
					if file.endswith(".shp"):
						append_count += 1
						full = (os.path.join(root,file))
						file_list.append(full)
			if append_count:
				try:
					arcpy.Append_management(file_list,ws+"\\"+folder+".shp","NO_TEST")
					print>>writeFile, "Appended %s files to %s:" % (append_count,ws+"\\"+folder+".shp")
				# elif len(file_list) > 1:
					# arcpy.Merge_management(file_list,ws+"\\"+folder+".shp")
				except Exception as e:
					print>> writeFile, "!Error: %s" % e
					arcpy.Merge_management(file_list,ws+"\\"+folder+".shp")
					print>> writeFile, "New shapefile added to UPDATED folder: "+ws+"\\"+folder+".shp"		
			for file in file_list:
				print>>writeFile, file
				head, tail = ntpath.split(file)
				arcpy.CopyFeatures_management(file,ws+"\\"+folder+"\\DONE\\"+tail)
				arcpy.Delete_management(file)
	writeFile.close()
try:
	# print "Summarizing updated (.ssf), corrected (.cor), and exported (.shp) data files in "+directory+".\n"
	with open(summary_file,'a') as writeFile:
		print>>writeFile,"\n***************************************************************************\n" +date+"\n***************************************************************************" 
	writeFile.close()
	# Add new imported Trimble files to summary_file
	processNewFiles(directory,".SSF")
	# Add new corrected filed to summary_file
	processNewFiles(correct_dir,".cor")
	# Add new exported files to summary_file and copy to DATA\WORKING\UPDATED
	processNewFiles(export_dir,".shp")
	mergeNewShp()
	appendData()
except Exception as e:
	with open(summary_file,'a') as writeFile:
		print>>writeFile, "Error: %s" % e
	writeFile.close()
	sys.exit()
finally:
	with open(summary_file,'a') as writeFile:
		print>>writeFile, "Successfully processed new data!"
	writeFile.close()
	

