from PIL import Image
import os


def convert(path_of_des, new_extension="jpg"):
    extensions_file_str = ".jpg, .jpeg, .png, .gif, .bmp, .tiff, .tif, .webp, .ico, .dds, .heif, .heic, .svg, .ai, .eps, .pdf, .raw, .cr2, .nef, .arw, .orf, .dng, .sr2, .psd, .xcf"
    extensions_file = [file.strip()[1:]
                       for file in extensions_file_str.split(",")]
    if os.path.exists(path_of_des) == False:
        os.mkdir(path_of_des)

    images = os.listdir("./temp")
    for img in images:
        if img.split(".")[1] in extensions_file:
            try:
                with Image.open(os.path.join("./temp", img)) as file:
                    name = img.split('.')[0] + "." + new_extension
                    file.save(os.path.join(path_of_des, name))
                print(f"Converted into {name}")
            except:
                print(f"Error when converted into {name}")
                pass

    for img in os.listdir("./temp"):
        os.remove(os.path.join("./temp", img))
    os.rmdir("./temp")
