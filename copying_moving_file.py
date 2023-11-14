import shutil
import os

current_path = os.getcwd()

# copy file and all context
shutil.copytree(os.path.join(current_path, 'f'), os.path.join(current_path, 'test'))


# copy file and folders
shutil.copy(os.path.join(current_path, 'text.txt'), os.path.join(current_path, 'test', 'man.txt'))

# move file and folders
shutil.move(os.path.join(current_path, 'text.txt'), os.path.join(current_path, 'test'))