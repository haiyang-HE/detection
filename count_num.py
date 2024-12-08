# import os
#
# # 定义需要检查的文件夹路径
# folder_path = r'F:\红外数据集\红外海上船舶数据集\红外船舶数据库\dataset\labels\txt'  # 替换为你的文件夹路径
#
# # 用于保存每个数字的总计数
# total_number_counts = {}
#
# # 遍历文件夹中的所有txt文件
# for filename in os.listdir(folder_path):
#     if filename.endswith('.txt'):
#         file_path = os.path.join(folder_path, filename)
#
#         # 读取文件内容
#         with open(file_path, 'r') as file:
#             lines = file.readlines()
#             for line in lines:
#                 line = line.strip()  # 去除前后空白
#                 if line:  # 确保行不为空
#                     # 提取第一个数字
#                     first_number = None
#                     for part in line.split():
#                         if part.isdigit():  # 检查每个部分是否为数字
#                             first_number = part
#                             break
#
#                             # 如果找到了第一个数字，增加总计数
#                     if first_number is not None:
#                         if first_number in total_number_counts:
#                             total_number_counts[first_number] += 1
#                         else:
#                             total_number_counts[first_number] = 1
#
#                         # 输出结果
# print("总计数结果:")
# for number, count in total_number_counts.items():
#     print(f'Number: {number}, Count: {count}')

import os
import shutil

# 定义文件夹路径
txt_folder_path = r'F:\红外数据集\红外海上船舶数据集\红外船舶数据库\dataset\labels\txt2'  # TXT文件所在的文件夹
jpg_folder_path = r'F:\红外数据集\红外海上船舶数据集\红外船舶数据库\dataset\labels\train_xml'  # JPG文件所在的文件夹
destination_folder_path = r'F:\红外数据集\红外海上船舶数据集\红外船舶数据库\dataset\labels\train_txt'  # 目标文件夹

# 创建目标文件夹（如果不存在的话）
os.makedirs(destination_folder_path, exist_ok=True)

# 遍历TXT文件夹中的所有文件
for filename in os.listdir(txt_folder_path):
    if filename.endswith('.txt'):
        # 替换文件扩展名为.jpg
        jpg_filename = filename[:-4] + '.jpg'  # 去掉.txt，再加上.jpg
        jpg_file_path = os.path.join(jpg_folder_path, jpg_filename)

        # 检查JPG文件是否存在
        if os.path.exists(jpg_file_path):
            # 复制JPG文件到目标文件夹
            shutil.copy(jpg_file_path, destination_folder_path)
            print(f'Copied: {jpg_filename}')
        else:
            print(f'File not found: {jpg_filename}')