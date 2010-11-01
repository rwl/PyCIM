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

class ErpPersonnel(IdentifiedObject):
    """Information that applies to the basic data about a utility person, used by ERP applications to transfer Personnel data for a worker.
    """

    def __init__(self, ErpPersons=None, status=None, *args, **kw_args):
        """Initializes a new 'ErpPersonnel' instance.

        @param ErpPersons:
        @param status:
        """
        self._ErpPersons = []
        self.ErpPersons = [] if ErpPersons is None else ErpPersons

        self.status = status

        super(ErpPersonnel, self).__init__(*args, **kw_args)

    def getErpPersons(self):
        
        return self._ErpPersons

    def setErpPersons(self, value):
        for x in self._ErpPersons:
            x._ErpPersonnel = None
        for y in value:
            y._ErpPersonnel = self
        self._ErpPersons = value

    ErpPersons = property(getErpPersons, setErpPersons)

    def addErpPersons(self, *ErpPersons):
        for obj in ErpPersons:
            obj._ErpPersonnel = self
            self._ErpPersons.append(obj)

    def removeErpPersons(self, *ErpPersons):
        for obj in ErpPersons:
            obj._ErpPersonnel = None
            self._ErpPersons.remove(obj)

    status = None

