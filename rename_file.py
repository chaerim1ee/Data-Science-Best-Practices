import os
import zipfile
import pandas as pd

#set directory path
directory = r'your directory'

# Simple example renaming file
old_filename = 'current_file_name.csv'
new_filename = 'new_file_name.csv'

old_file_path = os.path.join(directory, old_filename)
new_file_path = os.path.join(directory, new_filename)

os.rename(old_file_path, new_file_path)
print(f'Renamed {old_filename} to {new_filename}')
