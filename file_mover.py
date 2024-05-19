from hot_folder_library import files_in_directory
from hot_folder_library import sorting_directory
from hot_folder_library import sorting_dict
import os 
import shutil



class FileMover:
    def file_mover_commit(self):
        for file in files_in_directory:
            file_path = os.path.abspath(file)

            if file.find(".") >= 0:
                stripped_string = file[file.find(".") + 1:]
                new_sort = sorting_directory + f"\{file}"
                #print(new_sort)

                for keys, values in sorting_dict.items():
                    if stripped_string in keys:
                        other_sort = sorting_directory + f"\{sorting_dict[keys]}"
                        print(f"The files from \"{new_sort}\" have been moved to \"{other_sort}\".")
                        shutil.move(new_sort, other_sort)

moving_files = FileMover()
moving_files.file_mover_commit()