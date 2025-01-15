from PIL import Image
import os


def convert(path_of_des, new_extension="jpg"):
    extensions_file_str = ".jpg, .jpeg, .png, .gif, .bmp, .tiff, .tif, .webp, .ico, .dds, .heif, .heic, .svg, .ai, .eps, .pdf, .raw, .cr2, .nef, .arw, .orf, .dng, .sr2, .psd, .xcf"
    extensions_file = [file.strip()[1:]
                       for file in extensions_file_str.split(",")]
    if not os.path.exists(path_of_des):
        os.mkdir(path_of_des)

    # Lấy danh sách các thư mục con trong thư mục temp
    images_dir_tmp = os.listdir("./temp")
    images_dir = [os.path.join("./temp", img_dir)
                  for img_dir in images_dir_tmp]

    # Duyệt các thư mục con trong thư mục gốc
    for dir in images_dir:
        subfolder_name = os.path.basename(dir)
        dest_subfolder = os.path.join(path_of_des, subfolder_name)
        if not os.path.exists(dest_subfolder):
            os.makedirs(dest_subfolder)
        # Duyệt qua từng tệp trong mỗi thư mục con
        for img in os.listdir(dir):
            if img.split(".")[-1].lower() in extensions_file:
                try:
                    img_path = os.path.join(dir, img)
                    with Image.open(img_path) as file:
                        name = img.split('.')[0] + "." + new_extension
                        file.save(os.path.join(dest_subfolder, name))
                    print(f"Converted {img} into \
                          {os.path.join(dest_subfolder, name)}")
                except Exception as e:
                    print(f"Error processing {img}: {e}")

    # Xóa tất cả tệp trong thư mục temp và thư mục con
    for dir in images_dir:
        for img in os.listdir(dir):
            os.remove(os.path.join(dir, img))
        os.rmdir(dir)

    # Xóa thư mục temp
    os.rmdir("./temp")
