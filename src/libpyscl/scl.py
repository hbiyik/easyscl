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


from lxml import etree

from libpyscl import const
from libpyscl import log


class SCL(object):
    def __init__(self, scl=None, xsd=None):
        self.__sclfile = None
        self.__xsdfile = None
        self.openschema(xsd)
        if scl:
            scl = self.open(scl)
        else:
            self.__scl = None

    @property
    def schema(self):
        return self.__schema

    @property
    def scl(self):
        return self.__scl

    def openschema(self, xsd):
        if not xsd:
            xsd = const.resource("scd", "iec61850_1_6", "SCL.xsd")
        self.__xsdfile = xsd
        with open(xsd) as x:
            log.logger.info("Loading Schema From : %s" % xsd)
            schema = etree.parse(x)
            log.logger.info("Loaded Schema From : %s" % xsd)
            self.__schema = etree.XMLSchema(schema)
            if self.__sclfile:
                self.open(self.__sclfile)

    def open(self, scl):
        self.__sclfile = scl
        log.logger.info("Loading SCL File from : %s" % self.__sclfile)
        with open(scl) as s:
            self.__scl = etree.parse(s)
            log.logger.info("Loaded SCL File from : %s" % self.__sclfile)
            self.schema.validate(self.__scl)
            errlog = str(self.schema.error_log)
            errors = errlog.count("\n")
            if not errlog == "":
                log.logger.error("Found %d errors in SCL validation from %s" % (errors + 1,
                                                                                self.__xsdfile))
            log.logger.error(errlog)
