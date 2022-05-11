import glob
import shutil
import os

fp_list = glob.glob('lpixel/concat_image/20180918/error_00_fp/*.png')
center_list = glob.glob('lpixel/concat_image/20180918/error_center_line/*.png')

for i in range(len(fp_list)):
    print(fp_list)
    shutil.move(fp_list[i], 'lpixel/wmh_ano/20180918/error_00_fp/' + os.basename(fp_list[i]))



