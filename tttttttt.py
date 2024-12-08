import os
import shutil

# 源文件夹路径
source_folder = r'E:\新上皮细胞数据\20240117_Ep300 cKO_Upk2+Shh_H3K27me3+UPK3A'
# 目标文件夹路径
destination_folder = r'E:\新上皮细胞数据\new-ep'

# 遍历源文件夹
for root, dirs, files in os.walk(source_folder):
    for file in files:
        # 如果文件以.jpg结尾
        if file.endswith('.jpg'):
            # 拼接源文件路径
            source_file_path = os.path.join(root, file)
            # 拼接目标文件路径
            destination_file_path = os.path.join(destination_folder, file)
            # 复制文件
            shutil.copy(source_file_path, destination_file_path)