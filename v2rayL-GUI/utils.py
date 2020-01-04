# -*- coding:utf-8 -*-
# Author: Suummmmer
# Date: 2019-10-24

import datetime
from PyQt5.QtCore import (
    QtInfoMsg,
    QtWarningMsg,
    QtCriticalMsg,
    QtFatalMsg
)





def qt_message_handler(mode, context, message):
    if mode == QtInfoMsg:
     mode = 'INFO'
    elif mode == QtWarningMsg:
     mode = 'WARNING'
    elif mode == QtCriticalMsg:
     mode = 'CRITICAL'
    elif mode == QtFatalMsg:
     mode = 'FATAL'
    else:
     mode = 'DEBUG'

    msg = message.split("@$ff$@")
    if len(msg) == 2 and msg[0] == "True":
        with open("/etc/v2rayL/v2rayL_op.log", "a+") as f:
            f.write(' %s - %s: %s\n' % (datetime.datetime.now(), mode, msg[1]))
