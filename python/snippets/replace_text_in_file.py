import os, sys

filein = r"\\server-gis\data\PROJECTS\20160110_GPS_Data_Update\WORKING\GNSS Projects\PublicWorks\Documentation\_SUMMARY.txt"
f = open(filein,'r')
filedata = f.read()
f.close()

old_text = "\\server-gis\data"
new_text = r"\\server-gis\data"
newdata = filedata.replace(old_text,new_text)

f = open(filein,'w')
f.write(newdata)
f.close()