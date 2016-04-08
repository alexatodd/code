# source: https://docs.python.org/2/library/filecmp.html

import filecmp
from filecmp import dircmp

dir1 = r"M:\plan\drc\projects\16055_St_Johns_Consolidation\12107_StJohnsLandfill"
dir2 = r"M:\plan\drc\projects\16055_St_Johns_Consolidation\St_Johns_Landfill"
textfile = r"M:\plan\drc\projects\16055_St_Johns_Consolidation\compareDirs_log.txt"

def print_diff_files(dcmp):
	for name in dcmp.same_files:
		with open(textfile, 'a') as writeFile:
			print>>writeFile, "same_file %s found in %s and %s" % (name,dcmp.left,dcmp.right)
	# for name in dcmp.diff_files:
		# with open(textfile,'a') as writeFile:
			# print>>writeFile, "diff_file %s found in %s and %s" % (name,dcmp.left,dcmp.right)
	for sub_dcmp in dcmp.subdirs.values():
		print_diff_files(sub_dcmp)
		
dcmp = dircmp(dir1, dir2)
print_diff_files(dcmp)
