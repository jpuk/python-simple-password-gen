from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QApplication, QClipboard
import os
import generatePasswords


class Ui_MainWindow(object):
    password_generator = generatePasswords.PasswordGenerator()
    number_of_passwords = 20
    number_of_nouns = 1
    number_of_verbs = 0
    number_of_adverbs = 0
    number_of_adjectives = 1
    number_of_symbols = 1
    seperator = str()
    shuffle = False
    capitalize = True
    export_type = 0    # 0 = csv, 1 = plain text
    output_filename = "./output.csv"

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(427, 551)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 60, 256, 391))
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 131, 16))
        self.label.setObjectName("label")
        self.exportPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.exportPushButton.setGeometry(QtCore.QRect(290, 410, 93, 28))
        self.exportPushButton.setObjectName("exportPushButton")
        self.generatePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.generatePushButton.setGeometry(QtCore.QRect(30, 460, 93, 28))
        self.generatePushButton.setObjectName("generatePushButton")
        self.numberOfPasswordsLabel = QtWidgets.QLabel(self.centralwidget)
        self.numberOfPasswordsLabel.setGeometry(QtCore.QRect(160, 30, 55, 16))
        self.numberOfPasswordsLabel.setObjectName("numberOfPasswordsLabel")
        self.exportTypeComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.exportTypeComboBox.setGeometry(QtCore.QRect(300, 380, 73, 22))
        self.exportTypeComboBox.setObjectName("exportTypeComboBox")
        self.nounsSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.nounsSpinBox.setGeometry(QtCore.QRect(290, 100, 42, 22))
        self.nounsSpinBox.setObjectName("nounsSpinBox")
        self.verbsSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.verbsSpinBox.setGeometry(QtCore.QRect(290, 130, 42, 22))
        self.verbsSpinBox.setObjectName("verbsSpinBox")
        self.adverbsSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.adverbsSpinBox.setGeometry(QtCore.QRect(290, 160, 42, 22))
        self.adverbsSpinBox.setObjectName("adverbsSpinBox")
        self.adjectivesSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.adjectivesSpinBox.setGeometry(QtCore.QRect(290, 190, 42, 22))
        self.adjectivesSpinBox.setObjectName("adjectivesSpinBox")
        self.symbolsSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.symbolsSpinBox.setGeometry(QtCore.QRect(290, 220, 42, 22))
        self.symbolsSpinBox.setObjectName("symbolsSpinBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 100, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(340, 130, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(340, 160, 55, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(340, 190, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(340, 220, 55, 16))
        self.label_6.setObjectName("label_6")
        self.seperatorLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.seperatorLineEdit.setGeometry(QtCore.QRect(290, 250, 41, 22))
        self.seperatorLineEdit.setObjectName("seperatorLineEdit")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(340, 250, 61, 16))
        self.label_7.setObjectName("label_7")
        self.passwordsSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.passwordsSpinBox.setGeometry(QtCore.QRect(290, 70, 42, 22))
        self.passwordsSpinBox.setObjectName("passwordsSpinBox")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(340, 70, 61, 16))
        self.label_8.setObjectName("label_8")
        self.capatalizeCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.capatalizeCheckBox.setGeometry(QtCore.QRect(310, 280, 91, 20))
        self.capatalizeCheckBox.setObjectName("capatalizeCheckBox")
        self.shuffleCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.shuffleCheckBox.setGeometry(QtCore.QRect(310, 310, 81, 20))
        self.shuffleCheckBox.setObjectName("shuffleCheckBox")
        self.copyItemPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.copyItemPushButton.setGeometry(QtCore.QRect(290, 340, 93, 28))
        self.copyItemPushButton.setObjectName("copyItemPushButton")
        self.clearListPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearListPushButton.setGeometry(QtCore.QRect(170, 460, 93, 28))
        self.clearListPushButton.setObjectName("clearListPushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 427, 26))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuMenu.addAction(self.actionQuit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ## set ui values to defaults
        self.exportTypeComboBox.addItems(["CSV", "Text"])
        self.exportTypeComboBox.setCurrentIndex(self.export_type)
        self.exportTypeComboBox.setDisabled(True)
        self.passwordsSpinBox.setValue(self.number_of_passwords)
        self.nounsSpinBox.setValue(self.number_of_nouns)
        self.verbsSpinBox.setValue(self.number_of_verbs)
        self.adverbsSpinBox.setValue(self.number_of_adverbs)
        self.adjectivesSpinBox.setValue(self.number_of_adjectives)
        self.symbolsSpinBox.setValue(self.number_of_symbols)
        self.capatalizeCheckBox.setChecked(self.capitalize)
        self.shuffleCheckBox.setChecked(self.shuffle)
        ## message handler connectors
        #self.menuMenu.triggered(self.quitApp())
        self.passwordsSpinBox.valueChanged.connect(self.password_spinbox_changed)
        self.nounsSpinBox.valueChanged.connect(self.nouns_spinbox_changed)
        self.verbsSpinBox.valueChanged.connect(self.verbs_spinbox_changed)
        self.adverbsSpinBox.valueChanged.connect(self.adverbs_spinbox_changed)
        self.adjectivesSpinBox.valueChanged.connect(self.adjectives_spinbox_changed)
        self.symbolsSpinBox.valueChanged.connect(self.symbols_spinbox_changed)
        self.generatePushButton.clicked.connect(self.generate_passwords_push_button_clicked)
        self.exportPushButton.clicked.connect(self.export_push_button_clicked)
        self.exportTypeComboBox.currentIndexChanged.connect(self.export_type_combo_box_changed)
        self.copyItemPushButton.clicked.connect(self.copy_item_push_button_clicked)
        self.capatalizeCheckBox.clicked.connect(self.capatalize_checkbox_clicked)
        self.shuffleCheckBox.clicked.connect(self.shuffle_checkbox_clicked)
        self.clearListPushButton.clicked.connect(self.clear_list_push_button_clicked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password Generator QT"))
        self.label.setText(_translate("MainWindow", "Generated Passwords:"))
        self.exportPushButton.setText(_translate("MainWindow", "Export"))
        self.generatePushButton.setText(_translate("MainWindow", "Generate"))
        self.numberOfPasswordsLabel.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "Nouns"))
        self.label_3.setText(_translate("MainWindow", "Verbs"))
        self.label_4.setText(_translate("MainWindow", "Adverbs"))
        self.label_5.setText(_translate("MainWindow", "Adjectives"))
        self.label_6.setText(_translate("MainWindow", "Symbols"))
        self.label_7.setText(_translate("MainWindow", "Seperator"))
        self.label_8.setText(_translate("MainWindow", "Passwords"))
        self.capatalizeCheckBox.setText(_translate("MainWindow", "Capatalize"))
        self.shuffleCheckBox.setText(_translate("MainWindow", "Shuffle"))
        self.copyItemPushButton.setText(_translate("MainWindow", "Copy Item"))
        self.clearListPushButton.setText(_translate("MainWindow", "Clear List"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))

    ## my functions
    def generate_passwords_push_button_clicked(self):
        print("Generate passwords push button clicked")
        self.password_generator.generate_passwords(number_of_adjectives=self.number_of_adjectives,
                                                   number_of_adverbs=self.number_of_adverbs,
                                                   number_of_nouns=self.number_of_nouns,
                                                   number_of_verbs=self.number_of_verbs,
                                                   number_of_symbols=self.number_of_symbols,
                                                   number_of_passwords=self.number_of_passwords,
                                                   shuffle_password=self.shuffle,
                                                   capitalize=self.capitalize,
                                                   word_separator=self.seperatorLineEdit.text())
        self.listWidget.clear()
        self.listWidget.addItems(self.password_generator.password_list)
        self.numberOfPasswordsLabel.setText(str(len(self.password_generator.password_list)))


    def export_push_button_clicked(self):
        self.output_filename = os.path.abspath(QtWidgets.QFileDialog.getSaveFileName()[0])
        print("Export push button clicked - exporting to {}".format(self.output_filename))
        # fixes bug where clicking cancel will return directory path in osx
        if os.path.isdir(self.output_filename) is not True:
            if self.export_type == 0:
                self.password_generator.write_csv_file(self.password_generator.password_list, self.output_filename)
            else:
                self.password_generator.write_text_file(self.password_generator.password_list, self.output_filename)

    def export_type_combo_box_changed(self):
        print("Export type combo box changed")
        self.export_type = self.exportTypeComboBox.currentIndex()

    def copy_item_push_button_clicked(self):
        item = self.listWidget.currentIndex().data()
        print("Copy item push button clicked - {} - Copied to the clipboard".format(item))
        clip = QApplication.clipboard()
        clip.setText(item)

    def capatalize_checkbox_clicked(self):
        print("Capatlize checkbox clicked")
        if self.capatalizeCheckBox.isChecked():
            self.capatalize = True
        else:
            self.capatalize = False

    def shuffle_checkbox_clicked(self):
        print("Shuffle checkbox clicked")
        if self.shuffleCheckBox.isChecked():
            self.shuffle = True
        else:
            self.shuffle = False

    def password_spinbox_changed(self):
        print("Password spinbox changed")
        self.number_of_passwords = self.passwordsSpinBox.value()

    def nouns_spinbox_changed(self):
        print("Nouns spinbox changed")
        self.number_of_nouns = self.nounsSpinBox.value()

    def verbs_spinbox_changed(self):
        print("Verbs spinbox changed")
        self.number_of_verbs = self.verbsSpinBox.value()

    def adverbs_spinbox_changed(self):
        print("Adverbs spinbox changed")
        self.number_of_adverbs = self.adverbsSpinBox.value()

    def adjectives_spinbox_changed(self):
        print("Adjectives spinbox changed")
        self.number_of_adjectives = self.adjectivesSpinBox.value()

    def symbols_spinbox_changed(self):
        print("Symbols spinbox changed")
        self.number_of_symbols = self.symbolsSpinBox.value()

    def clear_list_push_button_clicked(self):
        print("Clear list push button clicked")
        self.listWidget.clear()
        self.password_generator.password_list = []

    def quitApp(self):
        exit(1)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
