import os
import shutil

def split(directory, class_dir, train_dir, test_dir, test_size):
    files = os.listdir(os.path.join(directory, class_dir))
    number_of_files = len(files)

    os.mkdir(os.path.join(train_dir, class_dir))
    os.mkdir(os.path.join(test_dir, class_dir))

    train_dir = os.path.join(train_dir, class_dir)
    test_dir = os.path.join(test_dir, class_dir)

    number_of_testing_files = int(number_of_files * test_size)
    number_of_training_files = number_of_files - number_of_testing_files

    for file_name in files[:number_of_training_files]:
        shutil.copy(os.path.join(directory, class_dir, file_name), train_dir)
    
    for file_name in files[number_of_training_files:]:
        shutil.copy(os.path.join(directory, class_dir, file_name), test_dir)

def initialize():
    root = "./doodle_dataset"
    train_dir = "./train"
    test_dir = "./test"
    test_size = 0.2

    classes = os.listdir(root)
    for class_name in classes:
        split(root, class_name, train_dir, test_dir, test_size)



initialize()