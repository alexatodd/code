import arcpy
mapdoc = arcpy.mapping.MapDocument("CURRENT")
mapdoc.findAndReplaceWorkspacePaths(r"G:\DATA\PRODUCTION\HR_PublicWorks.gdb" , r"G:\DATA\PUBLISH\HR_PublicWorks.gdb")
mapdoc.save()
del mapdoc