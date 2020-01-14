'''
Description:
Master Script to Generate DEMs for W FL. 

Author:
Chris Amante
Christopher.Amante@colorado.edu

Date:
11/25/2019

'''
#################################################################
#################################################################
#################################################################
####################### IMPORT MODULES ##########################
#################################################################
#################################################################
#################################################################
import os
import subprocess
import sys
import glob
#################################################################
#################################################################
#################################################################
###################### INITIAL VARIABLES ########################
#################################################################
#################################################################
#################################################################
basename="w_fl"
main_dir='/media/sf_E_win_lx/COASTAL_Act/camante/w_fl'
#
#
code_dir=main_dir+'/code/DEM_generation'
conv_grd_path=main_dir+'/data/conv_grd/cgrid_mllw2navd88.tif'
name_cell_extents_bs=main_dir+'/data/bathy/bathy_surf/name_cell_extents_bs.csv'
name_cell_extents_dem=main_dir+'/software/gridding/name_cell_extents_dem.csv'
bs_dlist=main_dir+'/data/bathy/bathy_surf/w_fl_bs.datalist'
dem_dlist=main_dir+'/software/gridding/w_fl_dem.datalist'
bs_path=main_dir+'/data/bathy/bathy_surf/tifs'
coast_shp=main_dir+'/data/coast/w_fl_coast'
dc_lidar_download_process=main_dir+'/data/dc_lidar_download_process.csv'
#shp for data download
study_area_shp=main_dir+'/data/study_area/w_fl_tiles_buff.shp'
#/media/sf_E_win_lx/COASTAL_Act/camante/w_fl/data/study_area/w_fl_tiles_buff.shp

os.system('cd')
os.chdir(main_dir)

print 'Main Directory is', os.getcwd()
#Creating main subdirectories
dir_list=['data', 'docs', 'software', 'software/gridding']
for i in dir_list:
	if not os.path.exists(i):
		print 'creating subdir', i
		os.makedirs(i)

#Create Empty Dummy BS, Bathy Surface and DEM datalists
create_bs_dlist='''if [ ! -e {}/data/bathy/bathy_surf/w_fl_bs.datalist ] ; 
then touch {}/data/bathy/bathy_surf/w_fl_bs.datalist
fi'''.format(main_dir,main_dir)
os.system(create_bs_dlist)

create_dem_dlist='''if [ ! -e {}/software/gridding/w_fl_dem.datalist ] ; 
then touch {}/software/gridding/w_fl.datalist
fi'''.format(main_dir,main_dir)
os.system(create_dem_dlist)


#ROI for data download
west_buff=-84.05
east_buff=-81.70
south_buff=27.20
north_buff=30.55
roi_str=str(west_buff)+'/'+str(east_buff)+'/'+str(south_buff)+'/'+str(north_buff)
roi_str_ogr=str(west_buff)+' '+str(south_buff)+' '+str(east_buff)+' '+str(north_buff)

#test_ROI
#roi_str_ogr='-84.05 27.20 -81.70 30.55'
#roi_str='-84.05/-81.70/27.20/30.55'

print "ROI is", roi_str
print "ROI OGR is", roi_str_ogr
#sys.exit()

#################################################################
#################################################################
#################################################################
####################### PRE-PROCESSING ##########################
#################################################################
#################################################################
#################################################################
# #Create Conversion Grid -- MLLW to NAVD88
# if not os.path.exists('data/conv_grd'):
# 	os.makedirs('data/conv_grd')

# os.chdir('data/conv_grd')
# print "Creating mllw2navd88 conversion grid"
# conv_grd_cmd='dem cgrid -i mllw -o navd88 -c -E 1s -R' +roi_str
# os.system(conv_grd_cmd)

#################################################################
#################################################################
#################################################################
####################### DATA DOWNLOAD ###########################
#################################################################
#################################################################
#################################################################

#################################################################
####################### STUDY AREA ##############################
#################################################################
#manually created shp in ArcGIS (w_fl_tiles.shp) 
#created name_cell_extents with arcpy get_poly_coords.py (name_cell_extents_bs.csv; name_cell_extents_DEM.csv) 
#manually created study area buffer in ArcMap (w_fl_tiles_buff.shp)

# #################################################################
# ######################## COASTLINE ##############################
# #################################################################
# os.system('cd')
# os.chdir(main_dir)
# os.chdir('data')

# coast_dir_list=['coast']
# for i in coast_dir_list:
# 	if not os.path.exists(i):
# 		print 'creating subdir', i
# 		os.makedirs(i)

# os.chdir(coast_dir_list[0])

# # #delete python script if it exists
# os.system('[ -e coast_processing.py ] && rm coast_processing.py')
# # #copy python script from DEM_generation code

# os.system('cp {}/coast_processing.py coast_processing.py'.format(code_dir)) 

# print "executing coast_processing script"
# os.system('python coast_processing.py {} {} {} {} {}'.format(basename,main_dir,study_area_shp,roi_str_ogr,roi_str))
# os.chdir('..')

# #################################################################
# ########################## BATHY ################################
# #################################################################
# os.system('cd')
# os.chdir(main_dir+'/data/bathy')

# #Creating main subdirectories
# bathy_dir_list=['usace_dredge', 'mb', 'nos', 'enc']
# for i in bathy_dir_list:
# 	if not os.path.exists(i):
# 		print 'creating subdir', i
# 		os.makedirs(i)

####################### USACE DREDGE #############################
# os.chdir(bathy_dir_list[0])
# print 'Current Directory is', os.getcwd()

# #delete python script if it exists
# os.system('[ -e usace_dredge_processing.py ] && rm usace_dredge_processing.py')
# #copy python script from DEM_generation code
# os.system('cp {}/usace_dredge_processing.py usace_dredge_processing.py'.format(code_dir)) 

# print "executing usace_dredge_processing script"
# os.system('python usace_dredge_processing.py {} {} {} {} {}'.format(main_dir, study_area_shp, conv_grd_path, bs_dlist, dem_dlist))

# ######################## Multibeam #############################
# os.system('cd')
# os.chdir(main_dir+'/data/bathy')
# os.chdir(bathy_dir_list[1])
# print 'Current Directory is', os.getcwd()

# #delete python script if it exists
# os.system('[ -e mb_processing.py ] && rm mb_processing.py')
# #copy python script from DEM_generation code
# os.system('cp {}/mb_processing.py mb_processing.py'.format(code_dir)) 

# print "executing mb_processing script"
# os.system('python mb_processing.py {} {}'.format(main_dir, name_cell_extents_dem))
# # ####
# ########################## NOS/BAG ################################
# os.system('cd')
# os.chdir(main_dir+'/data/bathy')
# os.chdir(bathy_dir_list[2])
# print 'Current Directory is', os.getcwd()

# #delete python script if it exists
# os.system('[ -e nos_processing.py ] && rm nos_processing.py')
# #copy python script from DEM_generation code
# os.system('cp {}/nos_processing.py nos_processing.py'.format(code_dir)) 

# print "executing nos_processing script"
# os.system('python nos_processing.py {} {} {} {} {}'.format(main_dir, roi_str, conv_grd_path, bs_dlist, dem_dlist))

# ########################## ENC ################################
# os.system('cd')
# os.chdir(main_dir+'/data/bathy')
# os.chdir(bathy_dir_list[3])
# print 'Current Directory is', os.getcwd()

# #delete python script if it exists
# os.system('[ -e enc_processing.py ] && rm enc_processing.py')
# #copy python script from DEM_generation code
# os.system('cp {}/enc_processing.py enc_processing.py'.format(code_dir)) 

# print "executing enc_processing script"
# os.system('python enc_processing.py {} {} {}'.format(main_dir, conv_grd_path, bs_dlist))

#############################################################
################## DIGITAL COAST LIDAR ######################
#############################################################
# os.system('cd')
# os.chdir(main_dir+'/data')

# dc_lidar_dir_list=['dc_lidar']
# for i in dc_lidar_dir_list:
# 	if not os.path.exists(i):
# 		print 'creating subdir', i
# 		os.makedirs(i)

# os.chdir(dc_lidar_dir_list[0])

# # #delete python script if it exists
# os.system('[ -e dc_lidar_processing.py ] && rm dc_lidar_processing.py')
# # #copy python script from DEM_generation code

# os.system('cp {}/dc_lidar_processing.py dc_lidar_processing.py'.format(code_dir)) 

# print "executing dc_lidar_processing script"
# os.system('python dc_lidar_processing.py {} {} {} {}'.format(main_dir,basename,dc_lidar_download_process,study_area_shp))


## manually downloaded lidar-derived DEM that didn't have laz files using digital coast
## E:\COASTAL_Act\camante\w_fl\data\dc_lidar\missing\2007_FDEM_Southwest
## tif2chunks2xyz.sh 500 no 0.0000102880663
## below is from AL/FL DEMs

# os.system('cd')
# os.chdir(main_dir+'/data/dc_lidar')

# dc_lidar_missing_dir_list=['missing']
# for i in dc_lidar_missing_dir_list:
# 	if not os.path.exists(i):
# 		print 'creating subdir', i
# 		os.makedirs(i)


# os.chdir(dc_lidar_missing_dir_list[0])

# # #delete python script if it exists
# os.system('[ -e dc_lidar_missing_processing.py ] && rm dc_lidar_missing_processing.py')
# # #copy python script from DEM_generation code

# os.system('cp {}/dc_lidar_missing_processing.py dc_lidar_missing_processing.py'.format(code_dir)) 

# print "executing dc_lidar_missing_processing script"
# os.system('python dc_lidar_missing_processing.py {}'.format(main_dir))


# #############################################################
# ################## TOPO NOT ON DIGITAL COAST ################
# #############################################################
# 
## Manually downloaded from USGS NED
## 

# # #################################################################
# # #################################################################
# # #################################################################
# # ####################### DATA PROCESSING #########################
# # #################################################################
# # #################################################################
# # #################################################################

# # #################################################################
# # #################################################################
# # #################################################################
# # ####################### BATHY SURFACE ###########################
# # #################################################################
# # #################################################################
# # #################################################################
os.system('cd')
os.chdir(main_dir+'/data/bathy')

# Create Bathy Surface 
if not os.path.exists('bathy_surf'):
 	os.makedirs('bathy_surf')

os.chdir('bathy_surf')
bathy_surf_cmd='create_bs.sh ' + name_cell_extents_bs + ' ' + bs_dlist + ' ' + coast_shp
os.system(bathy_surf_cmd)

# # #################################################################
# # #################################################################
# # #################################################################
# # ####################### DEM GENERATION ##########################
# # #################################################################
# # #################################################################
# # #################################################################
#Create DEM
os.system('cd')
os.chdir(main_dir)
os.chdir('software/gridding')

create_dem_cmd='create_dem.sh ' + name_cell_extents_dem + ' ' + dem_dlist + ' ' + str(5)
#create_dem.sh /media/sf_E_win_lx/COASTAL_Act/camante/w_fl/software/gridding/name_cell_extents_dem.csv /media/sf_E_win_lx/COASTAL_Act/camante/w_fl/software/gridding/w_fl.datalist /media/sf_E_win_lx/COASTAL_Act/camante/w_fl/data/bathy/bathy_surf/tifs 5
#create_dem.sh /media/sf_E_win_lx/COASTAL_Act/camante/w_fl/software/gridding/name_cell_extents_dem.csv /media/sf_E_win_lx/COASTAL_Act/camante/w_fl/software/gridding/w_fl.datalist 5
os.system(create_dem_cmd)

print "Tested out git2"
