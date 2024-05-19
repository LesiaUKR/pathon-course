# python -m venv <name of the virtual environment> - створення віртуального середовища
# якщо вказати певну версію Python, то віртуальне середовище буде створене для цієї версії
# -m - запуск модуля як скрипта
# venv, .env, env - назви для віртуальних середовищ


# pip - Python package manager
# pip3 list - список встановлених пакетів Python глобально
# pip help install - допомога по команді install

# source .env/bin/activate - активація віртуального середовища
# .\.env\Scripts\activate.ps1 - активація віртуального середовища в Windows
# deactivate - вийти із віртуального середовища, опинимося в глобальному середовищі

# pip3 show moskali - інформація про пакет
# run_main - запустити головний файл

# pip freeze > requirements.txt - створення файлу зі списком пакетів по типу package.json в Node.js
# pip install -r requirements.txt - встановлення пакетів з файлу requirements.txt при встановленні нового проєкту

# poetry - надбудова над pip, трішки складніше, але краще, використовують для більших проєктів
# source ./venv/Scripts/activate - активація віртуального середовища в Windows в bash
# venv\Scripts\activate - активація віртуального середовища в Windows в cmd
