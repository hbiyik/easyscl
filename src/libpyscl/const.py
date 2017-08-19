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
import os


__author__ = "Hüseyin BIYIK"
__copyright__ = """Copyright &copy; 2017 %s.
                All rights reserved in accordance with GPL v2 or later""" % __author__
__credits__ = ["Hüseyin BIYIK"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Hüseyin BIYIK"
__email__ = "huseyinbiyik at hotmail"
__status__ = "Alpha"
__program__ = "easySCL"

rootdir = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))


def resource(*paths):
    return os.path.abspath(os.path.join(rootdir, "libpyscl", "resources", *paths))
