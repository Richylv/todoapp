import FreeSimpleGUI as sg

compress_label = sg.Text('Select files to compress')
compress_input = sg.InputText('')
compress_btn = sg.FileBrowse('Choose')

destination_label = sg.Text('Select destination folder: ')
destination_input = sg.InputText('')
destination_btn = sg.FileBrowse('Choose')

aceptar_btn = sg.Button('Compress')

window = sg.Window('Compress File', layout=[[compress_label,compress_input,compress_btn],
                                            [destination_label,destination_input,destination_btn],
                                            [aceptar_btn]])
window.Read()
window.close()