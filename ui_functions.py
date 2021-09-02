# GUI FILE
from main import *

# GLOBALS

global_state = 0


class UIFunctions(MainWindow):

    # MAXIMIZE RESTORE FUNCTION
    def maximize_restore(self):
        global global_state
        status = global_state

        # IF NOT MEXIMIZED
        if status == 0:
            self.showMaximized()

            # SET GLOBAL TO 1
            global_state = 1
        else:
            global_state = 0
            self.showNormal()
            self.resize(self.width() + 1, self.height() + 1)

    # UI DEFINITIONS
    def uiDefinitions(self):

        # REMOVE TITLE BAR
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowOpacity(0.95)

        # MAXIMIZE / RESTORE
        self.ui.maximize.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        # MINIMIZE
        self.ui.minimize.clicked.connect(lambda: self.showMinimized())

        # CLOSE
        self.ui.close.clicked.connect(lambda: self.close())

        # CREATE SIZE GRIP TO RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.centralwidget)
        self.sizegrip.setGeometry(870, 570, 400, self.width())

    # RETURN STATUS IF WINDOW IS MAXIMIZED OF RESTORED
    def returnStatus(self):
        return global_state
