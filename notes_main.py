from PyQt5.QtCore import Qt
from  PyQt5.QtWidgets import QInputDialog, QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QMessageBox, QGroupBox, QTextEdit, QListWidget, QLineEdit
import json

app = QApplication([])
menu = QWidget()
menu.setWindowTitle('Умные замекти')
question = QLabel('Кто является основателем компании SpaceX?')

main_layout = QHBoxLayout() #главный лэйаут
layoutV1 = QVBoxLayout()
layoutV2 = QVBoxLayout()
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()
layoutH4 = QHBoxLayout()
layoutH5 = QHBoxLayout()
layoutH6 = QHBoxLayout()
layoutH7 = QHBoxLayout()

menu_write = QTextEdit()
list_with_notes = QListWidget()
create_new_note = QPushButton('Создать заметку')
delete_note = QPushButton('Удалить заметку')
save_note = QPushButton('Сохранить заметку')
list_with_tags = QListWidget()
find_tag = QLineEdit()
add_to_note = QPushButton('Добавить к заметке')
delete_from_note = QPushButton('Открепить от заметки')

layoutV1.addWidget(menu_write)
layoutH1.addWidget(list_with_notes)
layoutH2.addWidget(create_new_note)
layoutH2.addWidget(delete_note)
layoutH3.addWidget(save_note)
layoutH4.addWidget(list_with_tags)
layoutH5.addWidget(find_tag)
layoutH6.addWidget(add_to_note)
layoutH6.addWidget(delete_from_note)
layoutV2.addLayout(layoutH1)
layoutV2.addLayout(layoutH2)
layoutV2.addLayout(layoutH3)
layoutV2.addLayout(layoutH4)
layoutV2.addLayout(layoutH5)
layoutV2.addLayout(layoutH6)
layoutV2.addLayout(layoutH7)
main_layout.addLayout(layoutV1)
main_layout.addLayout(layoutV2)
menu.setLayout(main_layout)

notes = {
    "О планетах":
  
    { "текст" : "Что если на Марсе есть жизнь?",
      "теги": ["Марс, Гипотезы"]
    },
    "Очёрных дырах":
    {
        "текст": "Сингулярность на горизонте событий отсутствует",
        "теги": ["Чёрные дыры", "Факты"]
    }
}

with open("notes.json", "w", encoding = "utf8") as file:
    json.dump(notes, file)

def create_note():
    note_name,result = QInputDialog.getText(
        menu, "Добавить заметку", "Название заметки:")
    notes[note_name] = {'текст': '', 'теги': []}
    list_with_notes.addItem(note_name)

def show_note():
    name = list_with_notes.selectedItems()[0].text()
    menu_write.setText(notes[name]['текст'])
    list_with_tags.clear()
    list_with_tags.addItems(notes[name]['теги'])

list_with_notes.itemClicked.connect(show_note)    

def save_notes():
    if list_with_notes.selectedItems():
        name = list_with_notes.selectedItems()[0].text()
        noteText = menu_write.toPlainText()
        notes[name]['текст'] = noteText
        with open("notes.json", "w", encoding = "utf8") as file:
            json.dump(notes, file)


def del_note():
    if list_with_notes.selectedItems():
        name = list_with_notes.selectedItems()[0].text()
        del notes[name]
        with open("notes.json", "w", encoding = "utf8") as file:
            json.dump(notes, file)
        list_with_notes.clear()   
        list_with_notes.addItems(notes) 
        menu_write.clear()
        list_with_tags.clear()

def add_to_notes():
    if list_with_notes.selectedItems():
        name = list_with_notes.selectedItems()[0].text()
        tagText = find_tag.text()
        if  not tagText in notes[name]['теги']:
            notes[name]['теги'].append(tagText)
            list_with_tags.addItem(tagText)
            find_tag.clear()
        with open("notes.json", "w", encoding = "utf8") as file:
            json.dump(notes, file)



def delete_from_notes():
    if list_with_notes.selectedItems():
        name = list_with_notes.selectedItems()[0].text()
        tag_name = list_with_tags.selectedItems()[0].text()
        notes[name]['теги'].remove(tag_name)
        with open("notes.json", "w", encoding = "utf8") as file:
            json.dump(notes, file)   
        list_with_tags.clear()
        list_with_tags.addItems(notes[name]['теги']) 

#Связывание кнопок, выполняющих функции с функцией
create_new_note.clicked.connect(create_note)
list_with_notes.itemClicked.connect(show_note)
save_note.clicked.connect(save_notes) 
delete_note.clicked.connect(del_note)
add_to_note.clicked.connect(add_to_notes)
delete_from_note.clicked.connect(delete_from_notes)

menu.show()

list_with_notes.addItems(notes)
app.exec_()