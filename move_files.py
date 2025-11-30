# This scripts caaptures step by step how to move files into respective json  and csv folders in the repository 
# It follows 2 methods.-
# Creating directories through the terminal using mkdir
#  creating file list in the directo and moving the content of the list to designated folders

# option 2 uses python modules to create folders and move files into thes folders.


#solution1


#define a function that tacks the files 

#import os and shutil for creating and moving directories and files  
# import os
# import shutil


# #create a list 


# files = [
#     "business-financial-data.csv",
#     "economic-survey.csv",
#     "research-and-development.csv",
#     "report.txt",
#     "colors.json",
#     "books.json",
#     "employees.json",
#     "report.csv"
# ]


# # creating a function that first checks existence of csv,json folders


# def move_files(file_list):
#     # Ensure destination folders exist
#     os.makedirs("csv", exist_ok=True)
#     os.makedirs("json", exist_ok=True)

#     for file in file_list:
#         if not os.path.exists(file):
#             print(f"❌ File not found: {file}")
#             continue

#         ext = os.path.splitext(file)[1].lower()

#         if ext == ".csv":
#             shutil.move(file, "csv/")
#             print(f"📁 Moved {file} → csv/")
#         elif ext == ".json":
#             shutil.move(file, "json/")
#             print(f"📁 Moved {file} → json/")
#         else:
#             print(f"⚠️ Skipped {file} (unsupported file type)")



# move_files(files)


#option 2 

#create a list 

import os
import shutil

directory = r"c:\Users\USER\python_file_organizer"
# file_type = [
#     "business-financial-data.csv",
#     "economic-survey.csv",
#     "research-and-development.csv",
#     "report.txt",
#     "colors.json",
#     "books.json",
#     "employees.json",
#     "report.csv"
# ]
file_type = {
    "csv": [".csv"],
    "json": [".json"],
    "txt": [".txt"]
}

#to create folders:
def create_folders(base_folder,folders):
    for folder in folders:
        folder_path = os.path.join(base_folder,folder)
        if not os.path.exists(folder_path):
         os.makedirs(folder_path)

# organise file by file_type:

def organise_file_by_filetype(base_folder,file_type):
    for filename in os.listdir(base_folder):
        #find filepath 
        file_path = os.path.join(base_folder,filename)
        ##check if this filepath is a folder
        if os.path.isdir(file_path):
            continue # skips and goes into the next iteration

        #check file type and move to appropriate folder
        # to get extension
        ext = os.path.splitext(filename)[-1].lower()
        for folder, extensions in file_type.items():
            if ext in extensions:
                target_folder = os.path.join(base_folder,folder)
                shutil.move(file_path, target_folder)
                print(f"moved {filename} to {folder}")
                break


#calling functions:
create_folders(directory,file_type.keys())

organise_file_by_filetype(directory,file_type)




