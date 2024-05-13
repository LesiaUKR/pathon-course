from contextlib import contextmanager


@contextmanager
def file_manager(filename, mode='w', encoding='utf-8'):
    print("Відкриваємо файл", filename)
    file = open(filename, mode, encoding=encoding)
    try:
        yield file
    finally:
        print("Закриваємо файл", filename)
        file.close()
        print("Завершення блоку with")


if __name__ == '__main__':
    with file_manager('new_file.txt') as f:
        f.write('Hello world!\n')
        f.write('The end\n')
