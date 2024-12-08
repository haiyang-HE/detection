# import openpyxl
#
# # 读取txt文件内容并按行分割
# with open(r'D:\00000\RTDETR-main-ul\runs\detect\exp28\output.txt', 'r') as file:
#     lines = file.readlines()
#
# # 创建一个新的Excel工作表
# wb = openpyxl.Workbook()
# sheet = wb.active
#
# # 字典变量存储标题信息
# title_dict = {0: 'R-EPcell', 1: 'G-EPcell', 2: 'Neg-EPcell', 3: 'Db-EPcell'}
#
# # 设置标题行
# for col_idx, title in title_dict.items():
#     cell = sheet.cell(row=1, column=col_idx*2+6)  # 注意Excel单元格编号以1为起始
#     cell.value = title
#
# # 将每行数据中每个单元格的值写入Excel表格
# for row_idx, line in enumerate(lines, start=2):
#     data = line.strip().split()
#     for col_idx, item in enumerate(data, start=1):
#         cell = sheet.cell(row=row_idx, column=col_idx)
#         if col_idx in [7, 9, 11, 13]:
#         # if col_idx in [6, 8, 10, 12]:
#             cell.value = None
#         else:
#             cell.value = item
#
# # 保存Excel文件
# wb.save('outputsunshang1.xlsx')
#
# print("数据已写入Excel文件")
import pandas as pd
from pathlib import Path

# 假设你的数据
data = {
    'image 1/10 D:\\00000\\RTDETR-main-ul\\cell-ep-617\\images\\val\\CCD_WT_2587_2-2_KRT5+UPK3A_20X2_c1+2+3.jpg: ': {
        'R-EPcell': 124,
        'G-EPcell': 14,
        'Neg-EPcell': 67,
        'Db-EPcell': 0
    }
}

# 将数据转换为适合 DataFrame 的格式
rows = []
for image_name, values in data.items():
    row = {'name': image_name.strip()}
    row.update(values)
    rows.append(row)

# 创建 DataFrame
df = pd.DataFrame(rows)

# 定义输出文件路径
excel_file_path = 'output_data.xlsx'

# 检查 Excel 文件是否存在并读取工作表
if Path(excel_file_path).exists():
    try:
        existing_data = pd.read_excel(excel_file_path, sheet_name=None, engine='openpyxl')  # 读取所有工作表
        if existing_data:  # 检查是否有可用的工作表
            with pd.ExcelWriter(excel_file_path, engine='openpyxl', mode='a') as writer:
                df.to_excel(writer, index=False, header=False, sheet_name='Sheet1', startrow=writer.sheets['Sheet1'].max_row)
        else:
            df.to_excel(excel_file_path, index=False, sheet_name='Sheet1')
    except ValueError:
        print("Excel文件没有可用的工作表，创建新的文件。")
        df.to_excel(excel_file_path, index=False, sheet_name='Sheet1')
else:
    # 如果文件不存在，直接创建
    df.to_excel(excel_file_path, index=False, sheet_name='Sheet1')

print("数据已成功处理。")