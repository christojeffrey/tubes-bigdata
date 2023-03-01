import zipfile
import os
import sys 
# Extract datetime.zip and add the extracted folder to sys.path
zip_ref = zipfile.ZipFile('datetime.zip', 'r')
zip_ref.extractall()
zip_ref.close()
sys.path.append(os.path.abspath('./datetime'))

# Do the same for os.zip
zip_ref = zipfile.ZipFile('os.zip', 'r')
zip_ref.extractall()
zip_ref.close()
sys.path.append(os.path.abspath('./os'))


