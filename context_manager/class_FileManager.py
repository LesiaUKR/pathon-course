from contextlib import contextmanager


class FileManager:

    def __init__(self, filename, mode='w', encoding='utf-8'):
        self.file = None
        self.opened = False
        self.filename = filename
        self.mode = mode
        self.encoding = encoding

    def __enter__(self):
        self.file = open(self.filename, self.mode, encoding=self.encoding)
        self.opened = True
        print("Відкриваємо файл", self.filename)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Завершення блоку with")
        if self.opened:
            print("Закриваємо файл", self.filename)
            self.file.close()
        self.opened = False


if __name__ == '__main__':
    with FileManager('new_file.txt') as f:
        f.write('Hello world!\n')
        f.write('The end\n')



