import os
import zipfile


def un_zip(path_of_zip):
    if os.path.exists("./temp") == False:
        os.mkdir("./temp")

    zip_files = os.listdir(path_of_zip)
    for zip_file in zip_files:
        if zip_file.split(".")[1] == 'zip':
            with zipfile.ZipFile(os.path.join(path_of_zip, zip_file), 'r') as file:
                folder_name = zip_file.split(".")[0]
                file.extractall(os.path.join("./temp", folder_name))
