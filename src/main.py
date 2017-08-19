# -*- coding: utf-8 -*-
import sys
import PySide
from PySide import QtGui
import platform

from libpyscl.ui import main
from libpyscl import scl
from libpyscl import const
from libpyscl import log

from libpyscl.elements import nodes


class MainWindow(QtGui.QMainWindow, main.Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        log.logger.addHandler(log.GuiLogger(self.pte_status))
        self.cb_loglvl.activated[int].connect(self.setloglevel)
        self.setloglevel(log.levels.index(log.defaultlevel))
        self.cb_loglvl.setCurrentIndex(log.levels.index(log.defaultlevel))
        self.scl = scl.SCL()
        self.nodes = nodes.NODES(self.trw_nodes, self.scl)
        self.a_about.triggered.connect(self.about)
        self.a_open.triggered.connect(self.open)
        self.show()

    def about(self):
        QtGui.QMessageBox.about(self, u"About {}" % const.__program__,
                                u"""<b>{}</b> v {} <p>{}<p>
                                Python : {} <br>
                                PySide : {} <br>
                                Qt     : {} <br>
                                OS     : {}""".format(const.__program__,
                                                      const.__version__,
                                                      const.__copyright__,
                                                      platform.python_version(),
                                                      PySide.__version__,
                                                      PySide.QtCore.__version__,
                                                      platform.system()))

    def open(self):
        _filter = """SCL(*.cid *.icd *.iid *.scl *.scd);;*.* (*.*)"""
        _file, _filter = QtGui.QFileDialog.getOpenFileName(self, filter=_filter)
        self.scl.open(_file)
        self.nodes.build()

    def setloglevel(self, level):
        log.logger.setLevel(log.levels[level])


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mainWin = MainWindow()
    ret = app.exec_()
    sys.exit(ret)
