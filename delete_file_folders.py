import os
import shutil

# delete files
# os.unlink(os.path.join(os.getcwd(), 'test'))

# delete empty folders
# os.rmdir(os.path.join(os.getcwd(), 'test'))


# delete unempty folders
shutil.rmtree(os.path.join(os.getcwd(), 'test'))