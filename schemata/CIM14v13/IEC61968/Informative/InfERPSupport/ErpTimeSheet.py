# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

from CIM14v13.IEC61968.Common.Document import Document

class ErpTimeSheet(Document):
    """Time sheet for employees and contractors. Note that ErpTimeSheet inherits the relationship to ErpPerson from Document.
    """

    def __init__(self, ErpTimeEntries=None, *args, **kw_args):
        """Initializes a new 'ErpTimeSheet' instance.

        @param ErpTimeEntries:
        """
        self._ErpTimeEntries = []
        self.ErpTimeEntries = [] if ErpTimeEntries is None else ErpTimeEntries

        super(ErpTimeSheet, self).__init__(*args, **kw_args)

    def getErpTimeEntries(self):
        
        return self._ErpTimeEntries

    def setErpTimeEntries(self, value):
        for x in self._ErpTimeEntries:
            x._ErpTimeSheet = None
        for y in value:
            y._ErpTimeSheet = self
        self._ErpTimeEntries = value

    ErpTimeEntries = property(getErpTimeEntries, setErpTimeEntries)

    def addErpTimeEntries(self, *ErpTimeEntries):
        for obj in ErpTimeEntries:
            obj._ErpTimeSheet = self
            self._ErpTimeEntries.append(obj)

    def removeErpTimeEntries(self, *ErpTimeEntries):
        for obj in ErpTimeEntries:
            obj._ErpTimeSheet = None
            self._ErpTimeEntries.remove(obj)

