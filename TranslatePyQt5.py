import os
import sys

from pygtrans import Translate
from PyQt5 import uic
from PyQt5.QtWidgets import *

client = Translate()


class MyGUI(QDialog):

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi('./Gui.ui', self)
        self.show()
        self.setWindowTitle('Translate')

        self.Trans_btn.clicked.connect(self.translate)
        self.clearBtn.clicked.connect(self.clearText)

    def translate(self):
        source = self.sourceText.toPlainText()
        cuText = self.TargetLang.currentText()

        targetID = {'简体中文': 'zh-CN', '繁体中文': 'zh-TW', '马来文': 'ms', '英文': 'en', '韩文': 'ko', '日文': 'ja'}

        text = client.translate(source, target=targetID[cuText])
        self.TextTrans.clear()
        try:
            self.TextTrans.insertPlainText(text.translatedText)
        except AttributeError:
            self.TextTrans.insertPlainText('错误! 无内容\nError! No Content')

    def clearText(self):
        self.TextTrans.clear()
        self.sourceText.clear()


def main():
    global app
    app = QApplication([])
    window = MyGUI()
    app.exec_()


def base_path(path):
    if getattr(sys, 'frozen', None):
        basedir = sys._MEIPASS
    else:
        basedir = os.path.dirname(__file__)
    return os.path.join(basedir, path)


os.chdir(base_path(''))

if __name__ == '__main__':
    main()
