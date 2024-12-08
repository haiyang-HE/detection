import os
import json
import random
import base64
import shutil
import argparse
from pathlib import Path
from glob import glob


# Parse arguments
def arg_directory(path):
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f'`{path}` is not a valid path')


parser = argparse.ArgumentParser(
    description='Convert LabelMe annotations to YOLO compatible'
)
parser.add_argument('--input',
                    type=arg_directory,
                    help='Directory to LabelMe annotations',
                    default='atest/oringal'
                    )
parser.add_argument('--output',
                    type=arg_directory,
                    help='Directory to which YOLO annotations will be stored',
                    default='yolots'
                    )
parser.add_argument('--ratio',
                    type=float,
                    help='Training ratio',
                    default=0.9
                    )
args = parser.parse_args()

# YOLO metadata and files
yolo_names = []
yolo_train_dir_path = os.path.join(args.output, 'train')
yolo_valid_dir_path = os.path.join(args.output, 'valid')
yolo_backup_dir_path = os.path.join(args.output, 'backup')
yolo_list_file_train_path = os.path.join(args.output, 'train.txt')
yolo_list_file_valid_path = os.path.join(args.output, 'valid.txt')
yolo_data_path = os.path.join(args.output, 'custom.data')
yolo_names_path = os.path.join(args.output, 'custom.names')

# Prepare output directory
shutil.rmtree(yolo_train_dir_path)
os.mkdir(yolo_train_dir_path)
shutil.rmtree(yolo_valid_dir_path)
os.mkdir(yolo_valid_dir_path)
if not os.path.isdir(yolo_backup_dir_path):
    os.mkdir(yolo_backup_dir_path)

# Convert image annotations
yolo_list_file = {
    'train': open(yolo_list_file_train_path, 'w'),
    'valid': open(yolo_list_file_valid_path, 'w')
}
for index, labelme_annotation_path in enumerate(glob(f'{args.input}/*.json')):
    image_id = os.path.basename(labelme_annotation_path).rstrip('.json')
    train_or_valid = 'train' if random.random() < args.ratio else 'valid'

    labelme_annotation_file = open(labelme_annotation_path, 'r')
    labelme_annotation = json.load(labelme_annotation_file)

    yolo_annotation_path = os.path.join(args.output, train_or_valid, image_id + '.txt')
    yolo_annotation_file = open(yolo_annotation_path, 'w')
    yolo_image = base64.decodebytes(labelme_annotation['imageData'].encode())
    # yolo_image = "None"
    yolo_image_path = os.path.join(args.output, train_or_valid, image_id + '.jpg')

    # Write YOLO image (and it to the list)
    yolo_image_file = open(yolo_image_path, 'wb')
    yolo_image_file.write(yolo_image)
    yolo_image_file.close()
    yolo_list_file[train_or_valid].write(f'{yolo_image_path}{os.linesep}')

    # Write YOLO image annotation
    for shape in labelme_annotation['shapes']:
        if shape['shape_type'] != 'rectangle':
            print(
                f'Invalid type `{shape["shape_type"]}` in annotation `annotation_path`')
            continue
        if shape['label'] not in yolo_names:
            yolo_names.append(shape['label'])

        points = shape['points']
        scale_width = 1.0 / labelme_annotation['imageWidth']
        scale_height = 1.0 / labelme_annotation['imageHeight']
        width = (points[1][0] - points[0][0]) * scale_width
        height = (points[1][1] - points[0][1]) * scale_height
        x = ((points[1][0] + points[0][0]) / 2) * scale_width
        y = ((points[1][1] - points[0][1]) / 2) * scale_height
        object_class = yolo_names.index(shape['label'])
        yolo_annotation_file.write(f'{object_class} {x} {y} {width} {height}')
    yolo_annotation_file.close()
yolo_list_file['train'].close()
yolo_list_file['valid'].close()

# Write YOLO names
yolo_names_file = open(yolo_names_path, 'w')
yolo_names_file.write(os.linesep.join(yolo_names))
yolo_names_file.close()

# Write YOLO data configuration
yolo_data_file = open(yolo_data_path, 'w')
yolo_data_file.write(f'classes = {len(yolo_names)}{os.linesep}')
yolo_data_file.write(f'train = {yolo_list_file_train_path}{os.linesep}')
yolo_data_file.write(f'valid = {yolo_list_file_valid_path}{os.linesep}')
yolo_data_file.write(f'names = {yolo_names_path}{os.linesep}')
yolo_data_file.write(f'backup = {yolo_backup_dir_path}{os.linesep}')