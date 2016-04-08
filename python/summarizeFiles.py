# ---------------------------------------------------------------------------
# summarizeFiles.py
# Created on: 2016-03-25
# Created by: Alexa Todd
# Usage: summarize all the data files in the GNSS project file 
# Description: 
# ---------------------------------------------------------------------------

# IMPORT ARCPY MODULE
import arcpy, os, time
# from filecmp import dircmp
from arcpy import env

workspace = ws = r"G:\DATA\WORKING\UPDATED"
arcpy.env.workspace = ws
arcpy.env.overwriteOutput = True
# CONSTANTS ------------------------
directory = r"G:\PROJECTS\20160110_GPS_Data_Update\WORKING\GNSS Projects\PublicWorks"
export_dir = directory+"\Export"
correct_dir = directory+"\Corrected"
summary_file = directory+"\Documentation\_SUMMARY.txt"
# exports_file = directory+"\Documentation\EXPORTS.txt"

# LOCAL VARIABLES:
date = (time.strftime("%Y/%m/%d"))
# DEFINE FUNCTIONS:
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
			print>>writeFile,date+" new "+wild+" files\n"
			lines = set(l.strip() for l in readFile)
			for line in lines:
				print line
			for item in file_list:
				print item
				if str(item) in lines:
					print item+" is already in "+summary_file
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
			name = short.replace("\\","-")
			arcpy.CopyFeatures_management(shp,name[:-4])

try:
	print "Summarizing updated (.ssf), corrected (.cor), and exported (.shp) data files in "+directory+".\n"
	# Add new imported Trimble files to summary_file
	processNewFiles(directory,".SSF")
	# Add new corrected filed to summary_file
	processNewFiles(correct_dir,".cor")
	# Add new exported files to summary_file and copy to DATA\WORKING\UPDATED
	processNewFiles(export_dir,".shp")
finally:
	print "Success!"
