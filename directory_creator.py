from library import *
import os 
import shutil


class DirectoryCreator:
    def create_directory(self):
        for file in files_in_directory:
            stripped_string = file[file.find(".") + 1:]
            for keys, values in sorting_dict.items():
                if stripped_string in keys:
                    try:
                        path = os.path.join(sorting_directory, values)
                        os.mkdir(path + "\\")
                        print(f"The \"{values}\" directory has been created")
                    except:
                        continue

# create_directory = DirectoryCreator()
# create_directory.create_directory()