import os
import shutil

for file_name in os.listdir('DATA'):
    # print(f"file_name: {file_name}")
    file_path = os.path.join('DATA', file_name)
    print(f"file_path: {file_path}")
    # shutil.copy(file_path, the_destination)