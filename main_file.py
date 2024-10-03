from create_task import *
from main_window import *
from redact_reward import *
from redact_und_tasks import *
from endtask import *
from create_item import *
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import json

und_tasks = {

}

reward_task = {

}

rares = ['обычный', 'редкий', 'легендарный', 'квестовый']


class Main():
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.close_main_win = False
        self.close_tasks = False

        self.reward1 = ''
        self.reward2 = ''

        self.message = QMessageBox()
        self.count_rows_und_tasks = 0
        self.create_json_file = True

        self.show_start_window()

    def show_start_window(self):

        self.Mainwin = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.Mainwin)
        self.Mainwin.show()

        self.event_main_win()
        sys.exit(self.app.exec_())

    def render_item_create_window(self):

        self.close_main_win = True
        if self.close_main_win:
            self.Mainwin.close()
            self.close_main_win = False

        self.ItemWin = QtWidgets.QMainWindow()
        self.ui = Ui_ItemWin()
        self.ui.setupUi(self.ItemWin)
        self.ItemWin.show()

        self.ui.create_task.clicked.connect(self.check_values_item)

    def check_values_item(self):
        if self.ui.nameitem.text() != '' and self.ui.path.text() != '' and self.ui.location.text() != '' and\
            self.ui.rare.text() in rares and self.ui.describe.text() != '' and self.ui.buy.text().isdigit() and\
            self.ui.sell.text().isdigit():
            self.create_json_item()
            self.render_endtask_win('item')
        else:
            self.blit_error_text('Не все поля заполнены корректно', 'Ошибка полей')

    def event_main_win(self):
        self.ui.create_task.clicked.connect(lambda: self.render_task_create())
        self.ui.create_item.clicked.connect(self.render_item_create_window)

    def render_task_create(self):
        self.close_main_win = True
        if self.close_main_win:
            self.Mainwin.close()
            self.close_main_win = False
        self.TaskCreate = QtWidgets.QMainWindow()
        self.ui = Ui_Taskwin()
        self.ui.setupUi(self.TaskCreate)
        self.TaskCreate.show()
        self.ui.label_3.setText(f"Подзаданий: {len(und_tasks)}")

        self.ui.create_und_task.clicked.connect(lambda: self.render_und_tasks_win())
        self.ui.button_reward.clicked.connect(lambda: self.render_reward_win())

        self.ui.create_task.clicked.connect(self.check_values_tasks)

    def render_und_tasks_win(self):
        global und_tasks
        self.close_tasks = True
        if self.close_tasks:
            self.TaskCreate.close()
            self.close_tasks = False
        self.UndTaskWin = QtWidgets.QMainWindow()
        self.ui = Ui_UndTasksWin()
        self.ui.setupUi(self.UndTaskWin)

        self.UndTaskWin.show()


        if len(und_tasks) != 0:

            self.ui.count = len(und_tasks)
            self.count_rows_und_tasks = len(und_tasks)
            self.ui.tableWidget.setRowCount(len(und_tasks))
            y = 0

            for key, value in und_tasks.items():

                item = QtWidgets.QTableWidgetItem()
                item.setText(str(key))
                # print(item)
                self.ui.tableWidget.setItem(y, 0, item)

                item = QtWidgets.QTableWidgetItem()
                item.setText(str(value))

                self.ui.tableWidget.setItem(y, 1, item)
                y += 1


        self.ui.create_btn.clicked.connect(lambda: self.add_und_task())
        self.ui.savebtn.clicked.connect(lambda: self.save_und_tasks())

    def add_und_task(self):
        self.ui.count += 1
        self.count_rows_und_tasks += 1
        self.ui.tableWidget.setRowCount(self.ui.count)

    def blit_error_text(self, text, type='Введено не все', icon=QMessageBox.Warning):
        self.message.setWindowTitle(type)
        self.message.setGeometry(525, 405, 200, 100)
        self.message.setText(text)
        self.message.setIcon(icon)
        self.message.setDefaultButton(QMessageBox.Retry)
        self.message.exec_()

    def save_und_tasks(self):
        global und_tasks


        for y in range(self.ui.count):

            und_tasks[self.ui.tableWidget.item(y, 0).text()] = self.ui.tableWidget.item(y, 1).text()



        self.UndTaskWin.close()
        self.close_tasks = False
        self.render_task_create()

    def render_reward_win(self):
        self.close_tasks = True
        if self.close_tasks:
            self.TaskCreate.close()
            self.close_tasks = False
        self.RewardWin = QtWidgets.QMainWindow()
        self.ui = Ui_RewardsWin()
        self.ui.setupUi(self.RewardWin)
        if len(reward_task) != 0:
            self.ui.countreward1.setText(reward_task[self.reward1])
            self.ui.countreward2.setText(reward_task[self.reward2])
            self.ui.reward1.setText(self.reward1)
            self.ui.reward2.setText(self.reward2)

        self.RewardWin.show()

        self.ui.savebtn.clicked.connect(self.return_to_task_from_reward)

    def return_to_task_from_reward(self):
        global reward_task
        reward_task[self.ui.reward1.text()] = self.ui.countreward1.text()
        reward_task[self.ui.reward2.text()] = self.ui.countreward2.text()

        self.reward1 = self.ui.reward1.text()
        self.reward2 = self.ui.reward2.text()

        self.RewardWin.close()
        self.render_task_create()

    def render_endtask_win(self, type='task'):


        self.close_tasks = True
        if self.close_tasks and type == 'task':
            self.TaskCreate.close()
            self.close_tasks = False
        elif self.close_tasks and type == 'item':
            self.ItemWin.close()
            self.close_tasks = False

        self.EndTaskWin = QtWidgets.QMainWindow()
        self.ui = Ui_EndTask()
        self.ui.setupUi(self.EndTaskWin)

        self.EndTaskWin.show()

        self.ui.showhere.clicked.connect(self.show_here_task)

        self.ui.exporting.clicked.connect(lambda: self.export_task_file(type))



    def create_json_item(self):

        self.json_data = {
            f'"{self.ui.nameitem.text()}"' : {
                "use" : self.ui.use.isChecked(),
                "name" : f"{self.ui.nameitem.text()}",
                "location" : f"{self.ui.location.text()}",
                "buy" : int(self.ui.buy.text()),
                "sell" : int(self.ui.sell.text()),
                "rare" : f'{self.ui.rare.text()}',
                "path" : f'{self.ui.path.text()}',
                "describe" : f'{self.ui.describe.text()}'
            }
        }

        self.string_json = '; '.join(
            [f'{key.capitalize()} : {value}' for key, value in self.json_data.items()]).replace(",", ",\n\t")
        self.string_json = self.string_json.replace("{", "{\n\t")
        self.string_json = self.string_json.replace("}", "\n\t}")
        self.string_json = self.string_json.replace("False", "false")
        self.string_json = self.string_json.replace("True", "true")
        self.string_json = self.string_json.replace("'", "\"")
        print(self.string_json)

    def create_json_task(self):
        self.json_data = {
            f'"{self.ui.nametask.text()}"' : {
                "by" : self.ui.taskfrom.text(),
                "status" : False,
                "task" : {
                    key : {
                        "status": False,
                        "desc" : value
                    } for key, value in und_tasks.items()

                },
                "number_of_task" : self.ui.number_task.text(),
                "reward" : {
                    key : value for key, value in reward_task.items()
                }

            }
        }

        # self.string_json = json.loads(json_data)
        self.string_json = '; '.join([f'{key.capitalize()} : {value}' for key, value in self.json_data.items()]).replace(",", ",\n\t")
        self.string_json = self.string_json.replace("{", "{\n\t")
        self.string_json = self.string_json.replace("}", "\n\t}")
        self.string_json = self.string_json.replace("False", "false")
        self.string_json = self.string_json.replace("'", "\"")

    def show_here_task(self):
        self.ui.textEdit.setText(self.string_json)

    def export_task_file(self, type='task'):
        with open(f'exported_files/{type}.json', 'w', encoding='utf-8') as jsonfile:
            jsonfile.write("{\n\t" + self.string_json + "\n}")

        self.blit_error_text('Файл успешно экспортирован', 'Экспорт')

        self.EndTaskWin.close()
        self.__init__()


    def check_values_tasks(self):
        if self.ui.nametask.text() != '' and self.ui.taskfrom.text() != '' and\
                self.ui.number_task.text().isdigit() and len(und_tasks) != 0 and len(reward_task) != 0:
            self.create_json_task()
            self.render_endtask_win()
        else:
            self.blit_error_text('Введены не все поля')




if __name__ == "__main__":
    main = Main()