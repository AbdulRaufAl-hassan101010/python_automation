import os

# get separators for path (/|\)
print(os.sep)

# get current working directory
print(os.getcwd())

# best way to make path for cross platform os
print(os.path.join('folder1'))

# change dir
# print(os.chdir('C:\\'))

# get absolute path
print(os.path.abspath("files.py"))

# get relative path
print(os.path.relpath("files.py", os.getcwd()))

# get directory path
print(os.path.dirname(os.getcwd()))

# get basename(get last part of path)
print(os.path.basename(os.getcwd()))


# check if path exist
print(os.path.exists(os.getcwd()))

# check if it is folder name or path name
print(os.path.isfile(r'C:\windows\system32\calc.exe'))
print(os.path.isdir(r'C:\windows\system32'))


# get file size bytes
print(os.path.getsize(r'C:\windows\system32'))


# make dir
# print(os.makedirs())


"""
calculate  the file size in in directory
"""
# list directory
listdir = os.listdir()
total_size = 0

for item in listdir:
    path = os.path.join(os.getcwd(), item)
    if not os.path.isfile(path):
        continue

    file_size = os.path.getsize(path)
    print(f'{item}....{file_size / 1024}KB')
    total_size += file_size


print(f"Total file size: {total_size / 1024}KB")
