import os
from zipfile import ZipFile, ZIP_DEFLATED
class PhotoManager:
    def __init__(self, zip_file, folder_path):
        self.zip_path = zip_file
        self.folder_path = folder_path
        self.archive_name = self.zip_path.split('/')[-1][:-4]
        self.size = 10000000
    def unarchive(self):
        with ZipFile(self.zip_path, 'r') as zip_ref:
            zip_ref.extractall(self.folder_path)
    def process(self):
        files = os.listdir(self.folder_path)
        os.chdir(self.folder_path)
        index = self.make_archive(files)
        files = os.listdir(self.folder_path)
        curr_size = 0
        curr_files = []
        for photo in files:
            if photo.split('.')[-1] =='jpg':
                if curr_size + os.path.getsize(photo) < self.size:
                    curr_size += os.path.getsize(photo)
                    curr_files.append(photo)
                else:
                    zipf = ZipFile('/'.join([self.folder_path,f"{self.archive_name}_{index}.zip"]), 'w', ZIP_DEFLATED)
                    for file_ in curr_files: 
                        zipf.write(file_)
                    for file_ in curr_files: 
                        os.unlink('/'.join([self.folder_path,file_]))
                    curr_size = 0
                    curr_files = []
                    index += 1
                    break
        else:
            zipf = ZipFile('/'.join([self.folder_path,f"{self.archive_name}_{index}.zip"]), 'w', ZIP_DEFLATED)
            for file_ in curr_files: 
                zipf.write(file_)
            for file_ in curr_files: 
                os.unlink('/'.join([self.folder_path,file_]))
            curr_size = 0
            curr_files = []
            index += 1
    def make_archive(self, files):
        curr_size = 0
        curr_files = []
        index = 0
        for photo in files:
            if curr_size + os.path.getsize(photo) < self.size:
                curr_size += os.path.getsize(photo)
                curr_files.append(photo)
            else:
                zipf = ZipFile('/'.join([self.folder_path,f"{self.archive_name}_{index}.zip"]), 'w', ZIP_DEFLATED)
                for file_ in curr_files: 
                    zipf.write(file_)
                for file_ in curr_files: 
                    os.unlink('/'.join([self.folder_path,file_]))
                curr_size = os.path.getsize(photo)
                curr_files = [photo]
                index += 1
        return index
    def clear(self):
        os.unlink(self.zip_path)
    def run(self):
        self.unarchive()
        self.process()
        self.clear()
