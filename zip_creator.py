import zipfile
import pathlib

def make_archive(filepaths, destination_dir):
    dest_path = pathlib.Path(destination_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as file:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            file.write(filepath, arcname=filepath.name)


if __name__ == '__main__':
    make_archive(filepaths=['/Users/stefanofreyr/Dropbox/Arabic Literature and Thought/Adab/Muqaddima Ibn Khaldun.pdf'], destination_dir='/Users/stefanofreyr/Documents/Molyo')