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

from CIM14v13.IEC61968.Common.TelephoneNumber import TelephoneNumber

class ErpTelephoneNumber(TelephoneNumber):
    """The telephone number for a person or organisation.
    """

    def __init__(self, usage='', ElectronicAddress=None, ErpPersons=None, status=None, *args, **kw_args):
        """Initializes a new 'ErpTelephoneNumber' instance.

        @param usage: The purpose of the telephone: home, mobile, home fax, office, office fax, switchboard, other. 
        @param ElectronicAddress:
        @param ErpPersons:
        @param status:
        """
        #: The purpose of the telephone: home, mobile, home fax, office, office fax, switchboard, other. 
        self.usage = usage

        self._ElectronicAddress = None
        self.ElectronicAddress = ElectronicAddress

        self._ErpPersons = []
        self.ErpPersons = [] if ErpPersons is None else ErpPersons

        self.status = status

        super(ErpTelephoneNumber, self).__init__(*args, **kw_args)

    def getElectronicAddress(self):
        
        return self._ElectronicAddress

    def setElectronicAddress(self, value):
        if self._ElectronicAddress is not None:
            filtered = [x for x in self.ElectronicAddress.ErpTelephoneNumbers if x != self]
            self._ElectronicAddress._ErpTelephoneNumbers = filtered

        self._ElectronicAddress = value
        if self._ElectronicAddress is not None:
            self._ElectronicAddress._ErpTelephoneNumbers.append(self)

    ElectronicAddress = property(getElectronicAddress, setElectronicAddress)

    def getErpPersons(self):
        
        return self._ErpPersons

    def setErpPersons(self, value):
        for p in self._ErpPersons:
            filtered = [q for q in p.ErpTelephoneNumbers if q != self]
            self._ErpPersons._ErpTelephoneNumbers = filtered
        for r in value:
            if self not in r._ErpTelephoneNumbers:
                r._ErpTelephoneNumbers.append(self)
        self._ErpPersons = value

    ErpPersons = property(getErpPersons, setErpPersons)

    def addErpPersons(self, *ErpPersons):
        for obj in ErpPersons:
            if self not in obj._ErpTelephoneNumbers:
                obj._ErpTelephoneNumbers.append(self)
            self._ErpPersons.append(obj)

    def removeErpPersons(self, *ErpPersons):
        for obj in ErpPersons:
            if self in obj._ErpTelephoneNumbers:
                obj._ErpTelephoneNumbers.remove(self)
            self._ErpPersons.remove(obj)

    status = None

