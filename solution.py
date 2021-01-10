class FileReader:
    def __init__(self, path):
        self.path = path

    def read(self):
        try:
            with open(self.path, 'r') as file:
                result = str(file.read())
        except FileNotFoundError:
            result = ''
        finally:
            return result
