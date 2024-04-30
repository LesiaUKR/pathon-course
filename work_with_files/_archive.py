import shutil

# shutil - functions for copying and archiving files and directory trees.
# shutil - для копіювання, переміщення, перейменування та видалення файлів і директорій
# shutil підтримує архіви zip, tar, gz

print(shutil.get_archive_formats())

archive_file = shutil.make_archive(
    "work_with_files/photos", "zip", "work_with_files/picture")
print(archive_file)
shutil.unpack_archive("C:/Users/user/OneDrive/Документы/GitHub\python-course/work_with_files/photos.zip",
                      "C:/Users/user/OneDrive/Документы/GitHub/python-course/work_with_files/photos_unpacked")


# shutil.copy(src, dst) копіює файл з src в dst. Якщо dst є директорією,
# файл буде скопійований зі своїм поточним іменем у цю директорію.
# shutil.copytree(src, dst) - рекурсивно копіює всю директорію src в директорію dst.
# shutil.move(src, dst) - переміщує файл або директорію src в dst.
# shutil.rmtree(path) - рекурсивно видаляє директорію path.
# shutil.disk_usage(path) - повертає статистику використання диска, що містить загальний об'єм,
# використаний об'єм і вільний об'єм для даного шляху.
