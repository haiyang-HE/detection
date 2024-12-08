import os


# def count_lines_in_txt_files(directory):
#     total_lines = 0
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             if file.endswith(".txt"):
#                 file_path = os.path.join(root, file)
#                 with open(file_path, 'r') as f:
#                     lines = f.readlines()
#                     total_lines += len(lines)
#                 print(f"{file_path}: {len(lines)} lines")
#
#     print(f"Total lines in all txt files: {total_lines}")


def count_lines_in_txt_files(directory):
    total_lines = 0
    line_counts = {}

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    lines = f.readlines()
                    for line in lines:
                        first_digit = line.strip()[0]  # Get the first digit of the line
                        if first_digit not in line_counts:
                            line_counts[first_digit] = 1
                        else:
                            line_counts[first_digit] += 1
                    total_lines += len(lines)
                print(f"{file_path}: {len(lines)} lines")

    print(f"Total lines in all txt files: {total_lines}")
    for digit, count in line_counts.items():
        print(f"Lines starting with {digit}: {count} lines")


# 将目录路径替换为实际的目录路径
directory = r'D:\00000\RTDETR-main-ul\cell-yolo6-6\labels'
count_lines_in_txt_files(directory)