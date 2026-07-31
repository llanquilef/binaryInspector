import re
import subprocess


class BinaryInspector:
    def __init__(self, file_or_text: str):
        self.file_or_text = file_or_text

    def read_file(self):
        with open(self.file_or_text, 'rb') as file:
            # We need to read the first 8 characters to know his binaries
            binaries = file.read(8)
            return binaries

    def categorizer(self):
        byte_response = self.read_file()
        bytes_dictionary: dict = {
            'png': re.search(rb'\x89PNG\r\n\x1a\n', byte_response, re.S),
            'jpg': re.search(rb'\xff\xd8\xff\xdb\x00C\x00\x04', byte_response,
                             re.S),
        }
        for type_data in bytes_dictionary.keys():
            print(type_data)
            if type_data == 'png':
                print(type_data)
                return str(type_data)
            elif type_data == 'jpg':
                return str(type_data)
            elif type_data == 'pdf':
                return str(type_data)

    def process_by_type(self):
        commands: dict[str, list[str]] = {
            'jpg': ['exiftool', self.file_or_text]
        }
        for key, command in commands.items():
            category = self.categorizer()
            print(category)
            if category == 'jpg':
                print(command)
                with open('log.txt', 'w', encoding='utf-8') as log:
                    subprocess.run(command,
                                   stdout=log
                                   )


if __name__ == '__main__':
    tool = BinaryInspector(file_or_text='cat.jpg')
    tool.read_file()
    tool.categorizer()
    # tool.process_by_type()
