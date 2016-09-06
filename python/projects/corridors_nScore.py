import arcpy
from arcpy import env

workspace = ws = arcpy.GetParameterAsText(0)
scratch = arcpy.GetParameterAsText(1)
crashes = arcpy.GetParameterAsText(2)
corridors = arcpy.GetParameterAsText(3)

arcpy.env.workspace = ws
arcpy.env.overwriteOutput = True

# Source data:
study_area = r"K:\boundary\metropolitan_planning_area.lyr"

# Output:
crashes_copy		= "crashes_2010_2014"
corridor_crashes	= scratch+"\\corridor_crashes_2010_2014"
corridor_crashes_count = "corridors_2010_2014"

v = "VISIBLE"
h = "HIDDEN"
crash_fields		=	"OBJECTID OBJECTID "+v+" NONE;\
						Shape Shape "+v+" NONE;\
						CRASH_DT CRASH_DT "+v+" NONE;\
						CRASH_ID CRASH_ID "+v+" NONE;\
						CRASH_TYP_CD CRASH_TYP_CD "+v+" NONE;\
						CRASH_TYP_LONG_DESC CRASH_TYP_LONG_DESC "+v+" NONE;\
						CRASH_SVRTY_CD CRASH_SVRTY_CD "+v+" NONE;\
						CRASH_SVRTY_LONG_DESC CRASH_SVRTY_LONG_DESC "+v+" NONE;\
						AutoInj_Cnt AutoInj_Cnt "+v+" NONE;\
						Auto_FA Auto_FA "+v+" NONE;\
						Auto_BC Auto_BC "+v+" NONE;\
						Ped_FA Ped_FA "+v+" NONE;\
						Ped_BC Ped_BC "+v+" NONE;\
						Bike_FA Bike_FA "+v+" NONE;\
						Bike_BC Bike_BC "+v+" NONE;\
						Ped_PDO Ped_PDO "+v+" NONE;\
						Bike_PDO Bike_PDO "+v+" NONE;\
						\
						TOT_VHCL_CNT TOT_VHCL_CNT "+h+" NONE;\
						TOT_FATAL_CNT TOT_FATAL_CNT "+v+" NONE;\
						TOT_INJ_LVL_A_CNT TOT_INJ_LVL_A_CNT "+v+" NONE;\
						TOT_INJ_LVL_B_CNT TOT_INJ_LVL_B_CNT "+h+" NONE;\
						TOT_INJ_LVL_C_CNT TOT_INJ_LVL_C_CNT "+h+" NONE;\
						TOT_INJ_CNT TOT_INJ_CNT "+v+" NONE;\
						TOT_UNINJD_AGE00_04_CNT TOT_UNINJD_AGE00_04_CNT "+h+" NONE;\
						TOT_OCCUP_CNT TOT_OCCUP_CNT "+h+" NONE;\
						TOT_UNINJD_PER_CNT TOT_UNINJD_PER_CNT "+h+" NONE;\
						TOT_PED_CNT TOT_PED_CNT "+h+" NONE;\
						TOT_PED_FATAL_CNT TOT_PED_FATAL_CNT "+h+" NONE;\
						TOT_PED_INJ_CNT TOT_PED_INJ_CNT "+h+" NONE;\
						TOT_PEDCYCL_CNT TOT_PEDCYCL_CNT "+h+" NONE;\
						TOT_PEDCYCL_FATAL_CNT TOT_PEDCYCL_FATAL_CNT "+h+" NONE;\
						TOT_PEDCYCL_INJ_CNT TOT_PEDCYCL_INJ_CNT "+h+" NONE;\
						TOT_UNKNWN_CNT TOT_UNKNWN_CNT "+h+" NONE;\
						TOT_UNKNWN_FATAL_CNT TOT_UNKNWN_FATAL_CNT "+h+" NONE;\
						TOT_UNKNWN_INJ_CNT TOT_UNKNWN_INJ_CNT "+h+" NONE;\
						TOT_PER_INVLV_CNT TOT_PER_INVLV_CNT "+h+" NONE;\
						\
						CRASH_HR_NO CRASH_HR_NO "+h+" NONE;\
						CRASH_HR_LONG_DESC CRASH_HR_LONG_DESC "+h+" NONE;\
						CNTY_ID CNTY_ID "+h+" NONE;\
						CNTY_NM CNTY_NM "+h+" NONE;\
						CITY_SECT_ID CITY_SECT_ID "+h+" NONE;\
						CITY_SECT_NM CITY_SECT_NM "+h+" NONE;\
						URB_AREA_CD URB_AREA_CD "+h+" NONE;\
						URB_AREA_LONG_NM URB_AREA_LONG_NM "+h+" NONE;\
						FC_CD FC_CD "+h+" NONE;\
						FC_DESC FC_DESC "+h+" NONE;\
						NHS_FLG NHS_FLG "+h+" NONE;\
						RTE_ID RTE_ID "+h+" NONE;\
						RTE_NM RTE_NM "+h+" NONE;\
						RTE_TYP_CD RTE_TYP_CD "+h+" NONE;\
						HWY_NO HWY_NO "+h+" NONE;\
						HWY_MED_NM HWY_MED_NM "+h+" NONE;\
						HWY_SFX_NO HWY_SFX_NO "+h+" NONE;\
						RDWY_NO RDWY_NO "+h+" NONE;\
						HWY_COMPNT_CD HWY_COMPNT_CD "+h+" NONE;\
						HWY_COMPNT_LONG_DESC HWY_COMPNT_LONG_DESC "+h+" NONE;\
						MLGE_TYP_CD MLGE_TYP_CD "+h+" NONE;\
						MLGE_TYP_LONG_DESC MLGE_TYP_LONG_DESC "+h+" NONE;\
						RD_CON_NO RD_CON_NO "+h+" NONE;\MP_NO MP_NO "+h+" NONE;\
						LRS_VAL LRS_VAL "+h+" NONE;\
						LAT_DEG_NO LAT_DEG_NO "+h+" NONE;\
						LAT_MINUTE_NO LAT_MINUTE_NO "+h+" NONE;\
						LAT_SEC_NO LAT_SEC_NO "+h+" NONE;\
						LONGTD_DEG_NO LONGTD_DEG_NO "+h+" NONE;\
						LONGTD_MINUTE_NO LONGTD_MINUTE_NO "+h+" NONE;\
						LONGTD_SEC_NO LONGTD_SEC_NO "+h+" NONE;\
						LAT_DD LAT_DD "+h+" NONE;\
						LONGTD_DD LONGTD_DD "+h+" NONE;\
						SEG_MRK_ID SEG_MRK_ID "+h+" NONE;\
						SEG_PT_LRS_MEAS SEG_PT_LRS_MEAS "+h+" NONE;\
						UNLOCT_FLG UNLOCT_FLG "+v+" NONE;\
						SPECL_JRSDCT_ID SPECL_JRSDCT_ID "+h+" NONE;\
						SPECL_JRSDCT_LONG_DESC SPECL_JRSDCT_LONG_DESC "+h+" NONE;\
						RECRE_RD_NM RECRE_RD_NM "+h+" NONE;\
						ISECT_RECRE_RD_NM ISECT_RECRE_RD_NM "+h+" NONE;\
						AGY_ST_NO AGY_ST_NO "+h+" NONE;\
						ST_FULL_NM ST_FULL_NM "+h+" NONE;\
						ISECT_AGY_ST_NO ISECT_AGY_ST_NO "+h+" NONE;\
						ISECT_ST_FULL_NM ISECT_ST_FULL_NM "+h+" NONE;\
						ISECT_SEQ_NO ISECT_SEQ_NO "+h+" NONE;\
						FROM_ISECT_DSTNC_QTY FROM_ISECT_DSTNC_QTY "+h+" NONE;\
						CMPSS_DIR_CD CMPSS_DIR_CD "+h+" NONE;\
						CMPSS_DIR_SHORT_DESC CMPSS_DIR_SHORT_DESC "+h+" NONE;\
						POST_SPEED_LMT_VAL POST_SPEED_LMT_VAL "+h+" NONE;\
						RD_CHAR_CD RD_CHAR_CD "+h+" NONE;\
						RD_CHAR_LONG_DESC RD_CHAR_LONG_DESC "+h+" NONE;\
						OFF_RDWY_FLG OFF_RDWY_FLG "+h+" NONE;\
						ISECT_TYP_CD ISECT_TYP_CD "+h+" NONE;\
						ISECT_TYP_SHORT_DESC ISECT_TYP_SHORT_DESC "+h+" NONE;\
						ISECT_REL_FLG ISECT_REL_FLG "+h+" NONE;\
						RNDABT_FLG RNDABT_FLG "+h+" NONE;\
						DRVWY_REL_FLG DRVWY_REL_FLG "+h+" NONE;\
						LN_QTY LN_QTY "+h+" NONE;\
						TURNG_LEG_QTY TURNG_LEG_QTY "+h+" NONE;\
						MEDN_TYP_CD MEDN_TYP_CD "+h+" NONE;\
						MEDN_TYP_LONG_DESC MEDN_TYP_LONG_DESC "+h+" NONE;\
						IMPCT_LOC_CD IMPCT_LOC_CD "+h+" NONE;\
						COLLIS_TYP_CD COLLIS_TYP_CD "+h+" NONE;\
						COLLIS_TYP_LONG_DESC COLLIS_TYP_LONG_DESC "+h+" NONE;\
						CRASH_SVRTY_CD CRASH_SVRTY_CD "+v+" NONE;\
						WTHR_COND_CD WTHR_COND_CD "+h+" NONE;\
						WTHR_COND_LONG_DESC WTHR_COND_LONG_DESC "+h+" NONE;\
						RD_SURF_COND_CD RD_SURF_COND_CD "+h+" NONE;\
						RD_SURF_MED_DESC RD_SURF_MED_DESC "+h+" NONE;\
						LGT_COND_CD LGT_COND_CD "+h+" NONE;\
						LGT_COND_LONG_DESC LGT_COND_LONG_DESC "+h+" NONE;\
						TRAF_CNTL_DEVICE_CD TRAF_CNTL_DEVICE_CD "+h+" NONE;\
						TRAF_CNTL_DEVICE_LONG_DESC TRAF_CNTL_DEVICE_LONG_DESC "+h+" NONE;\
						TRAF_CNTL_FUNC_FLG TRAF_CNTL_FUNC_FLG "+h+" NONE;\
						INVSTG_AGY_CD INVSTG_AGY_CD "+h+" NONE;\
						INVSTG_AGY_LONG_DESC INVSTG_AGY_LONG_DESC "+h+" NONE;\
						SCHL_ZONE_IND SCHL_ZONE_IND "+h+" NONE;\
						WRK_ZONE_IND WRK_ZONE_IND "+h+" NONE;\
						ALCHL_INVLV_FLG ALCHL_INVLV_FLG "+h+" NONE;\
						DRUG_INVLV_FLG DRUG_INVLV_FLG "+h+" NONE;\
						CRASH_SPEED_INVLV_FLG CRASH_SPEED_INVLV_FLG "+h+" NONE;\
						CRASH_HIT_RUN_FLG CRASH_HIT_RUN_FLG "+h+" NONE;\
						POP_RNG_CD POP_RNG_CD "+h+" NONE;\
						POP_RNG_MED_DESC POP_RNG_MED_DESC "+h+" NONE;\
						RD_CNTL_CD RD_CNTL_CD "+h+" NONE;\
						RD_CNTL_MED_DESC RD_CNTL_MED_DESC "+h+" NONE;\
						REG_ID REG_ID "+h+" NONE;\
						DIST_ID DIST_ID "+h+" NONE;\
						TOT_SFTY_EQUIP_USED_QTY TOT_SFTY_EQUIP_USED_QTY "+h+" NONE;\
						TOT_SFTY_EQUIP_UNUSED_QTY TOT_SFTY_EQUIP_UNUSED_QTY "+h+" NONE;\
						TOT_SFTY_EQUIP_USE_UNKNWN_QTY TOT_SFTY_EQUIP_USE_UNKNWN_QTY "+h+" NONE;\
						CRASH_MO_NO CRASH_MO_NO "+h+" NONE;\
						CRASH_DAY_NO CRASH_DAY_NO "+h+" NONE;\
						CRASH_YR_NO CRASH_YR_NO "+h+" NONE;\
						CRASH_WK_DAY_CD CRASH_WK_DAY_CD "+h+" NONE;\
						CRASH_CAUSE_1_CD CRASH_CAUSE_1_CD "+h+" NONE;\
						CRASH_CAUSE_1_LONG_DESC CRASH_CAUSE_1_LONG_DESC "+h+" NONE;\
						CRASH_CAUSE_2_CD CRASH_CAUSE_2_CD "+h+" NONE;\
						CRASH_CAUSE_2_LONG_DESC CRASH_CAUSE_2_LONG_DESC "+h+" NONE;\
						CRASH_CAUSE_3_CD CRASH_CAUSE_3_CD "+h+" NONE;\
						CRASH_CAUSE_3_LONG_DESC CRASH_CAUSE_3_LONG_DESC "+h+" NONE;\
						CRASH_EVNT_1_CD CRASH_EVNT_1_CD "+h+" NONE;\
						CRASH_EVNT_1_LONG_DESC CRASH_EVNT_1_LONG_DESC "+h+" NONE;\
						CRASH_EVNT_2_CD CRASH_EVNT_2_CD "+h+" NONE;\
						CRASH_EVNT_2_LONG_DESC CRASH_EVNT_2_LONG_DESC "+h+" NONE;\
						CRASH_EVNT_3_CD CRASH_EVNT_3_CD "+h+" NONE;\
						CRASH_EVNT_3_LONG_DESC CRASH_EVNT_3_LONG_DESC "+h+" NONE;\
						GIS_PRC_DT GIS_PRC_DT "+h+" NONE;\
						EFFECTV_DT EFFECTV_DT "+h+" NONE;\
						MPA_FLAG MPA_FLAG "+h+" NONE;\
						SINK_FLAG SINK_FLAG "+v+" NONE;\
						"

def communicateResults(message):
	arcpy.AddMessage(message)
	print (message)
def hms_string(sec_elapsed):
	# SET UP A TIMER
    h = int(sec_elapsed / (60 * 60))
    m = int((sec_elapsed % (60 * 60)) / 60)
    s = sec_elapsed % 60.
    return "{}:{:>02}:{:>05.2f}".format(h, m, s)
def saveInStudyArea(in_fc,select_type,select_fc,distance,out_fc,query=None, fields=None):
	fc_lyr = in_fc+"_lyr"
	arcpy.MakeFeatureLayer_management(in_fc,fc_lyr,query, "", fields)
	arcpy.MakeFeatureLayer_management(select_fc,select_fc+"_lyr")
	arcpy.SelectLayerByLocation_management(fc_lyr,select_type,select_fc+"_lyr", distance, "NEW_SELECTION")
	arcpy.CopyFeatures_management(fc_lyr,out_fc)
						
try:
	start_time = time.time()

	# PROCESS: Add crash calculation scores (normalized) to corridors to create the High Injury Network
	# Crashes query removes sinks and includes only crashes within the 5-year window (2010-2014)
	saveInStudyArea(crashes,"INTERSECT",study_area,"",crashes_copy,"\"UNLOCT_FLG\" = 0 AND \"CRASH_DT\" >= date '2010-01-01 00:00:00'", crash_fields)
	arcpy.MakeFeatureLayer_management(corridors, "corridors_lyr")
	# Join crash point attributes to the corridors where they intersect within 70 feet 
	arcpy.SpatialJoin_analysis("corridors_lyr","crashes_lyr",corridor_crashes,"JOIN_ONE_TO_MANY","KEEP_COMMON","","INTERSECT","70 Feet","#")
	# Dissolve the duplicate corridor segments by UID and summarize the crash flags (severity by mode)
	arcpy.Dissolve_management(corridor_crashes,corridor_crashes_count,["TARGET_FID","STREETNAME", "DIRECTION"],"Auto_FA SUM;Bike_FA SUM;Ped_FA SUM;Bike_BC SUM;Ped_BC SUM;Bike_PDO SUM;Ped_PDO SUM","MULTI_PART","DISSOLVE_LINES")
	# Add and calculate the normalized score fields
	n = "name"
	q = "query"
	fields = ["All","FA","Auto","Bike","Ped"]
	field_dict = {
					"All":{n:"nScore",q:"""(((( [SUM_Auto_FA] + [SUM_Bike_FA] + [SUM_Ped_FA]) *10)+(( [SUM_Bike_BC] + [SUM_Ped_BC])*3)+( [SUM_Bike_PDO] + [SUM_Ped_PDO])) / [SHAPE_Length]) *10000"""},
					"FA":{n:"nScore_FA",q:"""((( [SUM_Auto_FA] + [SUM_Bike_FA] + [SUM_Ped_FA]) *10) / [SHAPE_Length]) *10000"""},
					"Auto":{n:"nScore_Auto",q:"""(([SUM_Auto_FA] *10)/[SHAPE_Length] ) * 10000"""},
					"Bike":{n:"nScore_Bike",q:"""((( [SUM_Bike_FA] * 10 ) + ( [SUM_Bike_BC] * 3 ) + ( [SUM_Bike_PDO] * 1 ) ) / [SHAPE_Length] ) * 10000"""},
					"Ped":{n:"nScore_Ped",q:"""(((( [SUM_Ped_FA]) *10)+((  [SUM_Ped_BC])*3)+([SUM_Ped_PDO])) / [SHAPE_Length]) *10000"""}}
	for f in fields:
		arcpy.AddField_management(corridor_crashes_count,field_dict[f][n])
		arcpy.CalculateField_management(corridor_crashes_count,field_dict[f][n],field_dict[f][q],"VB","#")

except Exception as e:
	communicateResults ("!-----------------\nThere was an error: %s-----------------!" % e)
else:
	communicateResults ("Success!")
finally:
	end_time = time.time()
	communicateResults ("Total time:	{}.".format(hms_string(end_time - start_time)))
	del arcpy
