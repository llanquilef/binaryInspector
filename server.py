import re
import subprocess
# import subprocess


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
        bytes_dictionary = {
            'png': re.search(rb'\x89PNG\r\n\x1a\n', byte_response, re.S),
            'jpg': re.search(rb'\xff\xd8\xff\xdb\x00C\x00\x04', byte_response,
                             re.S),
            'gif': re.search(rb'GIF8[79]a', byte_response, re.S)
        }
        for key, match in bytes_dictionary.items():
            # If the binary of one type of file matches returns the key
            # of that type
            if match:
                return key

    def process_images(self):
        command = ['exiftool', self.file_or_text]
        with open('log.txt', 'w', encoding='utf-8') as log:
            subprocess.run(command,
                           stdout=log
                           )

    def process_by_type(self):
        category = self.categorizer()
        # Narrowing
        # With this we define that type of category can in some cases be None or str
        if category is None:
            return
        commands = {
            # This is the reference to the methods, in this case, his behavior
            #  its like objects
            'jpg': self.process_images,
            'png': self.process_images,
            'gif': self.process_images
        }
        handler = commands.get(category)
        if handler:
            # Then we call the reference of the function and then we execute
            handler()
        else:
            print('No existe método para el tipo del archivo')


if __name__ == '__main__':
    tool = BinaryInspector(file_or_text='cat.jpg')
    tool.read_file()
    tool.categorizer()
    tool.process_by_type()
