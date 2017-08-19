# -*- coding: utf-8 -*-
'''
    Author    : Huseyin BIYIK <husenbiyik at hotmail>
    Year      : 2016
    License   : GPL

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
import logging
import sys

from libpyscl import const

logger = logging.getLogger(const.__program__)


class GuiLogger(logging.Handler):
    def __init__(self, edit, level=0):
        super(GuiLogger, self).__init__(level)
        self.__edit = edit

    def emit(self, record):
        msg = self.format(record)
        self.__edit.appendPlainText(msg)


class stdlogger(object):
    def __init__(self, level):
        self.level = level
        self.message = ""

    def write(self, message):
        if message != "\n":
            if message.endswith("\n"):
                message = self.message + message[:-1]
                self.level(message)
                self.message = ""
            else:
                self.message += message
        else:
            self.level(self.message)
            self.message = ""

    def flush(self):
        self.level(self.message)
        self.message = ""


sys.stdout = stdlogger(logger.info)
sys.stderr = stdlogger(logger.critical)

levels = [10, 20, 30, 40, 50, 0]
defaultlevel = 20
