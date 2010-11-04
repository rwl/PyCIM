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

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class ErpTimeEntry(IdentifiedObject):
    """An individual entry on an ErpTimeSheet.
    """

    def __init__(self, ErpProjectAccounting=None, ErpTimeSheet=None, status=None, **kw_args):
        """Initializes a new 'ErpTimeEntry' instance.

        @param ErpProjectAccounting:
        @param ErpTimeSheet:
        @param status:
        """
        self._ErpProjectAccounting = None
        self.ErpProjectAccounting = ErpProjectAccounting

        self._ErpTimeSheet = None
        self.ErpTimeSheet = ErpTimeSheet

        self.status = status

        super(ErpTimeEntry, self).__init__(**kw_args)

    def getErpProjectAccounting(self):
        
        return self._ErpProjectAccounting

    def setErpProjectAccounting(self, value):
        if self._ErpProjectAccounting is not None:
            filtered = [x for x in self.ErpProjectAccounting.ErpTimeEntries if x != self]
            self._ErpProjectAccounting._ErpTimeEntries = filtered

        self._ErpProjectAccounting = value
        if self._ErpProjectAccounting is not None:
            self._ErpProjectAccounting._ErpTimeEntries.append(self)

    ErpProjectAccounting = property(getErpProjectAccounting, setErpProjectAccounting)

    def getErpTimeSheet(self):
        
        return self._ErpTimeSheet

    def setErpTimeSheet(self, value):
        if self._ErpTimeSheet is not None:
            filtered = [x for x in self.ErpTimeSheet.ErpTimeEntries if x != self]
            self._ErpTimeSheet._ErpTimeEntries = filtered

        self._ErpTimeSheet = value
        if self._ErpTimeSheet is not None:
            self._ErpTimeSheet._ErpTimeEntries.append(self)

    ErpTimeSheet = property(getErpTimeSheet, setErpTimeSheet)

    status = None

