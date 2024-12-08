import os
import shutil

source_dir= r"D:\00000\cellcount_ultis\cocodsb"
target_dir = os.path.join(source_dir, 'mydatacoco')

# 创建目标目录
os.makedirs(target_dir, exist_ok=True)

# 复制train文件夹中以.jpg结尾的文件到目标目录并重命名为train2017
train_dir = os.path.join(source_dir, 'traincoco','JPEGImages')
target_train_dir = os.path.join(target_dir, 'train2017')
os.makedirs(target_train_dir, exist_ok=True)
for file in os.listdir(train_dir):
    if file.endswith('.jpg'):
        shutil.copy(os.path.join(train_dir, file), os.path.join(target_train_dir, file))


# 复制val文件夹中以.jpg结尾的文件到目标目录并重命名为val2017
val_dir = os.path.join(source_dir, 'valcoco','JPEGImages' )
target_val_dir = os.path.join(target_dir, 'val2017')
os.makedirs(target_val_dir, exist_ok=True)
for file in os.listdir(val_dir):
    if file.endswith('.jpg'):
        shutil.copy(os.path.join(val_dir, file), os.path.join(target_val_dir, file))

annfile = os.path.join(target_dir, 'annotations')
os.makedirs(annfile, exist_ok=True)
# 复制traincoco目录中的annotations.json到目标目录中的annotations，并改名为instances_train2017.json
shutil.copyfile(os.path.join(source_dir, 'traincoco', 'annotations.json'), os.path.join(target_dir, 'annotations', 'instances_train2017.json'))

# 复制valcoco目录中的annotations.json到目标目录中的annotations，并改名为instances_val2017.json
shutil.copyfile(os.path.join(source_dir, 'valcoco', 'annotations.json'), os.path.join(target_dir, 'annotations', 'instances_val2017.json'))