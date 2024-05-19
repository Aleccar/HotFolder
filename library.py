import os

# Here's the sorting directory, so all the files within this directory will be sorted into othger directories.
sorting_directory = r"c:\Users\Alecc\Desktop\File Sorter"

# Here are the keys and values of the file sorter:
# Keys will represent the file type
# Values will represent the directory of which they will be moved to
sorting_dict = {
"pdf": "PDFs",
"avi": "Videos",
"gif": "Images",
"png": "Images",
"jpg": "Images",
"jpeg": "Images",
"mp3": "Audio Files",
"mp4": "Videos",
"mov": "Videos",
"rar": "Compressed Files",
"zip": "Compressed Files",
"txt": "Document Files",
"wav": "Audio Files",
"doc": "Document Files",
"docx": "Document Files",
"exe": "Executable Files"
}


files_in_directory = os.listdir(sorting_directory)
