import PySimpleGUI as sg
sg.theme("DarkGrey12")
sg.theme_text_color("#66CDAA")
window = sg.Window(title="profile",
                   layout=[[sg.Text("SELAMAT DATANG DI KELAS",
                                    font=("Arial",25,"italic","bold", "underline"))],
                           [sg.Text("NPM        : 2210010370 ")],
                           [sg.Text("Nama       : Erni Fitriani ")],
                           [sg.Text("Kelas      : 5P Reguler Banjarmasin ")]
                           ],
                           size=(550,200),
                           font=("Times", 18))
window()
window.close()