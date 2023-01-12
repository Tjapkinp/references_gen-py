# Jan 12, 2023
# Author: Tyapkin P.S.

# TODO: 1. Add languages
# TODO: 2. OnForm.styles (GOST, MAI...)
# TODO: 3. OnForm.type (Articles, Books...)
# TODO: 5. Save references to .txt & excel table / csv

import PySimpleGUI as sGUI


class ParamsGUI:
    text_line_width = 13
    input_text_line_width = 45
    combo_line_width = 43
    combo_list_standard = ["ГОСТ Р 7.0.5-2008 \"Труды МАИ\"", "ГОСТ"]
    combo_list_standard_default = combo_list_standard[0]
    combo_list_type = ["Статья, RUS", "Статья, EN", "Книга, RUS", "Книга, EN"]
    combo_list_type_default = combo_list_type[0]


# theme_name_list = sGUI.theme_list()
# print(theme_name_list)

def generate_ref_gost_r_7_0_5_2008(std=ParamsGUI.combo_list_standard[0], reference_type="Статья, RUS", author="",
                                   ref_name="", publisher="", city="", year="", volume="", pages="", url="", doi=""):
    generated_string = ""
    if std == ParamsGUI.combo_list_standard[0]:  # ГОСТ Р 7.0.5-2008 \"Труды МАИ\"
        if reference_type == ParamsGUI.combo_list_type[0]:  # "Статья, RUS"
            if len(author):
                generated_string += author + ' '
            if len(ref_name):
                generated_string += ref_name + ' // '
            if len(publisher):
                generated_string += publisher + '. '
            if len(year):
                generated_string += year + '. '
            if len(volume):
                generated_string += '№ ' + volume + '. '
            if len(pages):
                generated_string += 'C. ' + pages + '. '
            if len(url):
                generated_string += 'URL: ' + url
            if len(doi):
                if len(url):
                    generated_string += '. '
                generated_string += 'DOI: ' + doi
        elif reference_type == "Статья, EN":
            if len(author):
                generated_string += author + ' '
            if len(ref_name):
                generated_string += ref_name + '. '
            if len(publisher):
                generated_string += publisher + ', '
            if len(year):
                generated_string += year + ', '
            if len(volume):
                generated_string += 'no. ' + volume + '. '
            if len(pages):
                generated_string += 'pp. ' + pages + '. '  # TODO: проверить!
            if len(url):
                generated_string += 'URL: ' + url
            if len(doi):
                if len(url):
                    generated_string += '. '
                generated_string += 'DOI: ' + doi
        # Советов Б.Я., Яковлев С.А. Моделирование систем. – М.: Высшая школа, 1985. – 271 с.
        # Паничев В.В., Соловьев Н.А. Компьютерное моделирование. – Оренбург: ГОУ ОГУ, 2008. – 130 с.
        elif reference_type == "Книга, RUS":  # TODO: проверить на статьях!
            if len(author):
                generated_string += author + ' '
            if len(ref_name):
                generated_string += ref_name + '. '
            if len(city):
                generated_string += '– ' + city
            if len(publisher):
                generated_string += ': ' + publisher + ', '
            if len(year):
                generated_string += year + '. '
            # if len(OnForm.volume_edit_text):
            #    generated_string += 'no. ' + OnForm.volume_edit_text + '. '
            if len(pages):
                generated_string += '– ' + pages + ' с. '
            if len(url):
                generated_string += 'URL: ' + url
            if len(doi):
                if len(url):
                    generated_string += '. '
                generated_string += 'DOI: ' + doi
        elif type == "Книга, EN":  # TODO:!!!
            if len(author):
                generated_string += author + ' '
            if len(ref_name):
                generated_string += ref_name + '. '
            if len(city):
                generated_string += ' – ' + city
            if len(publisher):
                generated_string += ': ' + publisher + ', '
            if len(year):
                generated_string += year + '. '
            # if len(OnForm.volume_edit_text):
            #    generated_string += 'no. ' + OnForm.volume_edit_text + '. '
            if len(pages):
                generated_string += '– ' + pages + ' с. '
            if len(url):
                generated_string += 'URL: ' + url
            if len(doi):
                if len(url):
                    generated_string += '. '
                generated_string += 'DOI: ' + doi
    return generated_string


class OnForm:
    sGUI.theme('Dark')
    form_pos = 0
    standard_textbox = sGUI.Text('Стиль/стандарт:', size=(ParamsGUI.text_line_width, 1))
    standard_combo = sGUI.Combo(values=ParamsGUI.combo_list_standard,
                                default_value=ParamsGUI.combo_list_standard_default,
                                size=(ParamsGUI.combo_line_width, 1),
                                readonly=True)
    standard_edit_text = ""
    standard_combo_read_pos = form_pos
    form_pos += 1

    reference_type_textbox = sGUI.Text('Тип источника:', size=(ParamsGUI.text_line_width, 1))
    reference_type_combo = sGUI.Combo(values=ParamsGUI.combo_list_type,
                                      default_value=ParamsGUI.combo_list_type_default,
                                      size=(ParamsGUI.combo_line_width, 1),
                                      readonly=True)
    reference_type_edit_text = ""
    reference_type_combo_read_pos = form_pos
    form_pos += 1

    author_textbox = sGUI.Text('Автор/авторы:', size=(ParamsGUI.text_line_width, 1))
    author_edit = sGUI.InputText(size=(ParamsGUI.input_text_line_width, 1))
    author_edit_text = ""
    author_read_pos = form_pos
    form_pos += 1

    ref_name_textbox = sGUI.Text('Название:', size=(ParamsGUI.text_line_width, 1))
    ref_name_edit = sGUI.InputText(size=(ParamsGUI.input_text_line_width, 1))
    ref_name_edit_text = ""
    ref_name_read_pos = form_pos
    form_pos += 1

    city_textbox = sGUI.Text('Город:', size=(ParamsGUI.text_line_width, 1))
    city_edit = sGUI.InputText(size=(ParamsGUI.input_text_line_width, 1))
    city_edit_text = ""
    city_readpos = form_pos
    form_pos += 1

    publisher_textbox = sGUI.Text('Издательство:', size=(ParamsGUI.text_line_width, 1))
    publisher_edit = sGUI.InputText(size=(ParamsGUI.input_text_line_width, 1))
    publisher_edit_text = ""
    publisher_read_pos = form_pos
    form_pos += 1

    volume_textbox = sGUI.Text('Том издания:', size=(ParamsGUI.text_line_width, 1))
    volume_edit = sGUI.InputText(size=(ParamsGUI.input_text_line_width, 1))
    volume_edit_text = ""
    volume_read_pos = form_pos
    form_pos += 1

    year_textbox = sGUI.Text('Год:', size=(ParamsGUI.text_line_width, 1))
    year_edit = sGUI.InputText(size=(ParamsGUI.input_text_line_width, 1))
    year_edit_text = ""
    year_read_pos = form_pos
    form_pos += 1

    pages_textbox = sGUI.Text('Страницы:', size=(ParamsGUI.text_line_width, 1))
    pages_edit = sGUI.InputText(size=(ParamsGUI.input_text_line_width, 1))
    pages_edit_text = ""
    pages_read_pos = form_pos
    form_pos += 1

    url_textbox = sGUI.Text('URL:', size=(ParamsGUI.text_line_width, 1))
    url_edit = sGUI.InputText(size=(ParamsGUI.input_text_line_width, 1))
    url_edit_text = ""
    url_read_pos = form_pos
    form_pos += 1

    doi_textbox = sGUI.Text('DOI:', size=(ParamsGUI.text_line_width, 1))
    doi_edit = sGUI.InputText(size=(ParamsGUI.input_text_line_width, 1))
    doi_edit_text = ""
    doi_read_pos = form_pos
    form_pos += 1

    add_2_table_is_checked = ""
    add_2_table_checkbox = sGUI.Checkbox('Добавить в таблицу')
    add_2_table_read_pos = form_pos
    form_pos += 1

    load_table_text = sGUI.Text('Выбрать табл.:', size=(ParamsGUI.text_line_width, 1))
    load_table_btn = sGUI.FileBrowse("Загрузить")
    ref_generate_btn = sGUI.Submit("Сформировать", size=(47, 1))
    exit_btn = sGUI.Exit('Выйти')

    results_memo = sGUI.Output(key='-OUT-', size=(60, 10))


def form_init():
    layout = [[OnForm.standard_textbox, OnForm.standard_combo],
              [OnForm.reference_type_textbox, OnForm.reference_type_combo],
              [OnForm.author_textbox, OnForm.author_edit],
              [OnForm.ref_name_textbox, OnForm.ref_name_edit],
              [OnForm.city_textbox, OnForm.city_edit],
              [OnForm.publisher_textbox, OnForm.publisher_edit],
              [OnForm.volume_textbox, OnForm.volume_edit],
              [OnForm.year_textbox, OnForm.year_edit],
              [OnForm.pages_textbox, OnForm.pages_edit],
              [OnForm.url_textbox, OnForm.url_edit],
              [OnForm.doi_textbox, OnForm.doi_edit],
              [OnForm.add_2_table_checkbox, OnForm.load_table_text, OnForm.load_table_btn],
              [OnForm.ref_generate_btn, OnForm.exit_btn],
              [OnForm.results_memo]]

    form_window = sGUI.Window('Формирователь списка лит. для Трудов МАИ (11.01.23)', layout)
    return form_window


main_form = form_init()

while True:  # The Event Loop
    event, values = main_form.read()

    if event == 'Сформировать':

        generated_string = ""

        try:
            OnForm.standard_edit_text = values[OnForm.standard_combo_read_pos]
            OnForm.reference_type_edit_text = values[OnForm.reference_type_combo_read_pos]
            OnForm.author_edit_text = values[OnForm.author_read_pos]
            OnForm.ref_name_edit_text = values[OnForm.ref_name_read_pos]
            OnForm.year_edit_text = values[OnForm.year_read_pos]
            OnForm.city_edit_text = values[OnForm.city_readpos]
            OnForm.publisher_edit_text = values[OnForm.publisher_read_pos]
            OnForm.volume_edit_text = values[OnForm.volume_read_pos]
            OnForm.pages_edit_text = values[OnForm.pages_read_pos]
            OnForm.url_edit_text = values[OnForm.url_read_pos]
            OnForm.doi_edit_text = values[OnForm.doi_read_pos]
        except():
            print("Что-то введено не так..")

        ref_str = generate_ref_gost_r_7_0_5_2008(std=OnForm.standard_edit_text,
                                                 reference_type=OnForm.reference_type_edit_text,
                                                 author=OnForm.author_edit_text,
                                                 ref_name=OnForm.ref_name_edit_text,
                                                 publisher=OnForm.publisher_edit_text,
                                                 city=OnForm.city_edit_text,
                                                 year=OnForm.year_edit_text,
                                                 volume=OnForm.volume_edit_text,
                                                 pages=OnForm.pages_edit_text,
                                                 url=OnForm.url_edit_text,
                                                 doi=OnForm.doi_edit_text)

        if len(ref_str):
            print(ref_str)

    if event in (None, 'Выйти', 'Cancel'):
        break
