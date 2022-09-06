# --------------------------------------------------------------------------------------------
# UI StatusBar Class
#
# imported as uiStatusBar
# instanced as: self.uiBar = uiStatus.uiStatusbar(self.statusBar)
#
# --------------------------------------------------------------------------------------------


class uiStatusbar():
    def __init__(self, _qwidget):
        '''
         _qwidget ::: widget of the status bar ui
        '''
        self.statusBar = _qwidget

    # --------------------------------------------------------------------------------------------
    # Methods
    # --------------------------------------------------------------------------------------------

    def success(self, msg):
        # Color green message
        # For succesful operations
        self.statusBar.showMessage(msg)
        self.statusBar.setStyleSheet("color: lime; background: rgba(20, 20, 20, 255);")  # green warning

    def inform(self, msg):
        # Color yellow message
        # for inform messages
        self.statusBar.showMessage(msg)
        self.statusBar.setStyleSheet("color: orange; background: rgba(20, 20, 20, 255);")  # orange warning

    def warning(self, msg):
        # Color orange message
        # for warning messages
        self.statusBar.showMessage(msg)
        self.statusBar.setStyleSheet("color: yellow; background: rgba(20, 20, 20, 255);")  # yellow warning

    def alert(self, msg):
        # Color RED message
        # for failed operations
        self.statusBar.showMessage(msg)
        self.statusBar.setStyleSheet("color: red; background: rgba(20, 20, 20, 255);")  # red warning

    def error(self, msg):
        # Color RED message
        # for failed operations
        self.statusBar.showMessage(msg)
        self.statusBar.setStyleSheet("color: red; background: rgba(20, 20, 20, 255);")  # red warning

    def text(self, msg):
        # Color white message
        self.statusBar.showMessage(msg)
        self.statusBar.setStyleSheet("color: white; background: rgba(20, 20, 20, 255);")  # white warning

    def rule(self, msg):
        # Color purple message
        self.statusBar.showMessage(msg)
        self.statusBar.setStyleSheet("color: fuchsia; background: rgba(20, 20, 20, 255);")  # purple warning
