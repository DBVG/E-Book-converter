import os
from os import listdir, rename
from os.path import isfile, join
import subprocess
from unicodedata import name

################################ folder paths##################################
# ( Provide path of folder containing files to be converted to E-Book)
m_folder_path = "C:/Users/c/Downloads/ebooks/" 

# ( Name your folder for finished file)
f_file_folder = "kindle"

# ( name the folder where processed files will be moved to, clearing the downloaded folder)
mypath_processed = "processed"  

# list of extensions that needs to be ignored.
ignored_extensions = ["pdf"]

#################################################################################

def main(a,b,c,d):
    # Main program
    raw_files = [f for f in listdir(a) if isfile(join(a, f))]
    converted_files = [f for f in listdir(os.path.join(a, b)) if isfile(join(os.path.join(a, b), f))]

    # return name of file to be kept after conversion.
    # we are just changing the extension. azw3 here.
    def get_final_filename(f):
        f = f.split(".")
        filename = ".".join(f[0:-1])
        processed_file_name = filename+".azw3"
        return processed_file_name


    # return file extension. pdf or epub or mobi
    def get_file_extension(f):
        return f.split(".")[-1]

    for f in raw_files:
        final_file_name = get_final_filename(f)
        extension = get_file_extension(f)
        if final_file_name not in converted_files and extension not in c:
            print("Converting : "+f)
            try:
                subprocess.call(["ebook-convert", a+f, os.path.join(a, b)+final_file_name])
                s = rename(a+f, os.path.join(a, d)+f)
                print(s)
            except Exception as e:
                print(e)
        else:
            print("Already exists : "+final_file_name)


if __name__=="__main__":
    main(m_folder_path,f_file_folder,ignored_extensions,mypath_processed)