import csv
filename = "C:\Users\User\gwyddion_scripts\gwy_data\c11NF_102_full.txt"

df = gwy.gwy_app_data_browser_get_current(gwy.APP_DATA_FIELD)
c = gwy.gwy_app_data_browser_get_current(gwy.APP_CONTAINER)
i = gwy.gwy_app_data_browser_get_current(gwy.APP_DATA_FIELD_ID)

ran = range(1,512,1)
c_sec = []
shift_c_sec = []

for i in ran:
	prf = df.get_profile(0,i,511,i,-1,1,interpolation=INTERPOLATION_LINEAR)
	gtt = prf.get_data()
	for j in gtt:
		shift_c_sec.append(j*(10**9))

with open(filename,'w') as data_file:
	data_writer = csv.writer(data_file, delimiter=',')
	data_writer.writerow(shift_c_sec)
print(len(shift_c_sec))