# Jan 7, 2023
# Author: Tyapkin P.S.

#TODO: 1. Add languages, styles
#TODO: 2. Styles (GOST, MAI...)
#TODO: 3. Type (Articles, Books...)
#TODO: 4. Refactoring
#TODO: 5. Save references to .txt & excel table

# import pandas as pd
# import numpy as np
# import re
import PySimpleGUI as sgui

sgui.theme('Dark')

TextLineWidth = 13
InputTextLineWidth = 45
ComboLineWidth = 43

ComboListStyle = ["ГОСТ Р 7.0.5-2008 \"Труды МАИ\"", "ГОСТ"]
ComboListStyleDefault = ComboListStyle[0]

ComboListType = ["Статья, RUS", "Статья, EN", "Книга, RUS", "Книга, EN"]
ComboListTypeDefault = ComboListType[0]

layout = [
    [sgui.Text('Стиль:', size=(TextLineWidth, 1)),
     sgui.Combo(values=ComboListStyle,
                default_value=ComboListStyleDefault,
                size=(ComboLineWidth, 1),
                readonly=True)],  # values[0]
    [sgui.Text('Тип материала:', size=(TextLineWidth, 1)),
     sgui.Combo(values=ComboListType,
                default_value=ComboListTypeDefault,
                size=(ComboLineWidth, 1),
                readonly=True)],  # values[1]
    [sgui.Text('Автор:', size=(TextLineWidth, 1)), sgui.InputText(size=(InputTextLineWidth, 1))],  # values[2]
    [sgui.Text('Название:', size=(TextLineWidth, 1)), sgui.InputText(size=(InputTextLineWidth, 1))],  # values[3]
    [sgui.Text('Год:', size=(TextLineWidth, 1)), sgui.InputText(size=(InputTextLineWidth, 1))],  # values[4]
    [sgui.Text('Город:', size=(TextLineWidth, 1)), sgui.InputText(size=(InputTextLineWidth, 1))],  # values[5]
    [sgui.Text('Издательство:', size=(TextLineWidth, 1)), sgui.InputText(size=(InputTextLineWidth, 1))],  # values[6]
    [sgui.Text('Том:', size=(TextLineWidth, 1)), sgui.InputText(size=(InputTextLineWidth, 1))],  # values[7]
    [sgui.Text('Страницы:', size=(TextLineWidth, 1)), sgui.InputText(size=(InputTextLineWidth, 1))],  # values[8]
    [sgui.Text('URL:', size=(TextLineWidth, 1)), sgui.InputText(size=(InputTextLineWidth, 1))],  # values[9]
    [sgui.Text('DOI:', size=(TextLineWidth, 1)), sgui.InputText(size=(InputTextLineWidth, 1))],  # values[10]
    [sgui.Checkbox('Добавить в таблицу'), sgui.Text('Выбрать табл.:', size=(TextLineWidth, 1)),  # values[11]
     sgui.FileBrowse("Загрузить")],
    [sgui.Submit("Сформировать", size=(47, 1)), sgui.Exit('Выйти')],
    [sgui.Output(key='-OUT-', size=(60, 10))]

]
window = sgui.Window('Формирователь списка лит. для Трудов МАИ (07.01.23)', layout)

while True:  # The Event Loop
    event, values = window.read()

    if event == 'Сформировать':

        outp_string = ""

        try:
            style = values[0]
            type = values[1]
            author = values[2]
            name = values[3]
            year = values[4]
            city = values[5]
            publisher = values[6]
            volume = values[7]
            pages = values[8]
            URL = values[9]
            DOI = values[10]

        except:
            print("Что-то введено не так..")

        if style == ComboListStyle[0]: # ГОСТ Р 7.0.5-2008 \"Труды МАИ\"
            if type == "Статья, RUS":
                if len(author):
                    outp_string += author + ' '
                if len(name):
                    outp_string += name + ' // '
                if len(publisher):
                    outp_string += publisher + '. '
                if len(year):
                    outp_string += year + '. '
                if len(volume):
                    outp_string += '№ ' + volume + '. '
                if len(pages):
                    outp_string += 'C. ' + pages + '. '
                if len(URL):
                    outp_string += 'URL: ' + URL
                if len(DOI):
                    if len(URL):
                        outp_string += '. '
                    outp_string += 'DOI: ' + DOI
            elif type == "Статья, EN":
                if len(author):
                    outp_string += author + ' '
                if len(name):
                    outp_string += name + '. '
                if len(publisher):
                    outp_string += publisher + ', '
                if len(year):
                    outp_string += year + ', '
                if len(volume):
                    outp_string += 'no. ' + volume + '. '
                if len(pages):
                    outp_string += 'pp. ' + pages + '. ' #TODO: проверить!
                if len(URL):
                    outp_string += 'URL: ' + URL
                if len(DOI):
                    if len(URL):
                        outp_string += '. '
                    outp_string += 'DOI: ' + DOI
        if len(outp_string):
            print(outp_string)

    if event in (None, 'Выйти', 'Cancel'):
        break
