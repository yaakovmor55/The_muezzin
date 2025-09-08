import datetime
from pathlib import Path



class ExportMetadata:
    def __init__(self, path):
        self.path = Path(path)



    def get_meta_data(self):
        file_name = str(self.path.stem)
        file_type = str(self.path.suffix)
        stats = self.path.stat()
        size_in_mb = str(stats.st_size / (1024 **2))[:4] + "MB"
        size_in_bytes = str(stats.st_size)
        creation_time = str(datetime.datetime.fromtimestamp(stats.st_ctime))
        modification_time = str(datetime.datetime.fromtimestamp(stats.st_mtime))
        meta_data =  {
            "file_name" : file_name,
            "file_type" : file_type,
            "size_in_MB" : size_in_mb,
            "size_in_bytes" : size_in_bytes,
            "creation_time" : creation_time,
            "modification_time" : modification_time
        }
        return meta_data


    def build_json(self):
        absolute_path = str(self.path.absolute())
        return {
            "path" : absolute_path,
            "metadata" : self.get_meta_data()
        }


