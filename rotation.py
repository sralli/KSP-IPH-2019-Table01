import os
import glob

def img_list():
    format_img = ['.jpg', '.jpeg', '.png']
    final = []
    for i in format_img:
        image_list = glob.glob("/Users/shivamralli/Desktop/Competitions/KCP/Data/missing_images/*"+i)
        for j in image_list:
            final.append(j)
    return final
        
image_list = img_list()

for i in image_list:
    save_path = "/Users/shivamralli/Desktop/Competitions/KCP/realign/i"
    mycmd = 'python3 /Users/shivamralli/Desktop/Competitions/KCP/Precise-face-alignment/run.py --mode 1 --path_to_load i --path_to_save save_path --rotation_mode 1'
    os.system(mycmd)