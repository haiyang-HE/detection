# import os
# import shutil
#
#
# # 获取当前目录下所有文件
# sources_folder = r"D:\data\data_guo\zdata\savedata617\train"
# files = os.listdir(sources_folder)
# # 创建imgs, jsons, out文件夹
# os.makedirs(os.path.join(sources_folder,'imgs'), exist_ok=True)
# os.makedirs(os.path.join(sources_folder,'jsons'), exist_ok=True)
# os.makedirs(os.path.join(sources_folder,'out'), exist_ok=True)
#
# # 移动.jpg文件到imgs文件夹
# for file in files:
#     if file.endswith('.jpg'):
#         shutil.move(os.path.join(sources_folder,file), os.path.join(sources_folder,'imgs'))
#
# # 移动.json文件到jsons文件夹
# for file in files:
#     if file.endswith('.json'):
#         shutil.move(os.path.join(sources_folder,file), os.path.join(sources_folder,'jsons'))
import os
import random
import shutil

# 设置文件夹路径
data_folder = r'F:\红外数据集\红外海上船舶数据集\红外船舶数据库\dataset\labels\txt2'  # 包含 JPG 和 TXT 文件的文件夹路径
train_folder = r'F:\红外数据集\红外海上船舶数据集\红外船舶数据库\dataset\labels/train'  # 训练集输出路径
val_folder = r'F:\红外数据集\红外海上船舶数据集\红外船舶数据库\dataset\labels/val'  # 验证集输出路径

# 创建训练集和验证集的文件夹
os.makedirs(train_folder, exist_ok=True)
os.makedirs(val_folder, exist_ok=True)

# 获取所有的 jpg 和 txt 文件
files = [f for f in os.listdir(data_folder) if f.endswith('.jpg') or f.endswith('.txt')]

# 遍历文件，找到 JPG 文件
jpg_files = [f for f in files if f.endswith('.jpg')]

# 随机洗牌文件列表
random.shuffle(jpg_files)

# 划分比例
train_size = 0.8  # 80% 用于训练集
split_index = int(len(jpg_files) * train_size)

# 划分训练集和验证集
train_files = jpg_files[:split_index]
val_files = jpg_files[split_index:]

# 移动文件到对应的文件夹
for file_name in train_files:
    # 处理 JPG 文件
    src_img = os.path.join(data_folder, file_name)
    dst_img = os.path.join(train_folder, file_name)
    shutil.copy(src_img, dst_img)

    # 处理相应的 TXT 文件
    txt_file_name = file_name.replace('.jpg', '.txt')
    src_txt = os.path.join(data_folder, txt_file_name)
    dst_txt = os.path.join(train_folder, txt_file_name)
    if os.path.exists(src_txt):
        shutil.copy(src_txt, dst_txt)

for file_name in val_files:
    # 处理 JPG 文件
    src_img = os.path.join(data_folder, file_name)
    dst_img = os.path.join(val_folder, file_name)
    shutil.copy(src_img, dst_img)

    # 处理相应的 TXT 文件
    txt_file_name = file_name.replace('.jpg', '.txt')
    src_txt = os.path.join(data_folder, txt_file_name)
    dst_txt = os.path.join(val_folder, txt_file_name)
    if os.path.exists(src_txt):
        shutil.copy(src_txt, dst_txt)

print("划分完成。")