# Pygwy Script
# This is used to pull cross-sectional data from an AFM scan.
#
# Before running script in Pygwy Console:
# 1.) Make sure the image (scan) you want to extract data from is the only open (active) scan that is open in Gwyddion 
# 2.) Level and set zero the image 
# 3.) Open up the Pygwy Console by navigating to "Data Process -> Pygwy Console"
# 4.) Change the "destination" variable to the file path where you want your raw data csv, and give the output file a name by adding/replacing the last cell of the path
# 5.) Change the "image_pixel_size" variable to the pixel length of your image
# 6.) Your "scaling_factor" variable should be an integer that will be placed in as "x" to a 10^x clause, the points extracted by Gwyddion will be in meters by default. Scale them up to micrometers (x10^6) or nanometers (x10^9) by scaling them up accordingly.  
# 7.) Run the script 
# 
#

import csv

destination = "C:\Users\lemle\gwyddion_scripts\gwy_data\output.txt"
image_pixel_size = 512
scaling_factor = 9


def get_cross_sectional_data(destination,image_pixel_size,scaling_factor):
	active_image = gwy.gwy_app_data_browser_get_current(gwy.APP_DATA_FIELD)

	if type(destination) != str:
		raise TypeError("Destination must be a string.")
	else:
		destination = destination

	if type(image_pixel_size) and type(scaling_factor) != int:
		raise TypeError("Image pixel size and scaling factor must be an integer.") 
	else:
		image_pixel_size = image_pixel_size
		scaling_factor = scaling_factor

	image_pixel_length = range(1,image_pixel_size,1)
	output = []

	for each_row_of_pixels in image_pixel_length:
		extracted_profile = active_image.get_profile(0,each_row_of_pixels,image_pixel_size-1,each_row_of_pixels,-1,1,interpolation=INTERPOLATION_LINEAR)
		z_values = extracted_profile.get_data()
		for each_z_value in z_values:
			output.append(each_z_value*(10**scaling_factor))

	with open(destination,'w') as data_file:
		data_writer = csv.writer(data_file, delimiter=',')
		data_writer.writerow(output)
	print("Success! Your raw csv is located at {} with {} cross sections extracted!".format(destination,image_pixel_size))


get_cross_sectional_data(destination=destination, image_pixel_size=image_pixel_size, scaling_factor=scaling_factor)

