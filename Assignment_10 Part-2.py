"""5. Create a programme that searches a folder tree for files with
a certain file extension (such as .pdf or .jpg).
Copy these files from whatever location they are in to a new folder."""

import shutil, os
import logging

logging.basicConfig(filename='folder.log',level=logging.INFO )

def Directory_walk(folder):
    for folderName, subfolders, filenames in os.walk(folder):
        print('The current folder is ' + folderName)
        for subfolder in subfolders:
            print('Subfolder of ' + folderName + ': ' + subfolder)
            for filename in filenames:
                print('File inside ' + folderName + ': ' + filename)
                if filename.endswith('.pdf'):
                    shutil.copytree(folder + filename, '<New folder>')

    try:
        logging.info('Trying to copy file content')

    except Exception as e:
            logging.exception(e)
            print(e)

    return '<New folder>'