import FreeSimpleGUI as sg
from zip import make_archive

compress_label = sg.Text('Select files to compress')
compress_input = sg.InputText('')
compress_btn = sg.FilesBrowse('Choose', key='files')

destination_label = sg.Text('Select destination folder: ')
destination_input = sg.InputText('')
destination_btn = sg.FolderBrowse('Choose',key='folder')

aceptar_btn = sg.Button('Compress')
output_label = sg.Text(key='output',text_color='green')

window = sg.Window('Compress File', layout=[[compress_label,compress_input,compress_btn],
                                            [destination_label,destination_input,destination_btn],
                                            [aceptar_btn, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values['files'].split(';')
    folder = values['folder']
    make_archive(filepaths,folder)
    window['output'].update(value='Compression complete')


window.close()