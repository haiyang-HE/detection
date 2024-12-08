import os
import shutil

# 源文件目录
source_dir = r'D:\data\usefull-new\jpgf'

# 目标文件目录
target_dir = r'D:\data\usefull-new\jpgf'

# 遍历源文件目录
for root, dirs, files in os.walk(source_dir):
    for file in files:
        if file.endswith('.jpg'):
            source_file = os.path.join(root, file)
            target_file = os.path.join(target_dir, file)
            shutil.copy(source_file, target_file)
