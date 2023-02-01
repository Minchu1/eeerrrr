import os
import shutil

from_dir="C:/Users/pgpra/Downloads"
to_dir="C:/Users/pgpra/OneDrive/Desktop/python/images"
list_of_files= os.listdir(from_dir)
print(list_of_files)
dir_tree={
    "image_files":[".jpg",".jpeg",".png",".gif",".jfif"],
    "video_files":[".mpg",".mp2",".mpeg",".mpe",".mpv",".mp4",".m4v",".avi",".mov"],
    "document_files":[".ppt",".csv",".exl",".txt",],
    "setup_files":[".exe",".bin",".cmd"],
}

def segregate_files(src_folder, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
        
    for filename in os.listdir(src_folder):
        file_path = os.path.join(src_folder, filename)
        extension = os.path.splitext(filename)[1]
        if extension:
            extension = extension[1:] # remove the leading "."
            sub_folder = os.path.join(dest_folder, extension)
            if not os.path.exists(sub_folder):
                os.makedirs(sub_folder)
            shutil.move(file_path, os.path.join(sub_folder, filename))

segregate_files('C:/Users/pgpra/Downloads', 'C:/Users/pgpra/OneDrive/Desktop/python/image')