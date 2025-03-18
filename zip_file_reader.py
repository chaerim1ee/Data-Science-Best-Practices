import os
import zipfile
import pandas as pd

def extract_zip_to_csv(zip_path, extract_dir):
    try:
        # Open the ZIP file
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # List all files in the zip file
            zip_files = zip_ref.namelist()
            
            # Loop through each file inside the zip
            for file_name in zip_files:
                # Check if the file is a CSV file
                if file_name.endswith('.csv'):
                    # Extract the file and save it locally as a CSV
                    zip_ref.extract(file_name, extract_dir)
                    print(f"Extracted {file_name} from {zip_path} to {extract_dir}")
                    return os.path.join(extract_dir, file_name)
        print(f"No CSV file found in {zip_path}")
        return None
    except Exception as e:
        print(f"Error extracting {zip_path}: {e}")
        return None

def process_zip_files(directory, extract_dir):
    # Get a list of all .zip files in the specified directory
    zip_files = [f for f in os.listdir(directory) if f.endswith('.zip')]
    
    if not zip_files:
        print("No zip files found in the directory.")
        return
    
    for zip_file in zip_files:
        zip_path = os.path.join(directory, zip_file)
        
        # Extract each .zip file and save the contained .csv file
        csv_file_path = extract_zip_to_csv(zip_path, extract_dir)
        
        # If a CSV was extracted, read it into a pandas DataFrame and print it
        if csv_file_path:
            df = pd.read_csv(csv_file_path)
            print(f"Data from {csv_file_path}:")
            print(df.head())  # Display the first few rows of the extracted CSV file
            # Optionally, you can process the DataFrame or save it elsewhere
        else:
            print(f"No CSV file found in {zip_file}")
            
# Directory where your .zip files are located
directory = r'C:/Users/clee1/OneDrive - Fors Marsh/Desktop/FEVS'  # Replace with the correct directory path
# Directory where you want to extract the .csv files
extract_dir = r'C:/Users/clee1/OneDrive - Fors Marsh/Desktop/FEVS'  # Replace with the extraction directory

# Make sure the extraction directory exists
os.makedirs(extract_dir, exist_ok=True)

# Process each .zip file in the directory
process_zip_files(directory, extract_dir)

import os
import pandas as pd

def combine_csv_files(csv_dir, output_file):
    # List all CSV files in the directory
    csv_files = [f for f in os.listdir(csv_dir) if f.endswith('.csv')]
    
    # Initialize an empty list to store DataFrames
    dataframes = []
    
    # Read each CSV file and append it to the list
    for csv_file in csv_files:
        csv_path = os.path.join(csv_dir, csv_file)
        try:
            # Read the CSV file into a DataFrame
            df = pd.read_csv(csv_path)
            dataframes.append(df)
            print(f"Loaded {csv_file}")
        except Exception as e:
            print(f"Error loading {csv_file}: {e}")
    
    # Concatenate all DataFrames into one
    if dataframes:  # If there are DataFrames to concatenate
        combined_df = pd.concat(dataframes, ignore_index=True)
        
        # Save the combined DataFrame to a new CSV file
        combined_df.to_csv(output_file, index=False)
        print(f"Combined CSV saved to {output_file}")
    else:
        print("No CSV files found to combine.")

# Directory where your extracted CSV files are located
csv_dir = r'C:/Users/clee1/OneDrive - Fors Marsh/Desktop/FEVS'  # Replace with your actual directory path

# Output file where the combined CSV will be saved
output_file = r'C:/Users/clee1/OneDrive - Fors Marsh/Desktop/FEVS/combined_output.csv'  # Replace with the desired output file path

# Combine the csv files
combine_csv_files(csv_dir, output_file)

##Practice##

# #Check the total rows of the combined csv file
# df = pd.read_csv('C:/Users/clee1/OneDrive - Fors Marsh/Desktop/FEVS/combined_output.csv')

# #seems like the file is too large to read , other way ?
# csv_file = 'combined_output.csv'

# chunk_size = 100000

# chunks = []

# for chunk in pd.read_csv(csv_file, chunksize=chunk_size):
#     chunks.append(chunk)

# combined_df = pd.concat(chunks, ignore_index=True)

# print(f"Total number of rows: {len(combined_df)}")















































































