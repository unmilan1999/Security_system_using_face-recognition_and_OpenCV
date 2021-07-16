from PyQt5 import QtCore, QtGui, QtWidgets
import os


class Ui_DetectionSystem(object):
    def setupUi(self, DetectionSystem):
        DetectionSystem.setObjectName("DetectionSystem")
        DetectionSystem.resize(400, 300)
        self.register_admin = QtWidgets.QPushButton(DetectionSystem)
        self.register_admin.setGeometry(QtCore.QRect(20, 40, 361, 31))
        self.register_admin.setObjectName("register_admin")
        self.test_admin = QtWidgets.QPushButton(DetectionSystem)
        self.test_admin.setGeometry(QtCore.QRect(20, 140, 361, 31))
        self.test_admin.setObjectName("test_admin")
        self.register_member = QtWidgets.QPushButton(DetectionSystem)
        self.register_member.setGeometry(QtCore.QRect(20, 240, 361, 31))
        self.register_member.setObjectName("register_member")

        self.register_admin.clicked.connect(self.c1)
        self.test_admin.clicked.connect(self.c2)
        self.register_member.clicked.connect(self.c3)

        self.retranslateUi(DetectionSystem)
        QtCore.QMetaObject.connectSlotsByName(DetectionSystem)

    def retranslateUi(self, DetectionSystem):
        _translate = QtCore.QCoreApplication.translate
        DetectionSystem.setWindowTitle(_translate("DetectionSystem", "Detection System"))
        self.register_admin.setText(_translate("DetectionSystem", "Admin Register"))
        self.test_admin.setText(_translate("DetectionSystem", "Admin Test"))
        self.register_member.setText(_translate("DetectionSystem", "Member Register"))

    def c1(self):
        os.system('python admin_register.py')
    def c2(self):
        os.system('python admin_test.py')
    def c3(self):
        os.system('python member_process.py')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DetectionSystem = QtWidgets.QDialog()
    ui = Ui_DetectionSystem()
    ui.setupUi(DetectionSystem)
    DetectionSystem.show()
    sys.exit(app.exec_())
