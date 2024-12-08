import glob
import os
import shutil


save_img_path= r"D:\data\data_guo\data-3rd\imgs"
if not os.path.exists(save_img_path):
    os.makedirs(save_img_path)


labelme_path = r"D:\data\data_guo\data-3rd\labelme_file"
jpg_list_path = glob.glob(labelme_path + "/*.jpg")

for file_path in jpg_list_path:
    # 获取文件名
    file_name = os.path.basename(file_path)
    # 构建目标文件路径
    destination_path = os.path.join(save_img_path, file_name)
    # 复制文件
    shutil.copyfile(file_path, destination_path)