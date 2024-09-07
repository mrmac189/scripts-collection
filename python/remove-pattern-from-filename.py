# this script will find [DEMO] pattern and remove it from file and folder names

import os

# root folder
src_folder = "C:\\Users\\user\\New Folder"


def rename_files_and_directories(src_folder):
    # recursive function to rename files and directories
    for root, dirs, files in os.walk(src_folder, topdown=False):
        # rename files
        for file in files:
            if '[DEMO]' in file:
                new_file = file.replace('[DEMO]', '').strip()
                try:
                    os.rename(os.path.join(root, file), os.path.join(root, new_file))
                    print(f'File {file} renamed to {new_file}')
                except Exception as e:
                    print(f'Error during rename {file}: {e}')

        # rename dirs
        for dir in dirs:
            if '[DEMO]' in dir:
                new_dir = dir.replace('[DEMO]', '').strip()
                try:
                    os.rename(os.path.join(root, dir), os.path.join(root, new_dir))
                    print(f'Dir {dir} renamed to {new_dir}')
                except Exception as e:
                    print(f'Error during dir rename {dir}: {e}')

    print('Scripts has finished.')


if __name__ == "__main__":
    rename_files_and_directories(src_folder)