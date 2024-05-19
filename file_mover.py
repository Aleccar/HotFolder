from library import *
import os 
import shutil


class FileMover:
    def file_mover_commit(self):
        for file in files_in_directory:
            #file_path = os.path.abspath(file)

            if file.find(".") >= 0:
                stripped_string = file[file.find(".") + 1:]
                new_sort = sorting_directory + f"\{file}"

                for keys, values in sorting_dict.items():
                    if values in files_in_directory:
                        if stripped_string in keys:
                            other_sort = sorting_directory + f"\\{sorting_dict[keys]}"
                            print(f"The files from \"{new_sort}\" have been moved to \"{other_sort}\".")
                            shutil.move(new_sort, other_sort)

moving_files = FileMover()
moving_files.file_mover_commit()