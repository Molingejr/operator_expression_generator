from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import resources_rc


class HelpForm(QDialog):

    def __init__(self, page, parent=None):
        super(HelpForm, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setAttribute(Qt.WA_GroupLeader)

        backAction = QAction(QIcon(":/back.png"), self.tr("&Back"), self)
        backAction.setShortcut(QKeySequence.Back)
        homeAction = QAction(QIcon(":/home.png"), self.tr("&Home"), self)
        homeAction.setShortcut(self.tr("Home"))
        self.pageLabel = QLabel()

        toolBar = QToolBar()
        toolBar.addAction(backAction)
        toolBar.addAction(homeAction)
        toolBar.addWidget(self.pageLabel)
        self.textBrowser = QTextBrowser()

        layout = QVBoxLayout()
        layout.addWidget(toolBar)
        layout.addWidget(self.textBrowser, 1)
        self.setLayout(layout)

        self.connect(backAction, SIGNAL("triggered()"),
                     self.textBrowser, SLOT("backward()"))
        self.connect(homeAction, SIGNAL("triggered()"),
                     self.textBrowser, SLOT("home()"))
        self.connect(self.textBrowser, SIGNAL("sourceChanged(QUrl)"),
                     self.updatePageTitle)

        self.textBrowser.setSearchPaths([":/"])
        self.textBrowser.setSource(QUrl(page))
        self.resize(400, 600)
        self.setWindowTitle(self.tr("{} Help").format(
                QApplication.applicationName()))

    def updatePageTitle(self):
        self.pageLabel.setText(self.textBrowser.documentTitle())


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    form = HelpForm("index.html")
    form.show()
    app.exec_()
