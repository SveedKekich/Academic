import re

class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def write(self, data_list):
        with open(self.filename, 'w', encoding='utf-8') as f:
            for obj in data_list:
                f.write(obj.info() + "\n")

    def read(self):
        with open(self.filename, 'r', encoding='utf-8') as f:
            return f.readlines()
