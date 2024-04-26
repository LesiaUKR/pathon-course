import shutil

# shutil - functions for copying and archiving files and directory trees.

print(shutil.get_archive_formats())

archive_file = shutil.make_archive(
    "work_with_files/photos", "zip", "work_with_files/picture")
print(archive_file)
shutil.unpack_archive("C:/Users/user/OneDrive/Документы/GitHub\python-course/work_with_files/photos.zip",
                      "C:/Users/user/OneDrive/Документы/GitHub/python-course/work_with_files/photos_unpacked")
