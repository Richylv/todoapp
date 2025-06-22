import zipfile
import pathlib

def make_archive(filepaths,dest_dir):
    des_path = pathlib.Path(dest_dir,'compressed.zip')
    with zipfile.ZipFile(des_path ,'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath,arcname=filepath.name)

if __name__ == "__main__":
    make_archive(filepaths=['bonus.py','bonus8.py'], dest_dir='dest')