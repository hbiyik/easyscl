# -*- coding: utf-8 -*-
'''
    Author    : Huseyin BIYIK <husenbiyik at hotmail>
    Year      : 2017
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
from PySide import QtGui

from libpyscl import log
from lxml.etree import QName


class NODES(object):
    def __init__(self, tree, scl):
        self.__tree = tree
        self.scl = scl

    def build(self):
        self.__tree.clear()

        def loop(base, root):
            for node in root:
                name = QName(node.tag)
                display = name.localname
                values = node.values()
                if values:
                    display += "[%s]" % ":".join(values)
                treeitem = QtGui.QTreeWidgetItem(base, [display])
                if node.getchildren():
                    loop(treeitem, node)

        loop(self.__tree, self.scl.scl.getroot())
