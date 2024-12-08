import glob
import os
import shutil

from sklearn.model_selection import train_test_split

save_train_path= r"D:\data\data_guo\new-mydatatrain"
save_val_path= r"D:\data\data_guo\new-mydataval"
if not os.path.exists(save_train_path):
    os.makedirs(save_train_path)
if not os.path.exists(save_val_path):
    os.makedirs(save_val_path)

labelme_path = r"D:\data\data_guo\new-mydata"
json_list_path = glob.glob(labelme_path + "/*.json")
train_path, val_path = train_test_split(json_list_path, test_size=0.1, train_size=0.9,random_state=510)
print(val_path)
print(len(val_path))
print(len(train_path))


for file_path in train_path:
    # 获取文件名
    file_name = os.path.basename(file_path)
    # 构建目标文件路径
    destination_path = os.path.join(save_train_path, file_name)
    jpgdestination_path = os.path.join(save_train_path, file_name.replace(".json", ".jpg"))
    # 复制文件
    shutil.copyfile(file_path, destination_path)
    shutil.copyfile(file_path.replace(".json", ".jpg"), jpgdestination_path)

for file_path in val_path:
    # 获取文件名
    file_name = os.path.basename(file_path)
    # 构建目标文件路径
    destination_path = os.path.join(save_val_path, file_name)
    jpgdestination_path = os.path.join(save_val_path, file_name.replace(".json", ".jpg"))
    # 复制文件
    shutil.copyfile(file_path, destination_path)
    shutil.copyfile(file_path.replace(".json", ".jpg"), jpgdestination_path)