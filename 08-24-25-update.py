import os
import re

# Directory to run in
directory = "./"   # current folder
date_prefix = "08-24-25"  # change this to the prefix you want

# Regex to match MM-DD-YY at start
pattern = re.compile(r"^\d{2}-\d{2}-\d{2}-")

for filename in os.listdir(directory):
    old_path = os.path.join(directory, filename)
    if os.path.isfile(old_path):
        # Skip files already starting with date format
        if not pattern.match(filename):
            new_filename = f"{date_prefix}-{filename}"
            new_path = os.path.join(directory, new_filename)
            print(f"Renaming: {filename} -> {new_filename}")
            os.rename(old_path, new_path)
