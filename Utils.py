import os, sys
import hashlib
from SqlHandler import SqlHandler

class Utils:
    def __init__(self, connector=None) -> None:
        if not connector:
            self.connector = SqlHandler()
        self.janela = None

    @staticmethod
    def get_base_path():
        return os.path.dirname(os.path.abspath(sys.argv[0]))

    @staticmethod
    def generate_md5(text: str):
        return hashlib.md5(text.encode('utf-8')).hexdigest()

    def get_connection(self):
        return self.connector

if __name__ == "__main__":
    import Main

    Main