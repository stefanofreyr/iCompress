import FreeSimpleGUI as sg
from zip_creator import make_archive

file_label = sg.Text("Files to compress:")
file_input = sg.Input(tooltip="Enter a file path")
button1 = sg.FilesBrowse("Choose", key='files')

folder_label = sg.Text("Destination folder:")
folder_input = sg.Input(tooltip="Enter a folder path")
button2 = sg.FolderBrowse("Choose", key='folder')

compress_button = sg.Button("Convert")
output_label = sg.Text(key='output')

window = sg.Window("iCompress", layout=[
    [file_label,file_input,button1],
    [folder_label,folder_input,button2],
    [compress_button, output_label]])

while True:
    event, values = window.read()
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["output"].update(value="Files compressed successfully.")

window.close()