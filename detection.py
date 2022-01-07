from PyQt5 import QtCore, QtGui, QtWidgets
import os


class Ui_FaceDetect(object):
    def setupUi(self, FaceDetect):
        FaceDetect.setObjectName("FaceDetect")
        FaceDetect.resize(387, 80)
        self.Detect = QtWidgets.QPushButton(FaceDetect)
        self.Detect.setGeometry(QtCore.QRect(10, 20, 371, 28))
        self.Detect.setObjectName("Detect")

        self.Detect.clicked.connect(self.c1)

        self.retranslateUi(FaceDetect)
        QtCore.QMetaObject.connectSlotsByName(FaceDetect)

    def retranslateUi(self, FaceDetect):
        _translate = QtCore.QCoreApplication.translate
        FaceDetect.setWindowTitle(_translate("FaceDetect", "Security System"))
        self.Detect.setText(_translate("FaceDetect", "Activate Detector"))

    def c1(self):
        os.system('python detect.py')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FaceDetect = QtWidgets.QDialog()
    ui = Ui_FaceDetect()
    ui.setupUi(FaceDetect)
    FaceDetect.show()
    sys.exit(app.exec_())
