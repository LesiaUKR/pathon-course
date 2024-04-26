
import shutil

# Копіюємо файл
# файл, який буде скопійовано
# source_file = 'work_with_files/photos_unpacked/bot-icon.png'
# destination_dir = 'work_with_files/'  # куди скопіювати файл
# shutil.copy(source_file, destination_dir)

# Копіюємо всю директорію
source_dir = 'work_with_files/photos_unpacked'
destination_dir = 'work_with_files/pictures'
shutil.copytree(source_dir, destination_dir)
