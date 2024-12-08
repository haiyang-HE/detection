import os
import shutil

def copy_different_files(dir1, dir2, output_dir):
    # 创建输出目录（如果不存在）
    os.makedirs(output_dir, exist_ok=True)

    # 获取两个目录中的文件名集合
    files_dir1 = set(os.listdir(dir1))
    files_dir2 = set(os.listdir(dir2))

    # 找出不同的文件名
    different_files_dir1 = files_dir1 - files_dir2
    different_files_dir2 = files_dir2 - files_dir1

    # 复制 dir1 中不同的文件
    for file in different_files_dir1:
        full_file_path = os.path.join(dir1, file)
        if os.path.isfile(full_file_path):  # 确保是文件而不是目录
            shutil.copy(full_file_path, output_dir)
            print(f"复制文件: {full_file_path} 到 {output_dir}")

    # 复制 dir2 中不同的文件
    for file in different_files_dir2:
        full_file_path = os.path.join(dir2, file)
        if os.path.isfile(full_file_path):
            shutil.copy(full_file_path, output_dir)
            print(f"复制文件: {full_file_path} 到 {output_dir}")

# 示例使用
dir1 = r'C:\Users\Administrator\Downloads\RTDETR-20240802\RTDETR-main\ultralytics\cfg\models\rt-detr'
dir2 = r'D:\00000\RTDETR-main-ul\ultralytics\cfg\models\rt-detr'
output_dir = 'out_diff_new'

copy_different_files(dir1, dir2, output_dir)