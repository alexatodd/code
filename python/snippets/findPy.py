import sys
import platform
import imp

"""If you don’t know where it is, you can discover its location; 
copy and paste the following code into a new Python script then execute the script. 
The script will print the location of python.exe 
as well as other information about your Python environment."""

print("Python EXE     : " + sys.executable)
print("Architecture   : " + platform.architecture()[0])
print("Path to arcpy  : " + imp.find_module("arcpy")[1])
 
raw_input("\n\nPress ENTER to quit")