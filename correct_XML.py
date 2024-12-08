import os
import xml.etree.ElementTree as ET


def safe_get_text(element):
    """安全获取XML元素的文本内容"""
    if element is not None and hasattr(element, 'text'):
        return element.text.strip() if element.text else None
    return None


def validate_xml_file(file_path):
    """验证单个XML文件"""
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        # 这里可以定义需要查找的节点路径，例如 'child/subchild'
        element_paths_to_check = ['child/subchild', 'missing_child']

        for path in element_paths_to_check:
            text_content = safe_get_text(root.find(path))
            if text_content is None:
                print(f"File {file_path} has an issue with path: {path}")
                return True  # 返回 True 表示已有问题

        return False  # 正常

    except ET.ParseError:
        print(f"File {file_path} is not a valid XML.")
        return True  # 返回 True 表示已有问题
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return True  # 返回 True 表示已有问题


def validate_xml_folder(folder_path):
    """遍历文件夹中的所有XML文件并验证它们"""
    problematic_files = []

    for filename in os.listdir(folder_path):
        if filename.endswith('.xml'):
            file_path = os.path.join(folder_path, filename)
            if validate_xml_file(file_path):
                problematic_files.append(filename)

    return problematic_files


if __name__ == '__main__':
    folder_path = r'F:\红外数据集\红外海上船舶数据集\红外船舶数据库\dataset\labels\train_xml'  # 替换为你的文件夹路径
    problems = validate_xml_folder(folder_path)

    if problems:
        print("Problematic XML files found:")
        for file in problems:
            print(file)
    else:
        print("No problematic XML files found.")