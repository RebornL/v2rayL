from PyQt5.QtCore import qInstallMessageHandler, Qt
from PyQt5.QtWidgets import QApplication

from utils import qt_message_handler
from v2rayLui import MyMainWindow

"""
打包指令（没有压缩）：
pyinstaller -F -w --i images/logo.png  v2rayLui.py
"""
if __name__ == "__main__":
    import sys
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    qInstallMessageHandler(qt_message_handler)
    app = QApplication(sys.argv)
    QApplication.setQuitOnLastWindowClosed(False)  # 禁止默认的closed方法
    myWin = MyMainWindow(app=app)
    # 显示在屏幕上
    myWin.show()
    # 系统exit()方法确保应用程序干净的退出
    # 的exec_()方法有下划线。因为执行是一个Python关键词。因此，exec_()代替
    sys.exit(app.exec_())
