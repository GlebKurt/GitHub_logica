import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QListWidgetItem
from ui import Ui_MainWindow


class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.load_data()

    def load_data(self):
        try:
            with open('notes_data.json', 'r', encoding='utf-8') as file:
                self.notes = json.load(file)
        except(FileNotFoundError, json.JSONDecodeError):
            self.notes = {}
        self.ui.listWidget.addItems(self.notes.keys())


def add_note(self):
    note_name, ok = QInputDialog.getText(self, 'Створити замітку', 'Назва замітки:')
    if ok and note_name != '':
        if note_name not in self.notes:
            self.notes[note_name] = {'текст': '', 'теги': []}
            self.ui.listWidget.addItem(note_name)


app = QApplication([])
ex = Widget()
ex.show()
app.exec_()
