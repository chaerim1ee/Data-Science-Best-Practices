import os
import zipfile
import pandas as pd

#set directory path
directory = r'C:/Users/clee1/OneDrive - Fors Marsh/Desktop/FEVS'

# Simple example renaming file
directory = 'C:/Users/clee1/OneDrive - Fors Marsh/Desktop/FEVS'
old_filename = 'FEVS_2023_PRDF_renamed.csv'
new_filename = 'FEVS_2023_PRDF.csv'

old_file_path = os.path.join(directory, old_filename)
new_file_path = os.path.join(directory, new_filename)

os.rename(old_file_path, new_file_path)
print(f'Renamed {old_filename} to {new_filename}')