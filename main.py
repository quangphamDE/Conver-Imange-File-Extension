from modules.change_file_extension import convert
from modules.unzip import un_zip

zip_path = input("Enter path where zip file located: ")
output_path = input("Enter path where you want extract to: ")

un_zip(zip_path)
convert(output_path)
