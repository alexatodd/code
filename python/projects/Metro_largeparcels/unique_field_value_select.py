# MODIFIED FROM:
'''
Created on Nov 19, 2013
@author: mosteele
'''


import arcpy, os
# TO RUN AS ARCMAP SCRIPT
fc = arcpy.GetParameterAsText(0)
# TO RUN IN OS
# fc = r'C:\Users\todda\Documents\ArcGIS\Default.gdb\Large_parcels_adjacent_pub_l'
fieldsToPrintList = ["OWNER1", "OWNERADDR"]
# large_parcels_union = fc
owner_id = 0
owner_id_field = "Owner_ID"
arcpy.MakeTableView_management(fc, 'tempfcTable')

# outFile = r'C:\Users\todda\Documents\ArcGIS\unique_values_in_owner_address_fields.txt'
owner_list = []
address_list = []
o_count = 0
a_count = 0
# with open(outFile,'w') as w:
fieldList = arcpy.ListFields('tempfcTable')
print "Creating owner list..."
arcpy.AddMessage("Creating owner list...")
for field in fieldList:
	if field.name == fieldsToPrintList[0]:
		values = [row[0] for row in arcpy.da.SearchCursor('tempfcTable', field.name)]
		uniqueValues = set(values)
		for aValue in uniqueValues:
			# print aValue
			# if field.name == fieldsToPrintList[0]:
			owner_list.append(aValue)
			# if field.name == fieldsToPrintList[1]:
				# address_list.append(aValue)
				# w.write ( field.name + '\t' + '\t'.join(str(x) for x in uniqueValues) + '\n' )
for item in owner_list:
	o_count += 1
total_items = str(o_count)
print "There are "+total_items+" listed owners."
arcpy.AddMessage("There are "+total_items+" listed owners.")
fc_lyr = arcpy.MakeFeatureLayer_management(fc,"fc_lyr")
fc1 = arcpy.MakeFeatureLayer_management(fc,"fc_a_lyr")
fc2 = arcpy.MakeFeatureLayer_management(fc,"fc_o_lyr")
count = 0
count2 = 0
# SELECT BY OWNER (ONE AT A TIME AS A LOOP)
for owner in owner_list:
	count += 1
	print ""
	print str(count) + "/"+ total_items+". "+owner
	arcpy.AddMessage(str(count) + "/"+ total_items+". "+owner)
	a_list = []
	o_list = []
	if len(owner) > 1:
		# print owner + ", "+str(len(owner))
		try:
			arcpy.SelectLayerByAttribute_management(fc_lyr,"NEW_SELECTION", """"OWNER1" = '"""+str(owner)+"""'""")
		# arcpy.Get
		# if owner_id_field == 0: # !!!! Need to fix this and add a true/false statement to find out if the field is null - this will prevent the owner_id from changing for each additional value in the owner_list
			ownerids = [row[0] for row in arcpy.da.SearchCursor(fc_lyr,owner_id_field)]
			uniqueIds = set(ownerids)
			for anId in uniqueIds:
				# print anId
				if anId == 0:
				# GET UNIQUE ADDRESSES FOR THE SELECTED FEATURES
					addresses = [row[0] for row in arcpy.da.SearchCursor(fc_lyr, "OWNERADDR")]
					uniqueAddesses = set(addresses)
					for anAddress in uniqueAddesses:
						a_list.append(anAddress)
					for a in a_list:
						print "selecting taxlots by address: "+str(a)
						arcpy.AddMessage("selecting taxlots by address: "+str(a))
						if len(a) > 1:
							arcpy.SelectLayerByAttribute_management(fc_lyr,"ADD_TO_SELECTION", """"OWNERADDR" = '"""+a+"""'""")
							owners = [row[0] for row in arcpy.da.SearchCursor(fc_lyr, "OWNER1")]
							uniqueOwners = set(owners)
							for anOwner in uniqueOwners:
								if len(anOwner) > 1:
									o_list.append(anOwner)
							for o in o_list:
								print "selecting taxlots by owner: "+str(o)
								arcpy.AddMessage("selecting taxlots by owner: "+str(o))
								try:
									arcpy.SelectLayerByAttribute_management(fc_lyr,"ADD_TO_SELECTION", """"OWNER1" = '"""+str(o)+"""'""")
								except:
									edit = owner.replace("\'","\\\'")
									# elif "\&" in owner:
									edit = edit.replace("\&", "\\\&")
									print edit
									truncate = edit[:-6]
									print truncate
									arcpy.SelectLayerByAttribute_management(fc_lyr,"NEW_SELECTION",""""OWNER1" LIKE '"""+truncate+"""%'""")
					owner_id += 1
					arcpy.CalculateField_management(fc_lyr, owner_id_field, owner_id)
					print "Owner ID is: "+str(owner_id)
					arcpy.AddMessage("Owner ID is: "+str(owner_id))
				else:
					print "Owner ID is: "+str(anId)
					arcpy.AddMessage("Owner ID is: "+str(anId))
		except:
			print "Cannot query owner."
			arcpy.AddMessage("Cannot query owner.")
			pass
arcpy.SelectLayerByAttribute_management(fc_lyr,"NEW_SELECTION", """"Owner_ID" = 0""")
arcpy.MakeFeatureLayer_management(fc_lyr, "fc_lyr_temp")
fieldList = arcpy.ListFields("fc_lyr_temp")
print "\n Creating address list..."
arcpy.AddMessage("\n Creating address list...")
for field in fieldList:
	if field.name == fieldsToPrintList[1]:
		values = [row[0] for row in arcpy.da.SearchCursor("fc_lyr_temp", field.name)]
		uniqueValues = set(values)
		for aValue in uniqueValues:
			# print aValue
			# if field.name == fieldsToPrintList[0]:
			address_list.append(aValue)
			# if field.name == fieldsToPrintList[1]:
				# address_list.append(aValue)
				# w.write ( field.name + '\t' + '\t'.join(str(x) for x in uniqueValues) + '\n' )
for item in address_list:
	a_count += 1
total_a = str(a_count)
print "There are "+total_a+" listed addresses without an owner name."
arcpy.AddMessage("There are "+total_a+" listed addresses without an owner name.")
for address in address_list:
	count2 += 1
	print ""
	print str(count2) + "/"+ total_a+". "+address
	arcpy.AddMessage(str(count2) + "/"+ total_a+". "+address)
	if len(address) > 1:
		# print owner + ", "+str(len(owner))
		try:
			arcpy.SelectLayerByAttribute_management("fc_lyr_temp","NEW_SELECTION", """"OWNERADDR" = '"""+str(address)+"""'""")
			owner_id += 1
			arcpy.CalculateField_management("fc_lyr_temp", owner_id_field, owner_id)
			print "Owner ID is: "+ str(owner_id)
			arcpy.AddMessage("Owner ID is: "+ str(owner_id))
		except:
			print "Cannot query address."
			arcpy.AddMessage("Cannot query address.")
			pass
print "Completed."
del owner_list, address_list


