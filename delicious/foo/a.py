import os

for folder_name, sub_folder, file_name in os.walk(os.path.join(os.getcwd(), 'delicious')):
    print(f"This is the folder name: {folder_name}")
    print(f"This is the sub folder name: {sub_folder}")
    print(f"This is the filename: {file_name}")
    print()
