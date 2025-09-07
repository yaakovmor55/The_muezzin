from publishMetadataInKafka import config
import os

class ReadPath:
    def __init__(self, path=config.PATH):
        self.path = path
        self.files_and_dirs = os.listdir(self.path)
